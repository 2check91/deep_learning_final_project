import scrapy
from carscrape.items import CarscrapeItem


class GlassSpider(scrapy.Spider):
    name = 'carscrape'
    start_urls = ['http://www.ebay.com/sch/Bumpers/33640/i.html?_udlo=125&_sop=16&_udhi=400&_dmd=2&_mPrRngCbx=1&_vxp=mtr&_from=R40&_nkw=audi%20a3%20bumper&_dcat=33640&rt=nc',
                  'http://www.ebay.com/sch/i.html?_odkw=audi+a4+bumper&_udlo=125&_sop=16&_udhi=400&_dmd=2&_mPrRngCbx=1&_vxp=mtr&_osacat=6028&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.TRS0&_nkw=audi+a4+bumper&_sacat=6028',
                  'http://www.ebay.com/sch/i.html?_odkw=audi+a6+bumper&_udlo=125&_sop=16&_udhi=400&_dmd=2&_mPrRngCbx=1&_vxp=mtr&_osacat=6028&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.TRS0&_nkw=audi+a6+bumper&_sacat=6028',
                  'http://www.ebay.com/sch/i.html?_odkw=bmw+e46+front+bumper&_udlo=125&_sop=16&_udhi=400&_dmd=2&_mPrRngCbx=1&_vxp=mtr&_osacat=6028&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.TRS0&_nkw=bmw+e46+front+bumper&_sacat=6028']
    
    def parse(self, response):
        image_links = response.css('ul[id="GalleryViewInner"] div[class="imgWr"] a[class="img imgWr2"] img[class="img"]::attr(src)').extract()
        yield CarscrapeItem(image_urls=image_links)
        next_page = response.css('td[class="pagn-next"] a::attr(href)')
        next_page = response.urljoin(next_page.extract_first())
        yield scrapy.Request(next_page, callback=self.parse)

