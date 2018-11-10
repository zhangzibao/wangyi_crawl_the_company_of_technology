# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class wangyi_CTRP_indicator_Item(scrapy.Item):
    title = scrapy.Field()
    TotalRevenue = scrapy.Field()
    CostofRevenue = scrapy.Field()
    GrossProfit = scrapy.Field()
    ResearchandDevelopment = scrapy.Field()
    SalesGeneral_Admin = scrapy.Field()
    NonRecurringItems = scrapy.Field()
    OtherOperatingItems = scrapy.Field()
    OperatingIncome = scrapy.Field()
    Add_income_expenseitems=scrapy.Field()
    EarningsBeforeInterest_Tax = scrapy.Field()
    InterestExpense = scrapy.Field()
    EarningsBeforeTax = scrapy.Field()
    IncomeTax = scrapy.Field()
    MinorityInterest = scrapy.Field()
    EquityEarningsLossUnconsolidatedSubsidiary = scrapy.Field()
    NetIncome_Cont_Operations = scrapy.Field()
    NetIncome = scrapy.Field()
    NetIncomeApplicableShareholders = scrapy.Field()
class wangyi_year_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass