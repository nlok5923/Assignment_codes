// Q_function= zeros(1,10); 
// N = zeros(1,10);
// Rn = zeros(1,1000);
// iterate = zeros(1,1000);

// alpha = 0.2;
// epsilon=0.1;
// sum = 0;

// for idx = 1:1000
//     iterate(idx) = idx;
//     if rand > epsilon
//         [m , id] = max(Q_function);
//         A = id;
//     else
//         temp = randperm(10); 
//         A = temp(1);
//     end
//     R = bandit_non_stationary(A);
//     N(A) = N(A) + 1;
//     Q_function(A) = Q_function(A) + alpha * (R - Q_function(A));
//     sum = sum + R;
//     Rn(idx) = sum/idx;
// end

// plot(iterate,Rn);


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
    % A
    N(A)= N(A)+1;
    Q_function(A)= Q_function(A)+ alpha*(R - Q_function(A));
    sum = sum + R;
    % sum = sum / iter
    Rn(iter) = sum / iter;
end
plot(itr,Rn);
title('Average rewards vs no of iteration graph for binaryBanditA')
ylabel('average rewards')
xlabel('no of iterations')
