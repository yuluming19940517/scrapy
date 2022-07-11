brand_sql = "insert into qczj.brand(id,`name`,letter) values(%s, %s, %s) on duplicate key update `status`='0'"

series_sql = """
    insert into qczj.series(brand_id, brand_logo, brand_name, fctpy, fctid, fctname, containbookedspec, 
    isforeigncar, levelid, levelname, newenergy, newenergyseriesid, pnglogo, `rank`, seriesimg, seriesname, 
    seriespricemax, seriespricemin, seriesstate, seriesid, seriesplace, uvrank) values (%s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) on duplicate key update brand_logo=values(brand_logo), 
    brand_name=values(brand_name), fctpy=values(fctpy), fctid=values(fctid), fctname=values(fctname), 
    containbookedspec=values(containbookedspec), isforeigncar=values(isforeigncar), levelid=values(levelid), 
    levelname=values(levelname), newenergy=values(newenergy), newenergyseriesid=values(newenergyseriesid), 
    pnglogo=values(pnglogo), `rank`=values(`rank`), seriesimg=values(seriesimg), seriesname=values(seriesname), 
    seriespricemax=values(seriespricemax), seriespricemin=values(seriespricemin), seriesstate=values(seriesstate), 
    seriesplace=values(seriesplace), uvrank=values(uvrank),`status`='0';
"""

update_brand_status = "update qczj.brand set `status`=%s where id=%s"

model_sql = """
    insert into qczj.model(seriesid, id, `name`, price, stat_id, stat_name) values (%s, %s, %s, %s, %s, %s)
    on duplicate key update `name`=values(`name`), price=values(price), stat_id=values(stat_id), 
    stat_name=values(stat_name),`status`='0';
"""

update_series_status = "update qczj.series set `status`=%s where seriesid=%s"