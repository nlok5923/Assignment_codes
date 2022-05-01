Q_function= zeros(1,10); 
N = zeros(1,10);
Rn = zeros(1,1000);
iterate = zeros(1,1000);

epsilon=0.1;
sum = 0;

for idx = 1:1000
    iterate(idx) = idx;
    if rand > epsilon
        [m , id] = max(Q_function);
        A = id;
    else
        temp = randperm(10); 
        A = temp(1);
    end
    R = bandit_non_stationary(A);
    N(A) = N(A) + 1;
    Q_function(A) = Q_function(A) + (1 / N(A)) * (R - Q_function(A));
    sum = sum + R;
    Rn(idx) = sum/idx;
end

plot(iterate,Rn);