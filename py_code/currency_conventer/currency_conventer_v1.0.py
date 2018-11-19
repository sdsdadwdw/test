#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2018/11/13 0013 上午 10:17'
_author_ = 'Mr yang'
#带单位货币输入
currency_str_value=input('请输入带单位的货币金额：')
#获取货币单位
unit = currency_str_value[-3:]
#汇率
usd_vs_rmb = 6.99
if unit == 'CNY':
    #输入的人民币
    rmb_str_value = currency_str_value[:-3]
    #将字符串转换为数字
    rmb_value = eval(rmb_str_value)
    #计算汇率
    usd_value = rmb_value/usd_vs_rmb
    #输出美元结果
    print("美元(USD)金额是：",usd_value)
elif unit == 'USD':
    #输入的dollar
    usd_str_value = currency_str_value[:-3]
    #将字符串转换为数字
    usd_value = eval(usd_str_value)
    #计算汇率
    rmb_value = usd_value*usd_vs_rmb
    #输出RMB结果
    print("人民币(CNY)金额是：",rmb_value)
else:
    #其他情况
    print("目前版本尚不支持该货币！")

