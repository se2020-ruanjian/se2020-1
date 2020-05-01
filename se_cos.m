function se_cos = se_cos( A )
%% cos（x)= 1 - x^2/2! + x^4/4! 使用泰勒级数计算cos函数
x = (A/180)*pi;%把输入的角度转换为弧度
 
%%
symbol=1;
sum=0;
my_eps=1e-10;
temp_sum=1;
power=0;
while abs(temp_sum)>my_eps
    sum=sum+temp_sum;
    symbol=-symbol;
    power=power+2;
    temp_sum=symbol*x^power/factorial(power);
    
end
se_cos = sum;
end

