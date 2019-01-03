#python 2.7 program calculate the inverse of the entered NxN square matrix
import copy

def Get_List(n):
	m,s=[],[]
	for i in range(n):
		print "Row : "+str(i+1)
		for j in range(n):
			a=input("Enter the element : ")
			s.append(a)
		m.append(s)
		s=[]
	return m

def rec_det(matrix):
        cnt=len(matrix)
        if cnt==2 :
                prod=(matrix[0][0]*matrix[1][1])-(matrix[1][0]*matrix[0][1])
                return prod
        prod,sign=0,1
        for i in range(cnt):
                sub_matrix=copy.deepcopy(matrix)
                for j in range(cnt):
                        sub_matrix[j].pop(i)
                sub_matrix.pop(0)
                prod+=(matrix[0][i]*sign*rec_det(sub_matrix))
                sign=sign*(-1)
        return prod

def sub_matrix(Matrix,i,j):
        sm=copy.deepcopy(Matrix)
        n=len(Matrix)
        for k in range(n):
                sm[k].pop(j)
        sm.pop(i)
        return sm

def determinant(Matrix):
        D=rec_det(Matrix)
        return D

def Co_Factors(Matrix):
        A=[]
        cnt=len(Matrix)
        if cnt==2:
                A=[[],[]]
                A[0].append(Matrix[1][1])
                A[0].append((-1*Matrix[1][0]))
                A[1].append((-1*Matrix[0][1]))
                A[1].append(Matrix[0][0])
                return A
        for i in range(cnt):
                C=[]
                for j in range(cnt):
                        submatrix=sub_matrix(Matrix,i,j)
                        term=determinant(submatrix)
                        term=term*((-1)**(i+j))
                        C.append(term)
                A.append(C)
        return A

def Transpose(Matrix):
        m=len(Matrix)
        transpose=copy.deepcopy(Matrix)
        for i in range(m):
                for j in range(i+1,m):
                        transpose[i][j],transpose[j][i]=transpose[j][i],transpose[i][j]
        return transpose

def Inverse(Matrix):
        Cofactor=Co_Factors(Matrix)
        Inverse=[]
        Adjoint=Transpose(Cofactor)
        Z_value=determinant(Matrix)
        if Z_value==0:
                return ["NULL"]
        cnt=len(Matrix)
        if Z_value==1:
                return Adjoint
        for i in range(cnt):
                C=[]
                for j in range(cnt):
                        term=str(Adjoint[i][j])+" / "+str(Z_value)
                        C.append(term)
                Inverse.append(C)
        return Inverse

A=[]
m=input("Enter order of the matrix : ")
A=Get_List(m)
print "Entered matrix : ",A
B=Inverse(A)
if B[0]!="NULL":
        print "Inverse of Matrix : ",B
else:
	print "Matrix is not invertible as it is singular .i.e. determinant is zero!!!"
raw_input("Press enter to continue !!! ")
