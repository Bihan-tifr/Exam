import numpy as np
A=np.array([[2,1],[1,0],[0,1]])
print("The Matrix:\n{}".format(A))
print("Singular value decomposition:")
u,s,v=(np.linalg.svd(A))
print("u:\n{}".format(u))
print("s:\n{}".format(s))
print("v:\n{}".format(v))


input("press any key to evaluate svd of second matrix")

B=np.array([[1,1,0],[1,0,1],[0,1,1]])
print("The Matrix:\n{}".format(B))
print("Singular value decomposition")
u,s,v=(np.linalg.svd(B))
print("u:\n{}".format(u))
print("s:\n{}".format(s))
print("v:\n{}".format(v))

