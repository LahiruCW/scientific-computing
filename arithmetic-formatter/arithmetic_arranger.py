#import regular expression module.
import re

def arithmetic_arranger(problems, solve=False):
  #Checking Problem length.
  if (len(problems)>5):
    return "Error: Too many problems."
  
  first_line = ""
  second_line = ""
  dashes = ""
  sum_line = ""
  final = ""
  SYMBOLS = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

  for problem in problems:
    #Checking operator and digits.
    if(re.search("[^\s0-9.+-]", problem)):
      if SYMBOLS.search(problem) != None:
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    container = problem.split(" ")

    firstNumber = container[0]
    operator = container[1]
    secondNumber = container[2]

    #Checking Maximum number of digits.
    if(len(firstNumber)>=5 or len(secondNumber)>=5):
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    #Solution.
    if(operator == "+"):
      sum = str(int(firstNumber) + int(secondNumber))
    elif(operator == "-"):
      sum = str(int(firstNumber) - int(secondNumber))

    #Dashes length according to documents.
    length = max(len(firstNumber), len(secondNumber)) + 2
    top_line = str(firstNumber).rjust(length)
    bottom_line = operator + str(secondNumber).rjust(length-1)
    line = "-"*(length)
    res = str(sum).rjust(length)

    seperation = "    "
    
    #Last Problem doesn't need spaces. this part will skip the spaces for last problem.
    if problem != problems[-1]:
      first_line += top_line + seperation
      second_line += bottom_line + seperation
      dashes += line + seperation
      sum_line += res + seperation
    else:
      first_line += top_line
      second_line += bottom_line
      dashes += line
      sum_line += res

  if solve:
    final = first_line+'\n'+second_line+'\n'+dashes+'\n'+sum_line
  else:
    final = first_line+'\n'+second_line+'\n'+dashes
  return final