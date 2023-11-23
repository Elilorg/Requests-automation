# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import json
import time
from scrapy.exceptions import IgnoreRequest

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class AmazondropsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class AmazondropsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class HarMiddleware:
    def __init__(self):
        self.har_data = {
            'log': {
                'version': '1.2',
                'creator': {'name': 'Scrapy', 'version': '1.0'},
                'entries': []
            }
        }

    @classmethod
    def from_crawler(cls, crawler):
        instance = cls()
        crawler.signals.connect(instance.spider_closed, signal=signals.spider_closed)
        return instance

    def process_response(self, request, response, spider):
        error_codes = [500, 502, 503, 504]  # Add more error codes if needed

        newheaders = {}

        for key in request.headers.keys() :
            newheaders[str(key)[2:-1]] = str(request.headers[key])[2:-1]
        
        newhead = {}

        for key in response.headers.keys() :
            newhead[str(key)[2:-1]] = str(response.headers[key])[2:-1]


        if response.status in error_codes:
            self.har_data['log']['entries'].append({
                'request': {
                    'url': request.url,
                    'method': request.method,
                    'headers': newheaders
                },
                'response': {
                    'status': response.status,
                    'headers': newhead
                },
                'time': time.time()
            })
            har_filename = f"{request.url.replace('/', '_')}_{response.status}.har"
            print(self.har_data)
            with open(har_filename, 'w') as har_file:
                json.dump(self.har_data, har_file)
            raise IgnoreRequest(f"Request failed with status {response.status}. HAR file saved as {har_filename}")
        return response

    def spider_closed(self, spider):
        self.har_data['log']['entries'].clear()