# se2020
This project is created for the software engineering's classwork .

Language：python、matlab
Interface
界面模块使用tkinter构建通过0-9数字button进行角度输入，sin、cos等进行运算选择，最下方radiobutton进行python和matlab三角函数function实时切换
![界面图](https://github.com/se20201/se2020/blob/master/Interface.png)
代码
（1）se_cos.m、se_sin.m、triangle.m使用matlab语言实现cos、sin、tan和cot函数。
（2）Interface.py主要实现了三角函数运算人机交互界面显示，通过python语言实现cos、cot、sin和tan函数，配合matlab for python engine 实现混合matlab python编程。


三角函数计算
首先实现sin和cos,入口参数为角度，先转弧度再进行泰勒展开式迭代运算，如果追求高精度可以提高迭代次数
