# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class ScrapyGogogoPipeline(object):
    def __init__(self):
        self.file = codecs.open('Article.json', 'w', encoding="utf-8")
        pass

    def process_item(self, item, spider):
        # with codecs.open('Article.json', 'a+', encoding='utf-8') as f:
            # lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        json.dump(dict(item), self.file,ensure_ascii =False)
        return item

    def spider_closed(self, spider):
        self.file.close()
        pass

