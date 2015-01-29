from matrix import Matrix

M = Matrix(2,3)

def print_matrix(M):
    for row in range(M.numRows()):
        for col in range(M.numCols()):
            print M[row,col],
        print ""

print_matrix(M)
print "numRows = ",M.numRows()
print "numCols = ",M.numCols()
M_2_3 = M
print "M_2_3"
print_matrix(M_2_3)
M_2_3.clear(1)
print "M_2_3"
print_matrix(M_2_3)

print "M*2"
M.scaleBy(2)
print_matrix(M)

for row in range(M.numRows()):
        for col in range(M.numCols()):
            M[row,col] = row + col
print_matrix(M)
newMatrix = M.transpose()
print_matrix(newMatrix)

M1 = newMatrix
M2 = newMatrix
print "M1"
print_matrix(newMatrix)
print "M2"
print_matrix(newMatrix)
print "M1+M2"
M3 = M1 + M2
print_matrix(M3)
print "M1-M2"
M3 = M1 - M2
print_matrix(M3)
print "-----M_2_3*M2----"
print "M_2_3"
print_matrix(M_2_3)
print "M2"
print_matrix(M2)
M3 = M_2_3 * M2
print "M_2_3*M2"
print_matrix(M3)



