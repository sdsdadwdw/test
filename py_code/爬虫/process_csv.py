#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2019/1/7 0007 上午 10:13'
_author_ = 'Mr yang'
import pandas as pd

def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())
    print(aqi_data.head())

    #数据基本处理
    print('全国AQI指数的最大值：',aqi_data['AQI'].max())
    print('全国AQI指数的最小值：', aqi_data['AQI'].min())
    print('全国AQI指数的平均值：', aqi_data['AQI'].mean())

    #排序top10 and bottom10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)

   # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'],ascending=False).head(10)
    print('全国空气质量最差的10个城市：')
    print(bottom10_cities)

    #将top10和bottom10保存到csv文件中
    top10_cities.to_csv('top10_cities.csv',encoding='utf-8',index=False)
    bottom10_cities.to_csv('bottom10_cities.csv',encoding='utf-8',index=False)

if __name__ == '__main__':
    main()