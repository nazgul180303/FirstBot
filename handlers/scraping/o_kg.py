from parsel import Selector
import requests


class ServiceOScrapper:
    URL = 'https://www.o.kg/ru/chastnym-klientam/uslugi/uslugi/'
    LINK_XPATH = '//div[@class="col-lg-9 col-xs-12"]/div/a/@href'
    PLUS_URL = 'https://www.o.kg'

    def parse_data(self):
        html = requests.get(self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
             print(self.PLUS_URL + link)
        return links[:5]


if __name__ == '__main__':
    scraper = ServiceOScrapper()
    scraper.parse_data()
