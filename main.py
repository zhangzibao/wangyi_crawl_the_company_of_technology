from scrapy.cmdline import execute
import sys, os

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'find_company'])
# import django
# from spiders.tools.proxyip import GetIP
#
# sys.path.append('../../../Charlotte')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'Charlotte.settings'
# django.setup()
#
# getip = GetIP()
# print(getip.get_random_ip())
