# Question-5:
# from pkg.poly import Poly 
# a = Poly(1,2,3)  #an, ...., a0 
# b = Poly(1,0,1,1,2,3)
# c = a+b 
# print(c) #Poly ( 1,0,1, 2,4,6)

class Poly:
    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)
        
    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        result = [0] * max_len
        for i in range(len(self.coeffs)):
            result[i] += self.coeffs[i]
        for i in range(len(other.coeffs)):
            result[i] += other.coeffs[i]
        return Poly(*result)
    
    def __repr__(self):
        return "Poly(" + ", ".join(map(str, self.coeffs)) + ")"

a = Poly(1, 2, 3) 
b = Poly(1, 0, 1, 1, 2, 3)
c = a + b 
print(c)

