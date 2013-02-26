A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
B = [[1,2],[3,4],[5,6]]
row_A = len(A)
col_A = len(A[0])
row_B = len(B)
col_B = len(B[0])

def matrixmult (A, B):
    C = [[0 for row in range(col_B)] for col in range(row_A)]
    for i in range(row_A):
        for j in range(col_B):
            for k in range(row_B):
                C[i][j] += A[i][k]*B[k][j]
    return C

if col_A != row_B:
	print "cant multiply to matrices"
	exit()
else:
	#to call the function multiplication of the matrices
	c = matrixmult(A,B)

for i in range(row_A):
	for j in range(col_B):
		pass	#print c[i][j]
	print c[i]

