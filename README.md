# FPI algorithm runs fixed point iteration algorithm. Finds fixed point of a function, which happens when the graph intersects with the line y = x. 
#There are two outcomes: One, after some number of steps from a starting point, the function converges to a stable fixed point. Two, the starting point doesn't lead to convergence, and as a result creates a pattern best defined as chaotic. 
#The example here is done with the function f(x) = ax(1-x), where a is a user entered coefficient. This function has fixed points has at x = 0 and x = 1 - 1/a 
#To prove, fixed point exits when ax(1-x)- x = 0, rearranging gives a(1-x)=1, so 1 - x = 1/a and x = 1-1/a
