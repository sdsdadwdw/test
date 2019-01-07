#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2019/1/7 0007 上午 11:19'
_author_ = 'Mr yang'
import pandas as pd
import matplotlib.pyplot as plt
#解决中文字显示问题
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())
    print(aqi_data.head())
    #数据清洗，排除掉aqi=0的城市
    aqi_clean_data = aqi_data[aqi_data['AQI']>0]

    #数据基本处理
    print('全国AQI指数的最大值：',aqi_clean_data['AQI'].max())
    print('全国AQI指数的最小值：', aqi_clean_data['AQI'].min())
    print('全国AQI指数的平均值：', aqi_clean_data['AQI'].mean())

    '''
    #排序top10 and bottom10
    top10_cities = aqi_clean_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)

   # bottom10_cities = aqi_clean_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_clean_data.sort_values(by=['AQI'],ascending=False).head(10)
    print('全国空气质量最差的10个城市：')
    print(bottom10_cities)

    #将top10和bottom10保存到csv文件中
    top10_cities.to_csv('top10_cities.csv',encoding='utf-8',index=False)
    bottom10_cities.to_csv('bottom10_cities.csv',encoding='utf-8',index=False)'''
    #统计空气质量较好的前50个城市，并可视化保存图片
    top50_cities=aqi_clean_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar',x='city_name',y='AQI',title='空气质量最好的50城市',figsize=(15,8))

    plt.savefig('top50_aqi.png')
    plt.show()

if __name__ == '__main__':
    main()