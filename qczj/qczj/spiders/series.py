import copy
import re

import scrapy
from scrapy import cmdline
import json
import pymysql
from qczj import sql


class SeriesSpider(scrapy.Spider):
    name = 'series'
    # allowed_domains = ['autohome.com']
    # start_urls = ['http://autohome.com/']
    connect = pymysql.connect(host='172.16.0.121', user='root', password='admin123', charset='utf8', database='qczj')
    cursor = connect.cursor()
    connect.ping()

    def start_requests(self):
        yield scrapy.Request(url='https://www.autohome.com.cn/ashx/index/GetHomeFindCar.ashx',callback=self.parse)

    def parse(self, response, **kwargs):
        url = 'https://www.autohome.com.cn/ashx/index/GetHomeFindCar.ashx?brandId={}&type=1'
        json_data = json.loads(str(response.text).replace('var IndexFindCarBrand=',''))
        for row in json_data:
            id = row['id']
            name = row['name']
            letter = row['letter']
            self.cursor.execute(sql.brand_sql, (id, name, letter))
            self.connect.commit()
            yield scrapy.Request(url=url.format(id), callback=self.parse_one)

    def parse_one(self, response):
        url = 'https://www.autohome.com.cn/ashx/index/GetHomeFindCar.ashx?type=2&seriesid={}&format=json&v=1'
        result = json.loads(str(response.text))['result']
        brand_id = result['brandid']
        brand_logo = result['brandlogo']
        brand_name = result['brandname']
        for fctlist in result['fctlist']:
            for series in fctlist['serieslist']:
                fctPy = series['fctPy']
                fctid = series['fctid']
                fctname = series['fctname']
                containbookedspec = series['containbookedspec']
                isForeignCar = series['isForeignCar']
                levelId = series['levelId']
                levelName = series['levelName']
                newenergy = series['newenergy']
                newenergySeriesId = series['newenergySeriesId']
                pnglogo = series['pnglogo']
                rank = series['rank']
                seriesImg = series['seriesImg']
                seriesName = series['seriesName']
                seriesPriceMax = series['seriesPriceMax']
                seriesPriceMin = series['seriesPriceMin']
                seriesState = series['seriesState']
                seriesid = series['seriesid']
                seriesplace = series['seriesplace']
                uvRank = series['uvRank']
                self.cursor.execute(sql.series_sql,(brand_id, brand_logo, brand_name, fctPy, fctid, fctname,
                                                    containbookedspec, isForeignCar, levelId, levelName, newenergy,
                                                    newenergySeriesId, pnglogo, rank, seriesImg, seriesName,
                                                    seriesPriceMax, seriesPriceMin, seriesState, seriesid, seriesplace,
                                                    uvRank))
                self.connect.commit()
                self.cursor.execute(sql.update_brand_status, ('1', brand_id))
                self.connect.commit()
                yield scrapy.Request(url=url.format(seriesid), callback=self.parse_two)

    def parse_two(self, response):
        series_id = re.search('seriesid=(?P<seriesid>\d+)&',response.url).group('seriesid')
        try:
            model_data_list = json.loads(response.text)
            for status in model_data_list:
                status_id = status['id']
                status_name = status['name']
                for model in status['list']:
                    model_id = model['id']
                    model_name = model['name']
                    model_price = model['price']
                    self.connect.ping()
                    self.cursor.execute(sql.model_sql, (series_id, model_id, model_name, model_price, status_id, status_name))
                    self.connect.commit()
                    self.cursor.execute(sql.update_series_status, ('1', series_id))
                    self.connect.commit()
        except (Exception, EOFError) as e:
            self.cursor.execute(sql.update_series_status, ('3', series_id))
            self.connect.commit()


if __name__ == '__main__':
    cmdline.execute('scrapy crawl series'.split())