Problem
=======
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

Solution
--------
+ Multiply up the LCM's!  Pseudo:

	def f():
		var hold = 2
		for num in 3..20
		   hold=lcm(hold,num) 
		return hold
