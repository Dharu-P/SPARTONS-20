n = int(input())
for t in range(n):
	a, b = map(int, input().split(' '))
	a = int(str(a)[::-1])
	b = int(str(b)[::-1])
	s = 0
	result = 0
	s = a + b
	result = int(str(s)[::-1])
	print(result)