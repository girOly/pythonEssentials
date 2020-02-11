import scrapy


class GenericSpider(scrapy.Spider):
    name = "generic_spider"
    start_urls = ['url']

    def parse(self, response):

        BOX_SELECTOR = '.product-box.left.medium-6.small-6'
        for item in response.css(BOX_SELECTOR):
            IMG_SELECTOR = '//img/src'
            NAME_SELECTOR = '.product-name-container ::text'
            LINK_SELECTOR = '.image-box ::attr(href)'

            results = {
                'name': item.css(NAME_SELECTOR).extract_first(),
                'link': item.css(LINK_SELECTOR).extract_first(),
                'image': item.xpath(IMG_SELECTOR).extract_first()
            }
            yield results

        # for link in link_obj['list_of_stuffs']:
            next_page = results['link']
            if next_page is not None:
                print('Scraping')
                next_page_link = response.urljoin(next_page)
                yield scrapy.Request(url=next_page_link, callback=self.parse_two)
                # yield scrapy.Request(response.urljoin(next_page),
                # callback= self.parse_two)
                # link_obj['list_of_stuffs'].remove(link)

    def parse_two(self, response):
        #     # print('===============')
        INDV_BOX_SELECTOR = '.gallery-img-item'
        for item in response.css(INDV_BOX_SELECTOR):
            IMAGE_ITEM_SELECTOR = 'img ::attr(src)'
            if item.css(IMAGE_ITEM_SELECTOR).startswith('//generic_url'):
                yield {
                    'image': item.css(IMAGE_ITEM_SELECTOR).extract_first()
                }
