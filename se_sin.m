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