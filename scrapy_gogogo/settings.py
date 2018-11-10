BOT_NAME = 'scrapy_gogogo'
SPIDER_MODULES = ['scrapy_gogogo.spiders']
NEWSPIDER_MODULE = 'scrapy_gogogo.spiders'
DEFAULT_ITEM_CLASS = 'scrapy_gogogo.items.wangyi_CTRP_indicator_Item'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False
DOWNLOADER_MIDDLEWARES = {
    "scrapy_gogogo.middlewares.AreaSpiderMiddleware": 400,
    # "scrapy_gogogo.middlewares.ProxyMiddleware": 200,
}
ITEM_PIPELINES = {
    'scrapy_gogogo.pipelines.ScrapyGogogoPipeline': 300
}
