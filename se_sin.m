function result=se_sin(angle)
%����̩��չ����Ƕȵ�sinֵ
%angleΪ����ĽǶ�
%resultΪ�ýǶȶ�Ӧ������ֵ

	angle = 3.141592 * (angle / 180);		%���Ƕ�Ϊ����
    
	result = 0;  
	s = 1;							   %�������Ӹ���ֵ
	denominator = 1;				  %��ĸ����ֵ
	numerator = angle;				 %���Ӹ���ֵ
    
	i=1;
while numerator / denominator >= 1e-6
    result = result + s * numerator / denominator;			   %�ۼ�һ��

	numerator = numerator* angle * angle;					%����һ��ķ���
	denominator = denominator * 2 * i * (2 * i + 1);		    %����һ��ķ�ĸ
	s =s * -1;
    i = i + 1;
end
end