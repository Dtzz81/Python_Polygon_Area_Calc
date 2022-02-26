class Rectangle():
    
    def __init__(self, width, height):
        self.height = height
        self.width = width 
        self.area = True
        self.diagonal = True
        self.perimeter = True
        
  #set_width, set_height, get_area: Returns area (width * height)      
    
    def set_width(self, width):
        self.width = width
        
    def get_width(self):
        return self.width
    
    def set_height(self,height):
        self.height = height
    
    def get_height(self):
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    #get_perimeter: Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    #get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

 
    #get_picture: Returns a string that represents the shape using lines of "*". 
    #The number of lines should be equal to the height width.
    #There should be a new line (\n) at the end of each line. 
    #If the width or height is larger than 50, 
    #this should return the string: "Too big for picture.".
    
             
    def get_picture(self):
        
        if self.width > 50 or self.height > 50:
            return ("Too big for picture.")
        else:
            picture = ""
      #found on google python print pattern 
            for i in range(0, self.height):
                for k in range(0, self.width):
                    picture = picture + "*"
                picture = picture + "\n"
        return picture
            
    #Takes another shape (square or rectangle) as an argument.
    # Returns the number of times the passed in shape could fit 
    #inside the shape (with no rotations). 

    def get_amount_inside(self, rectangle):
        a = self.height//rectangle.height
        b = self.width//rectangle.width 
        c = a * b
        return c
        #from net:
        #poly = getPolygon() // get the input polygon
        #a = rectangle.height // size of rectangle we are trying to fit
        #b = rectangle.width  // size of rectangle
        #//: divide with integral result (discard remainder)
        
#Additionally, if an instance of a Rectangle is represented
#as a string, it should look like: 
#Rectangle(width=5, height=10)
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

#the Square class should be a subclass of Rectangle. 
class Square(Rectangle):

    
    def __init__(self, side):
        super().__init__(side, side)
       
    
    #also contain a set_side method.      
    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)
        
    def get_side(self):
        return self.height 
        
    def __str__(self):
        return f'Square(side={self.width})'
        

   
