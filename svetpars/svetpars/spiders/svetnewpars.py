import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Парсим источники освещения на текущей странице
        svets = response.css('div._Ud0k')
        for svet in svets:
            yield {
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.pY3d2 span::text').get(),
                'url': svet.css('a').attrib['href'],
            }

        # Определяем номер текущей страницы
        current_page = int(response.url.split('/')[-1].split('-')[0]) if '-' in response.url else 1

        # Переходим на следующую страницу
        next_page = current_page + 1
        next_url = f'https://www.divan.ru/category/svet/page-{next_page}'
        yield response.follow(next_url, callback=self.parse)