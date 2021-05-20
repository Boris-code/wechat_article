# -*- coding: utf-8 -*-
"""
Created on 2021/5/20 5:11 下午
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
"""

from turtle import *
import turtle as t


t.up()
t.goto(-300, 0)
t.color("black")
t.pensize(2)
t.down()
t.left(40)
t.forward(50)

t.right(40)
t.forward(30)
t.right(90)
t.forward(40)
t.right(180)
t.up()
t.forward(40)
t.left(90)
t.forward(30)
t.right(90)
t.down()
t.forward(50)
# 手下
t.right(90)
t.forward(50)
t.right(40)
t.forward(30)
t.up()
t.right(180)
t.forward(30)
t.left(40)
t.forward(50)
t.right(90)
t.down()
t.forward(20)
# 手上
t.right(90)
t.forward(50)
t.left(40)
t.forward(30)
t.up()
t.right(180)
t.forward(30)
t.right(40)
t.forward(50)
t.right(90)
t.down()
# 头
t.forward(40)
t.right(90)
t.circle(30, 360)


# 左眼
t.up()
t.goto(-275, 175)
t.down()
t.fillcolor("black")
t.begin_fill()
t.circle(3)
t.end_fill()

# 右眼
t.up()
t.goto(-250, 175)
t.down()

t.fillcolor("black")
t.begin_fill()
t.circle(3)
t.end_fill()

# 微笑
t.up()
t.goto(-270, 165)
t.down()
t.right(90)
t.circle(10, 180)


# 腮红
t.color("#ffa0a0")
t.pensize(2)
t.left(100)

t.up()
t.goto(-275, 165)
t.down()
forward(8)

t.up()
t.goto(-239, 165)
t.down()
forward(8)


t.up()
t.right(180)
t.down()


# t.speed(0)
# Turtle().screen.delay(0)

# 爱心1
t.up()
t.goto(-150, 70)
t.down()

t.left(140)
t.begin_fill()
t.forward(51 * 0.20)
for i in range(15):
    # t.forward(0.20)
    # t.right(0.3)
    t.forward(2)
    t.right(3)

for i in range(21):
    t.forward(2)
    t.right(7.86)
t.left(120)
for i in range(21):
    t.forward(2)
    t.right(7.86)
for i in range(15):
    t.forward(2)
    t.right(3)
forward(51 * 0.20)
t.end_fill()
t.up()
t.goto(-157, 78)
t.down()
t.pencolor("red")
t.write("5", font=("Arial", "22"))

## 爱心2
t.color("#ffa0a0")
t.up()
t.goto(-75, 65)
t.down()

t.left(297)
t.begin_fill()
t.forward(51 * 0.24)
for i in range(15):
    t.forward(2.4)
    t.right(3)

for i in range(21):
    t.forward(2.4)
    t.right(8)
t.left(130)
for i in range(21):
    t.forward(2.4)
    t.right(8)
for i in range(15):
    t.forward(2.4)
    t.right(3)
t.forward(51 * 0.24)
t.end_fill()

t.up()
t.goto(-80, 80)
t.down()
t.pencolor("red")
t.write("2", font=("Arial", "22"))

## 爱心3
t.color("#ffa0a0")
t.up()
t.goto(10, 60)
t.down()

t.left(300)
t.begin_fill()
t.forward(51 * 0.28)
for i in range(15):
    t.forward(2.8)
    t.right(3)

for i in range(21):
    t.forward(2.8)
    t.right(8.30)
t.left(140)
for i in range(21):
    t.forward(2.8)
    t.right(8.30)
for i in range(15):
    t.forward(2.8)
    t.right(3)
t.forward(51 * 0.28)
t.end_fill()

t.up()
t.goto(-0, 80)
t.down()
t.pencolor("red")
t.write("0", font=("Arial", "22"))
t.down()

## 把笔头移走
t.up()
t.goto(0, 0)
t.down()


# 写给谁
t.up()
t.goto(200, 0)
t.down()
t.write("    by: Boris", font=("隶书", 20))

t.done()
