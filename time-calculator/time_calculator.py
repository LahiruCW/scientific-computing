__author__ = "LahiruCW"
__version__= 1.0
__description__ = "Time calculator is a function written to calculate time."

def add_time(start, duration, day = ""):
  new_time = ""

  #Make day parameter case insensitive
  day = day.lower()

  #Days dictionary
  daysOfWeek = ["Monday","Tuesday","Wednesday","Thursday", "Friday","Saturday", "Sunday"]

  #split the content of start
  startTime = start.replace(":"," ").split()

  #split the content of duration.
  durTime = duration.split(":")

  #Adding the values
  sumHour = int(startTime[0]) + int(durTime[0])
  sumMin = int(startTime[1]) + int(durTime[1])

  #Same time period values.
  if sumMin < 60:
    if sumHour < 12:
      if len(day) == 0:
        new_time = str(sumHour) + ":" + str(sumMin)+" "+str(startTime[2])

        if len(str(sumMin))<2:
          new_time = str(sumHour) + ":" + "0"+str(sumMin)+" "+str(startTime[2])
        
      elif len(day) > 0:
        for i in range(len(daysOfWeek)):
          a = daysOfWeek[i]
          if a.lower() == day:
            new_time = str(sumHour) + ":" + str(sumMin)+" "+str(startTime[2])+", "+a
    
    if sumHour > 12:
      i = 0
      while sumHour > 12:
        sumHour = sumHour - 12
        i = i+1
      
      numberOfDays = i/2
      restPeriod = i%2
      restDaysWeek = i%7

      if restPeriod == 1:
        if startTime[2] == "PM":
          period = "AM"
        elif startTime[2] == "AM":
          period = "PM"
      
      else:
        period = startTime[2]
    
      if numberOfDays == 1:
        if len(day) == 0:
          period = period + " (next day)"
          new_time = str(sumHour)+":"+str(sumMin)+" "+period
        
        elif len(day) > 1:
          for i in range(len(daysOfWeek)):
            a = daysOfWeek[i]
            if a.lower() == day:
              period = period + ", "+daysOfWeek[i+1]+" (next day)"
              new_time = str(sumHour)+":"+str(sumMin)+" "+period

      elif numberOfDays < 1:
        if len(day) == 0:
          if period =="AM":
            period = period + " (next day)"
            new_time = str(sumHour)+":"+str(sumMin)+" "+period
      
      else:
        if len(day) == 0:
          num = int(round(numberOfDays)) + 1
          period = period + " (" + str(num) + " days later)"
          new_time = str(sumHour)+":"+str(sumMin)+" "+period
        
        elif len(day)>0:
          if restDaysWeek == 4:
            for i in range(len(daysOfWeek)):
              b = daysOfWeek[i]
              if b.lower() == day:
                period = period + ", "+ daysOfWeek[i-1] + " (" + str(numberOfDays+1)+" days later)"
                new_time = str(sumHour)+":"+str(sumMin)+" "+period
  
  elif sumMin > 60:
    sumMin = sumMin-60
    sumHour = sumHour + 1
    
    k=0

    if sumHour > 12:
      while sumHour > 12:
        sumHour = sumHour - 12
        k = k + 1
    
    numberOfDays = k/2
    restPeriod = k%2
    restDaysWeek = k%7

    if numberOfDays == 0:
      if restPeriod ==1:
        if startTime[2] ==  "AM":
          period = "PM"
      
        if len(str(sumMin)) < 2:
          new_time = str(sumHour)+":"+"0"+str(sumMin)+" "+period
    
    if sumHour == 12:
      if startTime[2] == "AM":
        period = "PM"
      elif startTime[2] == "PM":
        period = "AM"
      
      if len(str(sumMin))<2:
        if period == "PM":
          new_time = str(sumHour)+":"+"0"+str(sumMin)+" "+period
        
        if len(day) == 0:
          if period == "AM":
            if numberOfDays == 1 or numberOfDays > 1:
              period = period + " "+"("+str(numberOfDays+1)+" days later)"
              new_time = str(sumHour)+":"+"0"+str(sumMin)+" "+period
        
        if len(day) > 0:
          if restDaysWeek == 2:
            for i in range(len(daysOfWeek)):
              c = daysOfWeek[i]
              if c.lower() == day:
                period = period +", "+daysOfWeek[i+2]+" ("+str(numberOfDays+1)+" days later)"
                new_time = str(sumHour)+":"+"0"+str(sumMin)+" "+period
    
  return new_time