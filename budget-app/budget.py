class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()
  
  def deposit(self, amount, description=""):
    self.amount = amount
    self.description = description

    self.dic = {}

    self.dic["amount"]=amount
    self.dic["description"]=description

    self.ledger.append(self.dic)
  
  def check_funds(self, amount):
    total_funds = 0
    
    for i in range(len(self.ledger)):
      total_funds += self.ledger[i]["amount"]
    
    if total_funds < amount:
      return False
    
    else:
      return True
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      
      self.withdraw_dic = {}

      self.amount = amount
      self.description = description

      self.withdraw_dic["amount"] = -(amount)
      self.withdraw_dic["description"] = description

      self.ledger.append(self.withdraw_dic)
      return True
    
    else:
      return False
  
  def get_balance(self):
    funds = 0
    for i in range(len(self.ledger)):
      funds += self.ledger[i]["amount"]
    
    return funds
  
  def transfer(self, amount, objname):
    object_name = objname.name
    tran = self.withdraw(amount,"Transfer to {}".format(object_name))

    depo = objname.deposit(amount, "Transfer from {}".format(self.name))

    if tran == True:
      return True
    else:
      return False
  
  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0

    for i in range(len(self.ledger)):
      items += f"{self.ledger[i]['description'][0:23]:23}" + \
            f"{self.ledger[i]['amount']:>7.2f}" + '\n'
      total += self.ledger[i]["amount"]
    
    return (title + items + "Total: " + str(total))


def create_spend_chart(categories):

  spend = []

  for category in categories:
    
    for amount in category.ledger:
      temp = 0
      
      if amount["amount"] < 0:
        temp += abs(amount["amount"])
      
    spend.append(temp)
    
  total = sum(spend)

  percentages = [amount/total*100 for amount in spend]

  title = "Percentage spent by category"

  for value in range(100,-1,-10):
    title += "\n" + str(value).rjust(3) + "|"
    
    for percentage in percentages:
      if percentage > value:
        title += " o "
      else:
        title += "   "
    
    title += " "
    
  title += "\n    ----------"

  category_length = []
  
  for category in categories:
    category_length.append(len(category.name))
  
  max_length = max(category_length)

  for value in range(max_length):
    title += "\n    "
    
    for num in range(len(categories)):
      if value < category_length[num]:
        title += " " + categories[num].name[value] + " "
      else:
        title += "   "
    title += " "

  return title