# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones//']
    custom_settings = {
        "FEED_FORMAT": "CSV",
        "FEED_URI": 'exported/reddit.csv'
    }

    def parse(self, response):
        # extracting the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()

        # give the extracted content row wise
        for item in zip(titles, votes, times, comments):
            # create a directory to store the scraped data
            scraped_info = {
                'title': item[0],
                'vote': item[1],
                'created_at': item[2],
                'comments': item[3]
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
