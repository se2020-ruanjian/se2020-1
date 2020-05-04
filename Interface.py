from tkinter import *
import matlab
import matlab.engine
import string
from math import pi
import math
import numpy as np
import random
import tkinter.messagebox
from test_func import *
root = Tk()
eng = matlab.engine.start_matlab()
v1 = IntVar()
v1.set(1)
flag = 1
# eng.se_sin(90)

# 窗口大小,并把界面移至屏幕中心 （宽x高）
width = 300
height = 205
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)

#root.geometry("300x205")

# 设置title
root.title("三角函数计算")

# Frame就是在屏幕上的一块矩形区域  多用来作为容器使用
frame_show = Frame(width=250, height=150, bg='#ddd')

# 添加到主窗体
frame_show.pack()

# 主窗体

# 实例化一个产生变量的类
v = StringVar()
# 初始化赋值'0'
v.set('0')
# Lable(用于存放父组件，属性参数   )
# anchor  文本相对于标签中心的位置   默认是center N S W E
show_label = Label(frame_show, textvariable=v, bg='white', width='30', height='1', anchor='e', font=("黑体", 20, "bold"))



# 添加到主窗体
show_label.pack(padx=10, pady=10)

frame_bord = Frame(width=250, height=200)
frame_bord.pack(padx=4, pady=4)


#用于测试时的文本提示框
frame_show2 = Frame(width=250, height=80)
frame_show2.pack()
l1 = Label(frame_show2,text="请输入角度",font=("黑体",10,"bold"))
l1.pack(padx=5, pady=5)
#l1.grid(row=5,column=0,columnspan=2)


calc = []
isoperate = False

#
def change(num):
    global isoperate
    if isoperate == False:
        if v.get() == "0" and num == '.':
            v.set(length(v.get() + num))
        elif v.get() == "0":
            v.set(length(num))
        else:
            if num == ".":
                if v.get().count(".") < 1:
                    v.set(v.get() + num)
            else:
                v.set(v.get() + num)
    else:
        v.set(length(num))
        isoperate = False
#
#
# # 检验字符串的长度的函数
def length(str):
    if len(str) > 12:
        return str[0:12]
    else:
        return str

#
# # 清空函数
def clear():
    global calc
    calc = []
    # 屏幕窗口恢复到0
    v.set("0")


#
# # 操作 +  -  *  /
# def operate(sign):
#     global calc
#     global isoperate
#     isoperate = True
#     calc.append(v.get())
#     if sign == "+":
#         calc.append(sign)
#     elif sign == "-":
#         calc.append(sign)
#     elif sign == "*":
#         calc.append(sign)
#     elif sign == "/":
#         calc.append(sign)
#
#
# # 运算
# global calcstr
#
#
# def equal():
#     global calc
#     # 获取当前界面的值
#     calc.append(v.get())
#     print(calc)
#     # 列表变字符串 join 把列表用什么拼接成字符串
#     calcstr = "".join(calc)
#     print(calcstr)
#     print(type(calcstr))
#
#     # 运算操作 eval（）把str当成有效的表达式进行计算
#     result = eval(calcstr)
#     if len(str(result)) > 12:
#         result = str(result)
#         result = result[0:12]
#         v.set(result)
#     else:
#         v.set(result)
#
#     print(result)
#
#
# 定义退格函数
def delete():
    # 获取v.get（）长度
    num = len(v.get())
    # 如果长度>1 怎么办
    if num > 1:
        strnum = v.get()
        strnum = strnum[0:num - 1]
        v.set(strnum)
    # 小于等于1的时候
    else:
        v.set("0")

def sel():
    print(v1.get())
    # flag =

def sign(display):
    angle = float(v.get())
    while 1:
        if (angle < 360.0): break
        angle = angle - 360.0
    flag = v1.get()
    print(flag)
    if(flag == 1):
        result = eng.se_sin(angle)
        # return result
    else:
        angle = 3.14 * (angle / 180)# 化角度为弧度
        result = 0
        denominator = 1 # 分母赋初值
        numerator = angle # 分子赋初值
        i = 1
        while(abs(numerator / denominator) >=  1e-6):
            result =result +  numerator / denominator# 累加一项

            numerator =-numerator * angle * angle #求下一项的分子
            denominator =denominator * 2 * i * (2 * i + 1) # 求下一项的分母
            i = i + 1
    result = round(result,6)

        # print(result)
        # v.set(result)
    if(display==1):
        v.set(result)
    return result

def cos(display):
    angle = float(v.get())
    while 1:
        if (angle < 360.0): break
        angle = angle - 360.0
    flag = v1.get()
    print(flag)
    if(flag == 1):
        result = eng.se_cos(angle)
    else:
        x = (angle/180)*pi;
        cosTotal  = 1
        count = 2
        term = 1
        x=float(x) 
        while abs(term) > 1e-20:
            term *= (-x * x)/( count * (count-1) )   
            cosTotal += term
            count += 2
            #print("%1d  %22.17e" % (count, term))
        result = cosTotal
    result = round(result,6)
        #print(result)
    if(display==1):
        v.set(result)
    return result

def tan():
    sin_res = sign(0)
    cos_res = cos(0)
    if(cos_res == 0):
        v.set("error")
    else:
        result =  sin_res / cos_res
        result = round(result,6)
    # print(result)
    v.set(result)

def cot():
    sin_res = sign(0)
    cos_res = cos(0)
    if(sin_res == 0):
        v.set("error")
    else:
        result = cos_res / sin_res
        result = round(result, 6)
        # print(result)
        v.set(result)


