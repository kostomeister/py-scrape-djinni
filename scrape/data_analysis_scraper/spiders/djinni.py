import scrapy
from scrapy.http import Response


class DjinniSpider(scrapy.Spider):
    name = "djinni"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/"]

    def parse(self, response: Response, **kwargs):
        pass
