#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2018/11/19 0019 下午 7:19'
_author_ = 'Mr yang'
#4.0新增功能：将汇率兑换功能封装到函数中

def convert_currency(im,er):
    '''
        汇率兑换
    '''
    out = im*er
    return out

#带单位货币输入
currency_str_value=input('请输入带单位的货币金额：')
#获取货币单位
unit = currency_str_value[-3:]
#汇率
usd_vs_rmb = 6.99
if unit == 'CNY':
    exchange_rate = 1 / usd_vs_rmb

elif unit == 'USD':
    exchange_rate = usd_vs_rmb

else:
    exchange_rate = -1

if exchange_rate !=-1:
    in_money = eval(currency_str_value[:-3])
    #调用函数
    out_money = convert_currency(in_money,exchange_rate)
    print('转换后的金额:',out_money)
else:
    print('不支持这种货币!')