def test():
    l1["text"] = "测试中，请稍等。。。"
    string1 = str("测试将随机选取1000个数对每一个三角函数进行计算平均精度\n测试需要大约10s，点击确定开始测试，请稍等一会")
    tkinter.messagebox.showinfo(title='提示', message = string1)
    score_sinm = 0
    score_cosm = 0
    score_tanm = 0
    score_cotm = 0

    score_sinp = 0
    score_cosp = 0
    score_tanp = 0
    score_cotp = 0

    for i in range(1,1001):
        x = round(random.uniform(1,3000),3)
        ##真实值
        sin_gt = math.sin(x / 180 * math.pi)
        cos_gt = math.cos(x / 180 * math.pi)
        tan_gt = math.tan(x / 180 * math.pi)
        cot_gt = (1 / (math.tan(x / 180 * math.pi)))
        
    
        #matlab计算出的值
        sin_sem = sign2(x,1)
        cos_sem = cos2(x,1)
        tan_sem = sin_sem / cos_sem
        cot_sem = cos_sem / sin_sem 
    
        #python计算出的值
        sin_sep = sign2(x,2)
        cos_sep = cos2(x,2)
        tan_sep = sin_sep / cos_sep
        cot_sep = cos_sep / sin_sep
    
        #matlab计算的误差
        score_sinm = score_sinm  + abs(sin_gt - sin_sem)
        score_cosm = score_cosm  + abs(cos_gt - cos_sem)
        score_tanm = score_tanm  + abs(tan_gt - tan_sem)
        score_cotm = score_cotm  + abs(cot_gt - cot_sem)
    
        #python计算的误差
        score_sinp = score_sinp  + abs(sin_gt - sin_sep)
        score_cosp = score_cosp  + abs(cos_gt - cos_sep)
        score_tanp = score_tanp  + abs(tan_gt - tan_sep)
        score_cotp = score_cotp  + abs(cot_gt - cot_sep)
    
    
    
    accsin_m =score_sinm / 1000
    acccos_m =score_cosm/ 1000
    acctan_m =score_tanm / 1000
    acccot_m =score_cotm / 1000

    accsin_p =score_sinp / 1000
    acccos_p =score_cosp/ 1000
    acctan_p =score_tanp / 1000
    acccot_p =score_cotp / 1000
    if (accsin_m<0.001 and acccos_m<0.001 and acctan_m<0.001 and acctan_m<0.001 and acccot_m<0.001 and accsin_p<0.001 and acccos_p<0.001 and acctan_p<0.001 and acccot_p<0.001):
        string2 = "测试通过，精度均<0.001，请使用。"
    else: string2 = "测试失败，请重新测试。"
    l1["text"] = ""
    string3 = str("测试完成:\n (要求精度<0.001)\n matlab的sin平均精度：%s\n matlab的cos平均精度：%s\n matlab的tan平均精度：%s\n matlab的cot平均精度：%s\n python的sin平均精度：%s\n python的cos平均精度：%s\n python的tan平均精度：%s\n python的cot平均精度：%s\n\n %s"
                 %(accsin_m, acccos_m, acctan_m, acccot_m, accsin_p, acccos_p, acctan_p, acccot_p, string2))
    tkinter.messagebox.showinfo(title='测试结果', message = string3)
    l1["text"] = "请输入角度"
    
# Button(父组件，属性参数)
#button_del = Button(frame_bord, text=' ', width='5', height='1').grid(row='1', column='3')
button_del = Button(frame_bord, text='←', width='5', height='1', command=lambda: delete()).grid(row='1', column='2')
button_del = Button(frame_bord, text='CE', width='5', height='1', command=lambda: clear()).grid(row='4', column='4')
button_del = Button(frame_bord, text='0', width='5', height='1', command=lambda: change("0")).grid(row='1', column='1')
button_del = Button(frame_bord, text='Sin', width='5', height='1', command=lambda: sign(1)).grid(row='1', column='3')

button_del = Button(frame_bord, text='7', width='5', height='1', command=lambda: change("7")).grid(row='2', column='0')
button_del = Button(frame_bord, text='8', width='5', height='1', command=lambda: change("8")).grid(row='2', column='1')
button_del = Button(frame_bord, text='9', width='5', height='1', command=lambda: change("9")).grid(row='2', column='2')
button_del = Button(frame_bord, text='Cos', width='5', height='1', command=lambda: cos(1)).grid(row='2', column='3')

button_del = Button(frame_bord, text='4', width='5', height='1', command=lambda: change("4")).grid(row='3', column='0')
button_del = Button(frame_bord, text='5', width='5', height='1', command=lambda: change("5")).grid(row='3', column='1')
button_del = Button(frame_bord, text='6', width='5', height='1', command=lambda: change("6")).grid(row='3', column='2')
button_del = Button(frame_bord, text='Tan', width='5', height='1', command=lambda: tan()).grid(row='3', column='3')

button_del = Button(frame_bord, text='1', width='5', height='1', command=lambda: change("1")).grid(row='4', column='0')
button_del = Button(frame_bord, text='2', width='5', height='1', command=lambda: change("2")).grid(row='4', column='1')
button_del = Button(frame_bord, text='3', width='5', height='1', command=lambda: change("3")).grid(row='4', column='2')
button_del = Button(frame_bord, text='Cot', width='5', height='1', command=lambda: cot()).grid(row='4', column='3')

button_del = Button(frame_bord, text='test', width='5', height='1', command=lambda: test()).grid(row='1', column='0')

r1 = Radiobutton(frame_bord, text="matlab", value=1, variable=v1,command=sel)
r1.grid(row=1, column=4)

r2 = Radiobutton(frame_bord, text="python", value=2, variable=v1,command=sel)
r2.grid(row=2, column=4)






root.mainloop()
