class Coordinate():
    def __init__(self,x_value,y_value):
        self.x_value = float(x_value)
        self.y_value = float(y_value)
    def Distance(self,other):
        x = (self.x_value - other.x_value)**2
        y = (self.y_value - other.y_value)**2
        return x + y
    
cityA = Coordinate(input("Give me cityA's x coordinate "),input("Give me cityA's y coordinate "))
cityB = Coordinate(input("Give me cityB's x coordinate "),input("Give me cityB's y coordinate "))

print("The distance between those cities is " + str(Coordinate.Distance(cityA,cityB)))