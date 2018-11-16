# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item

import scrapy
from tecnologia.items import FilmesItem

class FilmesSpider(scrapy.Spider):
    name = 'Wiki'
    allowed_domains = ['pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria']
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria']

    def parse(self, response):
        for lista in response.css("a"):
            link = lista.css("a::attr(href)").extract_first()
            title = lista.css("a::text").extract_first()
            yield {'link': link, 'title': title}


    def parse_article(self, response):
        link = response.url
        title = response.css("title ::text").extract_first()

        notice = FilmesItem(link=link, title=title)
        yield notice