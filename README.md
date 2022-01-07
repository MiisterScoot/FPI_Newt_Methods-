# FPI.py explanation: FPI runs fixed point iteration algorithm. Pictures have examples. 
There are two outcomes: One, after some number of steps from a starting point, the function converges to a stable fixed point. Two, the starting point doesn't lead to convergence, and as a result creates a pattern best defined as chaotic. 
The example here is done with the function f(x) = ax*(1-x), where a is a user entered coefficient. This function has fixed points has at x = 0 and x = 1 - 1/a 
To prove, fixed point exits when ax*(1-x)- x = 0, rearranging gives a*(1-x)=1, so 1 - x = 1/a and x = 1-1/a
To add your own function, replace the return statement in h(a, x) with whatever you want the new function to be. 

# Newt.py performs Newton's method, an algorithm for finding the zeroes of a function
Here's the wikipedia page if you're curious for more on the algorithm: https://en.wikipedia.org/wiki/Newton%27s_method

The code utilizes this to find the nth root of any positive real number, where n is a natural number. The graph just shows how it converges to the actual value. A nice application is using Newton's method to approximate the value of irrational numbers. For example, if I want to find the square root of 2, I can pick a function, g(x) = x<sup>2</sup> - 2. This function has roots at positive square root of 2 and negative square root of 2. Picking the right starting value, we can then get closer to a root and arrive at an approximation for the value of the square root of 2. 
