expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
print(expected)

lst = []
str1 = "3"
str2 = "855"
str3 = "+"

width = max(len(str1), len(str2)) + 2

str_1 = str1.rjust(width)
str_2 = str3 + str2.rjust(width-1)

hello = (str_1 + '\n' + str_2 + '\n' + "-"*(width) + '\n')
print(hello)

str4 = "3801"
str5 = "2"
str6 = "-"

width1 = max(len(str4), len(str5)) + 2

str_3 = str4.rjust(width1)
str_4 = str6 + str5.rjust(width1-1)

hello1 = (str_3 + '\n' + str_4 + '\n' + "-"*(width1) + '\n')
print(hello1)

str7 = "45"
str8 = "43"
str9 = "+"

width2 = max(len(str7), len(str8)) + 2

str_5 = str7.rjust(width2)
str_6 = str9 + str8.rjust(width2-1)

hello2 = (str_5 + '\n' + str_6 + '\n' + "-"*(width2))
print(hello2)

lst.append(hello)
lst.append(hello1)
lst.append(hello2)
print lst
print ''.join(lst)