class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"({self.x}i + {self.y}j)"
    
v1 = Vector(3, 4)
v2 = Vector(1, 2)       
print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(2, 2)      
print(v1 * 2)   # Vector(6, 8)
print(v1 / 2)   # Vector(1.5, 2.0  