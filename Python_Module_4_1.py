
# coding: utf-8

# In[29]:


class GeometricShape:
    def __init__(self, name, num_sides):
        self.__name = name
        self.__num_sides = num_sides
        
    def __str__(self):
        return "The shape is %s and the number of sides is %d." %(self.__name, self.__num_sides)
           
    def input_side_length(self):
        sides = []
        for i in range(0,self.__num_sides):
            sides.append(input("Please enter length of side number %d: " %(i+1)))
        return sides
    
class Triangle(GeometricShape):
    def __init__(self, *args, **args2):
        super(Triangle, self).__init__(*args, **args2)
        self.__side1 = 0
        self.__side2 = 0
        self.__side3 = 0
        
    def calculate_area(self):
        side_lengths = super(Triangle, self).input_side_length()
        perimeter = (int(side_lengths[0]) + int(side_lengths[1]) + int(side_lengths[2])) / 2
        area = (perimeter*(perimeter-int(side_lengths[0]))*(perimeter-int(side_lengths[1]))*(perimeter-int(side_lengths[2]))) ** 0.5
        print("The calculated area of the triangle is: %3.4f" %area)
        
T = Triangle("Triangle", 3)        
T.calculate_area()
        
    
    

