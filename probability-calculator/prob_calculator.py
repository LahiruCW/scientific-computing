import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    """
    convert the **balls arguments to a instance variable looks like this.
    {"red":2, "blue":1} -> ["red","red","blue"]
    """
    self.contents = []
    for key, value in balls.items():
      while value > 0:
        self.contents.append(key)
        value = value - 1
    
  def draw(self, num_balls):
    """
    remove balls at random from 'contents'
    param: num_balls
    return: removed balls as a list of string.
    """
    
    #if the number of balls to draw exceeds the available quantity, return all the balls
    if num_balls > len(self.contents):
      return self.contents
    else:
      balls = []
      for i in range(num_balls):
        randomChoice = random.choice(self.contents)
        balls.append(randomChoice)
        self.contents.remove(randomChoice)    
    
    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  """
  Calculate the probability according to a given number of experiment.
  param: hat, expected_balls, num_balls_drawn, num_experiment.abs
  return: probability
  """

  expected_keys = []

  for key in expected_balls.keys():
    expected_keys.append(key)
    
  M = 0
    
  for i in range(num_experiments):

    #create a deepcopy of hat object.
    copyHat = copy.deepcopy(hat)
    balls = copyHat.draw(num_balls_drawn)
    
    #counts the elements of balls list according to the expected keys.
    counter = [balls.count(key) for key in expected_keys]
    
    expected_values = []

    for val in expected_balls.values():
      expected_values.append(val)
    
    if expected_values <= counter:
      M += 1
        
  probability = (M/num_experiments)

  return probability