import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        bookTitle = response.css("h3 a::attr(title)").getall()
        for title in bookTitle:
            # print(title)
            yield
            {
                'bookTitle':title
            }
        
        
