function cos_se = cos_se( A )
%% cos��x)= 1 - x^2/2! + x^4/4! ʹ��̩�ռ�������cos����
x = (A/180)*pi;%������ĽǶ�ת��Ϊ����
 
%%
symbol=1;
sum=0;
my_eps=10^-8;
temp_sum=1;
power=0;
while abs(temp_sum)>my_eps
    sum=sum+temp_sum;
    symbol=-symbol;
    power=power+2;
    temp_sum=symbol*x^power/factorial(power);
    
end
cos_se = sum;
end

