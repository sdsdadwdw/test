#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2018/11/29 0029 下午 7:14'
_author_ = 'Mr yang'
#设置密码并保存至文件
def main():
    try_time = 5
    while try_time>0:
        pass_word = input('请输入密码(>8位)：')
        #设置强度等级
        pass_strength = 0
        #规则1长度必须>8
        if len(pass_word )>=8:
            pass_strength +=1
        else:
            print("密码长度至少8位！")
        #规则2 密码包含数字
        if judge_isnumber(pass_word):
            pass_strength +=1
        else:
            print('密码必须包含数字！')
        #规则3 密码必须包含字母
        if judge_istr(pass_word):
            pass_strength +=1
        else:
            print('密码中必须包含字母！')
        if pass_strength == 1:
            strength = '弱'
        elif pass_strength ==2:
            strength = '较弱'
        else:
            strength = '强'
        f =open('pass_wordv2.0.txt','a')
        f.write('密码：{}，强度：{}\n'.format(pass_word,strength))
        f.close()
        if pass_strength >=3:
            print('恭喜！密码创建成功！')
            break
        else:
            print('密码创建失败！')
            try_time -=1
        print()
    if try_time<=0:
        print('尝试次数过多，创建密码失败！')
#判断是否有字符串
def judge_istr(pass_word):
    get_alpha = False
    for c in pass_word:
        if c.isalpha():
            get_alpha = True
            break
    return get_alpha

#判断是否有数字
def judge_isnumber(pass_word):
    get_num = False
    for c in pass_word:
        if c.isnumeric():
            get_num = True
            break
    return get_num


if __name__ == '__main__':
    main()