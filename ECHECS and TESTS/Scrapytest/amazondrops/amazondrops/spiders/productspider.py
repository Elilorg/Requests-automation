import scrapy
from amazondrops.items import AmazondropsItem


class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["www.amazon.fr"]
    start_urls = ["https://www.amazon.fr/s?i=computers&rh=n%3A429879031&page=2&qid=1682792901"]

    def parse(self, response):
        products = response.css('div[cel_widget_id*="MAIN-SEARCH_RESULTS"]')

        for product in products : 
            Item = AmazondropsItem()
            Item["title"] = product.css("span.a-size-base-plus::text").get(),
            Item["link"] =  "https://www.amazon.fr/" + product.css("a.a-link-normal").attrib.get("href"),
            Item["price"]  =  product.css("span.a-price-whole::text").get(),
            Item["ref_page"] =  response.request.url

            yield{
                "title" : product.css("span.a-size-base-plus::text").get(),
                "link" : "https://www.amazon.fr/" + product.css("a.a-link-normal").attrib.get("href"),
                "price" : product.css("span.a-price-whole::text").get(),
                "page" : response.request.url
            }
        
        next_page = response.css("a.s-pagination-next").attrib.get("href")
        if next_page is not None : 
            next_link = "https://www.amazon.fr" + next_page
            yield response.follow(next_link, callback=self.parse)
