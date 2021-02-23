#open sample data and calculate sum of integers
#sample data: regex_sum_42.txt total 445833
#actual data: regex_sum_992877.txt total 377149
import re
name = input("Enter file:")

file = open(name)
total = 0
#extract numbers
for num in file:
    n = re.findall('[0-9]+', num)
#view as individual strings, convert to integer and sum
    for count in n:
        if (type(count) == str):
            total = total + int(count)

print(total)
