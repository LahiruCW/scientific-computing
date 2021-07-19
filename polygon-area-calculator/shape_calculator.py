class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __str__(self):
    if type(self).__name__ == "Square":
      return "Square(side={side})".format(side=self.width)
    else:
      return "Rectangle(width={width}, height={height})".format(width=self.width, height=self.height)
  
  # Setter Method for width
  def set_width(self,width):
    self.width = width
  
  # Setter Method for height
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    """
    Returns area of the Rectangle.
    area = width * height
    """

    self.area = (self.width)*(self.height)
    return self.area
  
  def get_perimeter(self):
    """
    Returns perimeter of the Rectangle.
    perimeter = 2 * width + 2 * height
    """
    sideOne = 2 * (self.width)
    sideTwo = 2 * (self.height)
    perimeter = sideOne + sideTwo
    return perimeter
  
  def get_diagonal(self):
    """
    Returns the diagonal of the Rectangle.
    diagonal = (width ** 2 + height ** 2) ** 0.5
    """
    wi = (self.width)**2
    hi = (self.height)**2
    diagonal = (wi+hi)**0.5
    return diagonal
  
  def get_picture(self):
    """
    Returns a string that represents the shape of the rectangle. width = number of "*" in each line, height = number of lines.
    """

    # if the width or height is larger than 50 this will return "Too big for picture."
    if (self.width > 50) or (self.height > 50):
      return "Too big for picture."

    else:
      self.picture = ""
      self.top= "*"*(self.width)
      for i in range(self.height):
        self.picture = self.picture + self.top + '\n'
      
      return self.picture
  
  def get_amount_inside(self, new):
    """
    Takes another argument(square or rectangle) and returns the number of times the passed in shape could fit inside the shape with no rotation.

    number = first rec.area // second rec.area
    """
    num = (self.get_area() // new.get_area())
    return num

class Square(Rectangle):

  #Pass the side length
  def __init__(self,length):
    """
    store the side length in both the width and height attributes from the rectangle class.
    """
    super().__init__(length, length)
  
  #Setter Method for length
  def set_side(self, length):
    super().set_width(length)
    super().set_height(length) 
  
  #Setter method for width
  def set_width(self, width):
    super().set_width(width)
    super().set_height(width)
  
  #Setter method for height
  def set_height(self, height):
    super().set_height(height)
    super().set_width(height)
