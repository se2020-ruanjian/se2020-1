# se2020
This project is created for the software engineering's classwork . (version：2.0)   
1.介绍
-------
![界面图](https://github.com/se2020-ruanjian/se2020-1/blob/master/Interface.png)
![界面图](https://github.com/se2020-ruanjian/se2020-1/blob/master/Interface2.0.png)  
左图为1.0版本，右图为修改的2.0版本，加入了test按钮，并重新对按钮布局使其更美观，同时在最下方加入了文字引导。

Language：python、matlab  

Interface  
界面模块使用tkinter构建通过0-9数字button进行角度输入，sin、cos、tan、cot等进行运算选择，右边的两个按钮radiobutton进行python和matlab三角函数function实时切换，右下方的CE按钮实现计算器初始化功能。test按钮是2.0中新增按钮，实现对计算器进行检测。

代码  
（1）se_cos.m、se_sin.m使用matlab语言实现cos、sin、tan和cot函数。  
（2）Interface.py主要实现了三角函数运算人机交互界面显示，通过python语言实现cos、cot、sin和tan函数，配合matlab for python engine 实现混合matlab python编程。  

三角函数计算  
首先实现sin和cos,入口参数为角度，先转弧度再进行泰勒展开式迭代运算，如果追求高精度可以提高迭代次数  

测试  
为了方便，用八个计算模块的函数组成test_func.py文件，test.py文件调用该文件中的函数进行计算。测试随机生成1000个1到3000内的三位小数，三角函数计算的真实值由python自带的math包中的函数实现；最终test.py返回八个值，分别表示对于输入的1000个随机数的matlab计算三角函数值和python计算三角函数值与真实值间的平均绝对误差。

2.文件说明
--------
  Interface.py为主程序，实现界面编写，python算法编写，调用matlab模块功能。    
  m文件为matlab函数功能实现，tan和cot的matlab算法采用sin和cos相除得到。   
  test.py和test_func.py是单独对函数模块进行测试的文件。   
  测试记录和说明文档是本次项目的一些说明文件和记录文件。   
  
3.软件安装
--------
  请下载本工程的所有文件，运行前请安装python和matlab，使用时运行Interface.py文件即可。
  
4.新增测试按钮
--------
点击test按钮时，程序首先会弹出说明框如下图：  
![界面图](https://github.com/se2020-ruanjian/se2020-1/blob/master/test1.png)  
点击确定后开始测试，测试完成后会显示各个模块测试精度，如下图所示:   
![界面图](https://github.com/se2020-ruanjian/se2020-1/blob/master/test2.png)

