#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2018.5.4
_date_ = '2018/11/21 0021 上午 9:59'
_author_ = 'Mr yang'
import turtle
def draw_branch(branch_length):
    if branch_length >5:
        #绘制右树枝
        turtle.forward(branch_length)
        print('向前',branch_length)
        turtle.right(20)
        print('向右20')
        draw_branch(branch_length - 15)
        #绘制左树枝
        turtle.left(40)
        print('向左40')
        draw_branch(branch_length-15)
        #返回之前的树枝
        turtle.right(20)
        print('向右20')
        turtle.backward(branch_length)
        print('向后',branch_length)

def main():

    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.pencolor('brown')
    branch_length= eval(input('请输入树干长度：'))
    draw_branch(branch_length)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
