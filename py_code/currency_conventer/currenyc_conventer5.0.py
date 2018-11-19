#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2018/11/19 0019 下午 7:40'
_author_ = 'Mr yang'
#5.0 (1)使程序结构化.(2)简单函数的定义 lambda <函数名>=lambda<参数列表>:<表达式>

# def convert_currency(im,er):
#     '''
#         汇率兑换
#     '''
#     out = im*er
#     return out

def main():
    '''
        主函数
    '''
    # 带单位货币输入
    currency_str_value = input('请输入带单位的货币金额：')
    # 获取货币单位
    unit = currency_str_value[-3:]
    # 汇率
    usd_vs_rmb = 6.99
    if unit == 'CNY':
        exchange_rate = 1 / usd_vs_rmb
    elif unit == 'USD':
        exchange_rate = usd_vs_rmb
    else:
        exchange_rate = -1
    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        #使用lambda定义函数
        convert_currency2 = lambda x:x *exchange_rate
        # # 调用函数
        # out_money = convert_currency(in_money, exchange_rate)
        #调用lambda函数
        out_money = convert_currency2(in_money)
        print('转换后的金额:', out_money)
    else:
        print('不支持这种货币!')

if __name__ == '__main__':
    main()


