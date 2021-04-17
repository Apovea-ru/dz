#1 подзадача
cubic_odd_number=[]
number=1
sum=0
sum_odd_numbers=0

while number<1001:
    cubic_number=number**3
    cubic_odd_number.append(cubic_number)
    number=number+2
print(cubic_odd_number)

for each_number in cubic_odd_number:
    each_number_str=str(each_number)
    for number in each_number_str:
        sum=sum+int(number)
    number_by_seven=sum%7
    sum=0
    if number_by_seven==0:
        sum_odd_numbers=sum_odd_numbers+each_number

print(sum_odd_numbers)

#2 подзадача
i=0
number=1
sum=0
sum_odd_numbers=0

for each_number_first in cubic_odd_number:
    cubic_odd_number[i]=each_number_first+17
    i+=1
print(cubic_odd_number)

for each_number_second in cubic_odd_number:
    each_number_str_second=str(each_number_second)
    for number in each_number_str_second:
        sum=sum+int(number)
    number_by_seven=sum%7
    sum=0
    if number_by_seven==0:
        sum_odd_numbers=sum_odd_numbers+each_number_second

print(sum_odd_numbers)
