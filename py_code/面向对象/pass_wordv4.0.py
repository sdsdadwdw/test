#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2018/12/19 0019 下午 4:59'
_author_ = 'Mr yang'

#判断密码类
class PasswordTool:
    #初始化类的属性
    def __init__(self,password):
        self.password=password
        self.pass_strength=0
    #类的方法
    def process_password(self):
        #规则1长度必须>8
        if len(self.password )>=8:
            self.pass_strength +=1
        else:
            print("密码长度至少8位！")
        #规则2 密码包含数字
        if self.judge_isnumber():
            self.pass_strength +=1
        else:
            print('密码必须包含数字！')
        #规则3 密码必须包含字母
        if self.judge_istr():
            self.pass_strength +=1
        else:
            print('密码中必须包含字母！')
    # 判断是否有字符串
    def judge_istr(self):
        get_alpha = False
        for c in self.password:
            if c.isalpha():
                get_alpha = True
                break
        return get_alpha

    # 判断是否有数字
    def judge_isnumber(self):
        get_num = False
        for c in self.password:
            if c.isnumeric():
                get_num = True
                break
        return get_num

#操作文件类
class FileTool:
    def __init__(self,filepath):
        self.filepath = filepath
    def write_to_file(self,line):
        f = open(self.filepath,'a')
        f.write(line)
        f.close()
    def read_from_file(self):
        f =open(self.filepath,'r')
        lines = f.readlines()
        f.close()
        return lines

#面向对象的特点：封装、继承、多态

def main():
    try_time = 5
    filepath='pass_wordv2.0.txt'
    # 实例化文件操作类对象
    file_tool = FileTool(filepath)
    while try_time>0:
        password = input('请输入密码(>8位)：')
        #实例化对象
        password_tool=PasswordTool(password)
        password_tool.process_password()

        if password_tool.pass_strength == 1:
            strength = '弱'
        elif password_tool.pass_strength ==2:
            strength = '较弱'
        else:
            strength = '强'
        line = '密码：{}，强度：{}\n'.format(password,strength)
        file_tool.write_to_file(line)
        if password_tool.pass_strength >=3:
            print('恭喜！密码创建成功！')
            break
        else:
            print('密码创建失败！')
            try_time -=1
        print()
    if try_time<=0:
        print('尝试次数过多，创建密码失败！')
    #读操作
    lines = file_tool.read_from_file()
    print(lines)

if __name__ == '__main__':
    main()