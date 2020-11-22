#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author: InTereSTingHE

import requests
import json
from myKey import KEY

''' official website  https://www.qweather.com '''
'''      dev website  https://dev.qweather.com'''
mykey = '&key=' + KEY # EDIT HERE!

url_api_weather = 'https://devapi.qweather.com/v7/weather/'
url_api_geo = 'https://geoapi.qweather.com/v2/city/'
url_api_rain = 'https://devapi.qweather.com/v7/minutely/5m'
url_api_air = 'https://devapi.qweather.com/v7/air/now'

def get(api_type):
    url = url_api_weather + api_type + '?location=' + city_id + mykey
    return requests.get(url).json()

def rain(lat, lon):
    url = url_api_rain  + '?location=' + lat + ',' + lon + mykey
    return requests.get(url).json()

def air(city_id):
    url = url_api_air + '?location=' + city_id + mykey
    return requests.get(url).json()

def get_city(city_kw):
    url_v2 = url_api_geo + 'lookup?location=' + city_kw + mykey
    city = requests.get(url_v2).json()['location'][0]

    city_id = city['id']
    district_name = city['name']
    city_name = city['adm2']
    province_name = city['adm1']
    country_name = city['country']
    lat = city['lat']
    lon = city['lon']

    return city_id, district_name, city_name, province_name, country_name, lat, lon

def now():
    return get_now['now']

def daily():
    return get_daily['daily']

def hourly():
    return get_hourly['hourly']

if __name__ == '__main__':
    print('请输入城市:')
    city_input = input()
    city_idname = get_city(city_input)

    city_id = city_idname[0]

    get_now = get('now')
    get_daily = get('3d') # 3d/7d/10d/15d
    get_hourly = get('24h') # 24h/72h/168h
    get_rain = rain(city_idname[5], city_idname[6]) # input longitude & latitude
    air_now = air(city_id)['now']

    #print(json.dumps(get_now, sort_keys=True, indent=4))
    if city_idname[2] == city_idname[1]:
        print(city_idname[3], str(city_idname[2]) + '市')
    else:
        print(city_idname[3], str(city_idname[2]) + '市', str(city_idname[1]) + '区')
    print('当前天气：', get_now['now']['text'], get_now['now']['temp'], '°C', '体感温度', get_now['now']['feelsLike'], '°C')
    print('空气质量指数：', air_now['aqi'])
    print('降水情况：', get_rain)
    print('今日天气：', daily()[0]['textDay'], daily()[0]['tempMin'], '-', daily()[0]['tempMax'], '°C')

    nHoursLater = 1 # future weather hourly
    print(nHoursLater, '小时后天气：', hourly()[1]['text'], hourly()[1]['temp'], '°C')

    nDaysLater = 1 # future weather daily
    print(nDaysLater, '天后天气：', daily()[nDaysLater]['textDay'], daily()[nDaysLater]['tempMin'], '-', daily()[nDaysLater]['tempMax'], '°C')