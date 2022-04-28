function [reward] = bandit_non_stationary(action)
mean_reward = [.1 .1 .1 .1 .1 .1 .1 .1 .1 .1];
reward = mean_reward(action)+ 0.01.*randn(); 
end