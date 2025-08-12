class Vector:
    def __init__(self, l):
        self.l = l

    
    def __len__(self):
        return len(self.l)
    
v1 = Vector([3, 4])
v2 = Vector([1, 2])  

print(len(v1))
#print(v1 + v2)  # Vector(4, 6)
#print(v1 - v2)  # Vector(2, 2)      
#print(v1 * 2)   # Vector(6, 8)
#print(v1 / 2)   # Vector(1.5, 2.0  