#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2018/11/21 0021 上午 9:45'
_author_ = 'Mr yang'
#新增功能：使用迭代函数绘制不同大小的函数
import turtle

#函数绘制五角星
def draw_pentagram(size):
    count = 1
    while count <= 5:
        # 第一条边
        turtle.forward(size)
        turtle.right(144)
        count +=  1

def draw_recursive_pentagram(size):
    '''
    迭代绘制五角星
    '''
    draw_pentagram(size)
    #五角星绘制完成，更新参数
    size +=10
    if size<=100:
        draw_recursive_pentagram(size)
def main():
    '''主函数'''
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')
    size = 50
    draw_recursive_pentagram(size)
    turtle.exitonclick()

if __name__ == '__main__':
    main()