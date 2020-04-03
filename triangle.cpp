#define pi 3.141592
#include <math.h>
#pragma warning(disable:4244)

float se_cos(float angle)
{
	float  x;                                        //���廡��
	x = (angle/ 180)* pi;                                 //�Ƕ�ת��Ϊ����
	float  result = 0;                                //���
	float  numerator = 1;                                //̩��չ��ʽ�ķ���
	float  denominator = 1;                             //̩��չ��ʽ�ķ�ĸ
	int    s = 1;


	float  temp_result = 1;          //չ����
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
		for (int i = n; i > 1; i--)                        //����n�Ľ׳�
		{
			m = m*i;
		}
		numerator = pow(x, n);                                //���ӵ���x��n�η�
		denominator = m;                             //��ĸ����n�Ľ׳�
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
	float	result;				        //���
	float	numerator;				   //̩��չ����ķ���
	float	denominator;			  //̩��չ����ķ�ĸ
	int	s;							 //̩��չ������������

	angle = pi * (angle / 180);		//���Ƕ�Ϊ����

	result = 0;  
	s = 1;							   //�������Ӹ���ֵ
	denominator = 1;				  //��ĸ����ֵ
	numerator = angle;				 //���Ӹ���ֵ
	
	for (int i = 1; numerator / denominator >= 1e-6; i++)
	{
		result +=  s * numerator / denominator;			   //�ۼ�һ��

		numerator *=  angle * angle;					 //����һ��ķ���
		denominator *=  2 * i * (2 * i + 1);		    //����һ��ķ�ĸ
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