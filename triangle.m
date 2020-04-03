function tangle=triangle
tangle.se_sin=@se_sin;
tangle.se_cos=@se_cos;
tangle.se_tan=@se_tan;
tangle.se_cot=@se_cot;
end

function result=se_sin(angle)
%利用泰勒展开求角度的sin值
%angle为输入的角度
%result为该角度对应的正弦值

	angle = 3.141592 * (angle / 180);		%化角度为弧度
    
	result = 0;  
	s = 1;							   %正负因子赋初值
	denominator = 1;				  %分母赋初值
	numerator = angle;				 %分子赋初值
    
	i=1;
while numerator / denominator >= 1e-6
    result = result + s * numerator / denominator;			   %累加一项

	numerator = numerator* angle * angle;					%求下一项的分子
	denominator = denominator * 2 * i * (2 * i + 1);		    %求下一项的分母
	s =s * -1;
    i = i + 1;
end
end
%% cos（x)= 1 - x^2/2! + x^4/4! 
 
%%
clc
 
%%
A = input('please enter the degree of angle A = ');
x = A/180*pi;
 
%%
symbol=1;
sum=0;
my_eps=10^-3;
temp_sum=1;
power=0;
while abs(temp_sum)>my_eps
    sum=sum+temp_sum;
    symbol=-symbol;
    power=power+2;
    temp_sum=symbol*x^power/factorial(power);
end
disp(['cos(' num2str(x) ') is: ' num2str(sum)]);
right=cos(x);
right = roundn(right,-3);
disp(['the right answer is: ' num2str(right)]);
function tance=se_tan(angle)
    tance=se_sin(angle)/se_cos(angle);
end
function cotce=se_cot(angle)
    cotce=se_cos(angle)/se_sin(angle);
end
 