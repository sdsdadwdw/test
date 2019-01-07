#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2019/1/5 0005 下午 7:30'
_author_ = 'Mr yang'
import requests
from bs4 import BeautifulSoup
import csv
#爬取网页信息，并存储到html文件中
def get_html_text(url):
    res = requests.get(url,timeout=30)
    start_pos=url.find('//')+6
    end_pos=url.find('/',start_pos)
    city_name=url.rfind('/')+1
    #命名文件，便于记录
    filename=url[start_pos:end_pos] + '_' +url[city_name:] +'.html'
    with open(filename,'w+',encoding='utf-8') as f:
        f.write(res.text)
    return res.text
#获取城市AQi空气健康指数
def get_city_aqi(city_name):
    # 网页地址
    url = 'http://www.pm25.in/' + city_name
    res = requests.get(url,timeout=30)
    soup = BeautifulSoup(res.text,'lxml')
    div_list = soup.find_all('div',{'class':'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div',{'class':'caption'}).text.strip()
        value = div_content.find('div',{'class':'value'}).text.strip()

        city_aqi.append(value)
    return city_aqi
#获取所有城市名单以及各项空气指标参数
def get_all_cities():
    url = 'http://www.pm25.in/'
    res = requests.get(url,timeout=30)
    soup = BeautifulSoup(res.text,'lxml')

    city_list = []
    city_div=soup.find_all('div',{'class':'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_url = city_link['href'][1:]
        city_list.append((city_name,city_url))
    return city_list
#存储在csv文件中
def get_city_csv():
    city_list = get_all_cities()
    header = ['city_name','AQI','PM2.5/1h','PM10/1h','CO/1h','NO2/1h','O3/1h','O3/8h','SO2/1h']

    with open('china_city_aqi.csv','w+',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i,city in enumerate(city_list):
            if (i+1)%20==0:
                print('已处理{}条记录。（共{}条记录）'.format(i+1,len(city_list)))
            city_name = city[0]
            city_url = city[1]
            city_aqi = get_city_aqi(city_url)
            row = [city_name]+city_aqi
            writer.writerow(row)

def main():
    get_city_csv()
    city_name=input('请输入城市名：')
    url = 'http://www.pm25.in/' + city_name
    get_html_text(url)
    aqi_val = get_city_aqi(city_name)
    print('{}的空气质量指数：{}'.format(city_name,aqi_val[0]))

if __name__=='__main__':
    main()