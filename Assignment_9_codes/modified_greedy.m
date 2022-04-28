Q_function = zeros(1,10);
N = zeros(1,10);
Rn = zeros(1,1000);
Rn1 = zeros(1,1000);
iterate = zeros(1,1000);

epsilon=0.1;
sum=0;

alpha=0.2;
temp_sum=0; 

for idx_1= 1:1000
    Rn = zeros(1,1000);
    sum = 0;
    for idx_2= 1:1000
        iterate(idx_2)=idx_2;
        if rand > epsilon
            [m,id] = max(Q_function);
            A= id;
        else
            temp = randperm(10);
            A = temp(1);
        end
        R = bandit_non_stationary(A);
        N(A) = N(A)+1;
        Q_function(A)= Q_function(A)+ (R-Q_function(A))*alpha;
        sum = sum + R;
        Rn(idx_2)= sum/idx_2;       
    end
    temp_sum = temp_sum + Rn(idx_1);
    Rn1(idx_1) = temp_sum/idx_1;
end    

plot(iterate,Rn1);