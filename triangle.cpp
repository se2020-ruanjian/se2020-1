#define pi 3.141592
#include <math.h>
#pragma warning(disable:4244)

float se_cos(float angle)
{
	float  x;                                        //定义弧度
	x = (angle/ 180)* pi;                                 //角度转化为弧度
	float  result = 0;                                //结果
	float  numerator = 1;                                //泰勒展开式的分子
	float  denominator = 1;                             //泰勒展开式的分母
	int    s = 1;


	float  temp_result = 1;          //展开项
	float  my_eps = 1 / 100000000;
	float n, m;
	n = 0;
	m = 1;
	while (fabs(temp_result) > my_eps)
	{
		result += temp_result;
		s = -s;
		n = n + 2;
		m = 1;
		for (int i = n; i > 1; i--)                        //计算n的阶乘
		{
			m = m*i;
		}
		numerator = pow(x, n);                                //分子等于x的n次方
		denominator = m;                             //分母等于n的阶乘
		temp_result = s* numerator / denominator;
	}
	if (fmodf(angle, 90) == 0)
		result = round(result);
	else 
		result = (int)(1000.0*result + 0.5) / 1000.0;
	return  result;
}

float se_sin(float angle)
{	
	float	result;				        //结果
	float	numerator;				   //泰勒展开项的分子
	float	denominator;			  //泰勒展开项的分母
	int	s;							 //泰勒展开的正负因子

	angle = pi * (angle / 180);		//化角度为弧度

	result = 0;  
	s = 1;							   //正负因子赋初值
	denominator = 1;				  //分母赋初值
	numerator = angle;				 //分子赋初值
	
	for (int i = 1; numerator / denominator >= 1e-6; i++)
	{
		result +=  s * numerator / denominator;			   //累加一项

		numerator *=  angle * angle;					 //求下一项的分子
		denominator *=  2 * i * (2 * i + 1);		    //求下一项的分母
		s *= -1;
	}

	return result;
}

float se_tan(float angle)
{	
	float	result;	
	result=se_sin(angle)/se_cos(angle);
	return result;
}

float se_cot(float angle)
{	
	float	result;	
	result=se_cos(angle)/se_tan(angle);
	return result;
}