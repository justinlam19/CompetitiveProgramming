# For a pair of integers a and b, the digit sum of the interval 
# [a,b] is defined as the sum of all digits occurring in all 
# numbers between (and including) a and b. 
# For example, the digit sum of [28,31] can be calculated as:

# 2+8+2+9+3+0+3+1=28
# Given the numbers a and b, calculate the digit sum of [a,b].

from math import log

casenums = int(input())

size = 15
dp = [0] * (size + 1)
for i in range(1, size + 1):
	dp[i] = dp[i - 1] * 10 + 45 * (10 ** (i - 1))

def digitsum(n):
	if n < 10:
		return n * (n + 1) / 2
		
	size = int(log(n, 10))
	pwr_ten = 10 ** size
	msd = n // pwr_ten
	remainder = n % pwr_ten
	
	return msd * dp[size] + pwr_ten * (msd - 1) * msd / 2 + msd * (remainder + 1) + digitsum(remainder)

for _ in range(casenums):
	a, b = [int(x) for x in input().split()]
	print(int(digitsum(b) - digitsum(a - 1)))
