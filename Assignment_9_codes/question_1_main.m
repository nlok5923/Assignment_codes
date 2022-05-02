Q_function= zeros(1,2); 
N= zeros(1,2);
Rn= zeros(1,1000);
itr =zeros(1,1000);

% Q_function

epsilon=0.1;
sum=0;
alpha=0.2;

for iter = 1:1000
    itr(iter)=iter;
    if rand > epsilon
        [m,id]= max(Q_function);
        A= id;
    else
        temp= randperm(2); 
        A= temp(1);
    end
    % R = binaryBanditB(A)
    % R = binaryBanditA(A)
    N(A)= N(A)+1;
    Q_function(A)= Q_function(A)+ (1 / N(A)) * (R - Q_function(A));
    sum = sum + R;
    Rn(iter) = sum / N(A);
end
plot(itr,Rn);
title('Average rewards vs no of iteration graph for binaryBanditA')
ylabel('average rewards')
xlabel('no of iterations')
