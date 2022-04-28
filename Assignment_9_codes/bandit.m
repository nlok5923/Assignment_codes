function [reward] = bandit(action)
mean_reward = [.1 .2 .25 .3 .35 .4 .5 .7 .45 .55];
reward = mean_reward(action) + randn;
end