# -*- coding: utf-8 -*-
import scrapy
from gitrepo.items import GitrepoItem

class RepoSpider(scrapy.Spider):
    name = 'repo'
#    allowed_domains = ['github.com']
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for repository in response.css('li.col-12'):
            yield ({
                'name':repository.xpath('.//div/h3/a/text()').extract_first().strip(),
                'update_time':repository.xpath('.//relative-time/@datetime').extract_first()
                })

