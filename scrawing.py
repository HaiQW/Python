#python scrapy testing
from scrapy import Spider,Item,Field
class Post(Item):
    tittle = Field()
class BlogSpider(Spider):
    name, star_urls = 'blogspider',['http://blog.scrapinghub.com']
    def parse(self,response):
        return [Post(tittle = e.extract()) for e in response.css("h2 a::text")]

nnat > myspider.py <<EOF

from scrapy import Spider, Item, Field

class Post(Item):
    title = Field()

class BlogSpider(Spider):
    name, start_urls = 'blogspider', ['http://blog.scrapinghub.com']

    def parse(self, response):
        return [Post(title=e.extract()) for e in response.css("h2 a::text")]

EOF
 scrapy runspider myspider.pyat > myspider.py <<EOF

from scrapy import Spider, Item, Field

class Post(Item):
    title = Field()

class BlogSpider(Spider):
    name, start_urls = 'blogspider', ['http://blog.scrapinghub.com']

    def parse(self, response):
        return [Post(title=e.extract()) for e in response.css("h2 a::text")]

EOF
 scrapy runspider myspider.py
