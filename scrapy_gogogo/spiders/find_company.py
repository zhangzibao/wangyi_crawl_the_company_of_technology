import scrapy
from selenium import webdriver
import time
from scrapy_gogogo.items import wangyi_CTRP_indicator_Item


class find_company(scrapy.Spider):
    name = "find_company"

    # allowed_domains = ["www.baidu.com"]
    # start_urls = 'https://www.baidu.com/'
    # base_url = 'https://www.baidu.com'
    def start_requests(self):
        url = "http://finance.sina.com.cn/stock/usstock/sector.shtml#c4m"
        yield scrapy.Request(url=url, callback=self.parse )
        # url = "https://www.nasdaq.com/symbol/msft/financials?query=income-statement"
        # yield scrapy.Request(url=url, callback=self.table_parse)

    def parse(self, response):
        print("hello")
        urls = response.xpath("//table//td[@class='nocolor max_name']/a/@href")
        titles = response.xpath("//table//td[@class='nocolor max_name']/a/@title")
        for title, url in zip(titles, urls):
            print(title.extract(), end=":")
            print(url.extract())
            yield scrapy.Request(url=url.extract(), callback=self.detail_parse,meta={"title":title.extract()})

    def detail_parse(self, response):
        url = response.xpath("//div[@class='links']//ul//li/a/@href")[2].extract()  # 历史价格
        tail = url.split('/')[-1]
        url = url.replace(tail, 'financials?query=income-statement')
        yield scrapy.Request(url=url, callback=self.table_parse ,meta=response.meta)
        # yield scrapy.Request(url=url, callback=self.parse)

    def table_parse(self, response):
        item = wangyi_CTRP_indicator_Item()
        thes = response.xpath('//div[@class="genTable"]/table//td/text()')
        i = 0
        year_2015 = 3  # 得出初始位数3
        for th in thes:
            i += 1
            if i % 4 == year_2015:
                num = ''.join([x for x in th.extract() if x.isdigit()])
                if i == year_2015 + 4 * 0:
                    item['TotalRevenue'] = num
                elif i == year_2015 + 4:
                    item['CostofRevenue'] = num
                elif i == year_2015 + 4 * 2:
                    item['GrossProfit'] = num
                elif i == year_2015 + 4 * 3:
                    item['ResearchandDevelopment'] = num
                elif i == year_2015 + 4 * 4:
                    item['SalesGeneral_Admin'] = num
                elif i == year_2015 + 4 * 5:
                    item['NonRecurringItems'] = num
                elif i == year_2015 + 4 * 6:
                    item['OtherOperatingItems'] = num
                elif i == year_2015 + 4 * 7:
                    item['OperatingIncome'] = num
                elif i == year_2015 + 4 * 8:
                    item['Add_income_expenseitems'] = num
                elif i == year_2015 + 4 * 9:
                    item['EarningsBeforeInterest_Tax'] = num
                elif i == year_2015 + 4 * 10:
                    item['InterestExpense'] = num
                elif i == year_2015 + 4 * 11:
                    item['EarningsBeforeTax'] = num
                elif i == year_2015 + 4 * 12:
                    item['IncomeTax'] = num
                elif i == year_2015 + 4 * 13:
                    item['MinorityInterest'] = num
                elif i == year_2015 + 4 * 14:
                    item['EquityEarningsLossUnconsolidatedSubsidiary'] = num
                elif i == year_2015 + 4 * 15:
                    item['NetIncome_Cont_Operations'] = num
                elif i == year_2015 + 4 * 16:
                    item['NetIncome'] = num
                elif i == year_2015 + 4 * 17:
                    item['NetIncomeApplicableShareholders'] = num
            if i % 4 == 0:
                print()
        item['title'] = response.meta['title']
        yield item
