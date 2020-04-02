%% cos£¨x)= 1 - x^2/2! + x^4/4! 
 
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