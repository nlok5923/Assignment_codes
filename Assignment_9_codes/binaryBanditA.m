function [val] = binaryBanditA(action)

probability = [.1 .2];
if rand < probability(action)
	val = 1;
else
	val = 0;
end
end