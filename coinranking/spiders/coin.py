import scrapy


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['coinranking.com']
    start_urls = ['https://coinranking.com']

    def parse(self, response):
        rows = response.xpath('//tbody[@class="table__body"]/tr[not(contains(@class, "table__row--ad"))]')
        for row in rows:
            name = row.xpath('.//td[1]/div/span[@class="profile__name"]/a/text()').get()
            symbol = row.xpath('.//td[1]/div/span[@class="profile__name"]/span/text()').get()
            price = row.xpath('normalize-space(.//td[2]/div/text())').get()
            market_cap = row.xpath('normalize-space(.//td[3]/div/text())').get()
            change_24hr = row.xpath('normalize-space(.//td[4]/div/text())').get()
            yield{
                "Name": name.strip(),
                "Symbol": symbol.strip(),
                "Price": price,
                "Market Cap": market_cap,
                "24hr Change": change_24hr
            }
        next_page = response.xpath(
            '//div[@class="pagination__buttons"]/a[not(contains(@class, "--disabled")) and contains(text(), "Next")]/@href'
        ).get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
