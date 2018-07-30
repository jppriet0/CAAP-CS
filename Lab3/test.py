a = [1,2,3]

b = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
	res = [a[x]*b[i][x] for x in range(3)]
	print(sum(res))

input("exit")