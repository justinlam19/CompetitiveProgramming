from math import log

casenums = int(input())

size = 16
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

out = []
for _ in range(casenums):
	a, b = [int(x) for x in input().split()]
	out.append(int(digitsum(b) - digitsum(a - 1)))

for i in out:
	print(i)