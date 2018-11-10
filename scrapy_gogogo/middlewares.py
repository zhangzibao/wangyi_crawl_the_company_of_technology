# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
from selenium import webdriver
import time
import random, base64


# 代理ip
# class ProxyMiddleware(object):
#     proxyList = ['1.196.160.101:9999', '120.79.7.149:80', '58.53.128.83:3128', '112.115.57.20:3128', '118.190.95.35:9001']
#
#     def process_request(self, request, spider):
#         # Set the location of the proxy
#         pro_adr = random.choice(self.proxyList)
#         print("USE PROXY -> " + pro_adr)
#         request.meta['proxy'] = "http://" + pro_adr
# 动态爬虫
class AreaSpiderMiddleware(object):
    def process_request(self, request, spider):
        # 指定谷歌浏览器路径
        if request.url == 'http://finance.sina.com.cn/stock/usstock/sector.shtml#c4m':
            driver = webdriver.Firefox()
            driver.get(request.url)
            time.sleep(1)
            btn = driver.find_elements_by_xpath("/html/body/div[6]/div[2]/div[5]/div[3]/a[3]")[0]
            btn.click()
            html = driver.page_source
            time.sleep(1)
            driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8',
                                            request=request)
