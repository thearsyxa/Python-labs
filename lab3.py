class Rectangle:
    rectangles_quantity = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.rectangles_quantity +=1
        
    def area(self):
        return self.width*self.height
    
    def perimetr(self):
        return 2*(self.width + self.height)
    
    def is_square(self):
        return self.width ==self.height
    
    
if __name__ == "__main__":
    rect = Rectangle(5,10)
    print("Площадь:", rect.area())           
    print("Периметр:", rect.perimetr())    
    print("Это квадрат?", rect.is_square())  
    print("Создано объектов:", Rectangle.rectangles_quantity)  

