# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dbutils.pooled_db import PooledDB
import pymysql
connect = pymysql.connect(host='172.16.0.106', user='root', password='admin123', charset='utf8', database='qczj',
                              autocommit=True)
cursor = connect.cursor()
sql = """
        insert into qczj.all_model(brand_id, brand_logo, brand_name, fctpy, fctid, fctname, containbookedspec, 
        isforeigncar, levelid, levelname, newenergy, newenergyseriesid, pnglogo, `rank`, seriesimg, seriesname, 
        seriespricemax, seriespricemin, seriesstate, seriesid, seriesplace, uvrank, model_id, model_name, price, 
        stat_id, stat_name) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s) on duplicate key update brand_logo=values(brand_logo), brand_name=values(brand_name), 
        fctpy=values(fctpy), fctid=values(fctid), fctname=values(fctname), containbookedspec=values(containbookedspec), 
        isforeigncar=values(isforeigncar), levelid=values(levelid), levelname=values(levelname), 
        newenergy=values(newenergy), newenergyseriesid=values(newenergyseriesid), pnglogo=values(pnglogo), 
        `rank`=values(`rank`), seriesimg=values(seriesimg), seriesname=values(seriesname), 
        seriespricemax=values(seriespricemax), seriespricemin=values(seriespricemin), seriesstate=values(seriesstate), 
        seriesplace=values(seriesplace), uvrank=values(uvrank), model_name=values(model_name), price=values(price), 
        stat_id=values(stat_id), stat_name=values(stat_name),`status`='0'
    """


class QczjItem(scrapy.Item):
    brand_id = scrapy.Field()
    brand_logo = scrapy.Field()
    brand_name = scrapy.Field()
    fctPy = scrapy.Field()
    fctid = scrapy.Field()
    fctname = scrapy.Field()
    containbookedspec = scrapy.Field()
    isForeignCar = scrapy.Field()
    levelId = scrapy.Field()
    levelName = scrapy.Field()
    newenergy = scrapy.Field()
    newenergySeriesId = scrapy.Field()
    pnglogo = scrapy.Field()
    rank = scrapy.Field()
    seriesImg = scrapy.Field()
    seriesName = scrapy.Field()
    seriesPriceMax = scrapy.Field()
    seriesPriceMin = scrapy.Field()
    seriesState = scrapy.Field()
    seriesid = scrapy.Field()
    seriesplace = scrapy.Field()
    uvRank = scrapy.Field()
    status_id = scrapy.Field()
    status_name = scrapy.Field()
    model_id = scrapy.Field()
    model_name = scrapy.Field()
    model_price = scrapy.Field()
    cursor.execute(sql, (brand_id, brand_logo, brand_name, fctPy, fctid, fctname, containbookedspec, isForeignCar,
                             levelId, levelName, newenergy, newenergy, pnglogo, rank, seriesImg, seriesName,
                             seriesPriceMax, seriesPriceMin, seriesState, seriesid, seriesplace, uvRank, model_id,
                             model_name, model_price, status_id, status_name))

