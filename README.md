# se2020
This project is created for the software engineering's classwork .

![界面图](https://github.com/se20201/se2020/blob/master/Interface.png)


Language：python、matlab


Interface
界面模块使用tkinter构建通过0-9数字button进行角度输入，sin、cos等进行运算选择，最下方radiobutton进行python和matlab三角函数function实时切换



代码
（1）se_cos.m、se_sin.m、triangle.m使用matlab语言实现cos、sin、tan和cot函数。
（2）Interface.py主要实现了三角函数运算人机交互界面显示，通过python语言实现cos、cot、sin和tan函数，配合matlab for python engine 实现混合matlab python编程。


三角函数计算
首先实现sin和cos,入口参数为角度，先转弧度再进行泰勒展开式迭代运算，如果追求高精度可以提高迭代次数


测试
为了方便，用八个计算模块的函数组成test_func.py文件，test.py文件调用该文件中的函数进行计算。测试随机生成1000个1到3000内的三位小数，三角函数计算的真实值由python自带的math包中的函数实现；最终test.py返回八个值，分别表示对于输入的1000个随机数的matlab计算三角函数值和python计算三角函数值与真实值间的平均绝对误差。
