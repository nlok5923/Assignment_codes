function [val] = binaryBanditB(action)

probability = [.8 .9];
if rand < probability(action)
	val = 1;
else
	val = 0;
end
end
