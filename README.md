# xinlang_crawl_the_company_of_technology
## 本爬虫用于爬取新浪财经网上美股之科技板块排名前60的上市公司

新浪财经网有点机灵，表格数据是动态的，直接爬取是无法获得，因此使用了selenium，即web自动化测试这个插件，配合火狐浏览器模拟真实的浏览器操作，从而得到数据。
另外延迟请保持为1，否则将会被封ip。

## 使用此源码。

> 1. 项目根目录命令行执行 pip install -r requirements.txt
> 2. 请参考此链接完成动态爬虫所需要的插件配置 [使用Selenium进行动态爬虫](https://www.jianshu.com/p/5eeb14bc55fc "Title")
> 3. 接着运行main.py 即可，数据保存在Article.json 中，可能部分数据有所残缺，在test/test.py 中有对其整理，最终生成data.csv 为整齐的格式数据。
