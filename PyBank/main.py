import os
import csv

file = "/Users/hyunsookim/Documents/bootcamp/Practice/homework-instructions/03_Python/python-challenge/PyBank/Resources/budget_data.csv"

with open (file,'r') as csv_file:
    budget_data = csv.reader(csv_file, delimiter=',')
    csv_header = next(budget_data)

    total_month = 0
    total = 0
    profit_list = []
    profit_change_list = []

    for row in budget_data:
        total_month = total_month + 1
        total = total + int(row[1])
        profit_list.append(row[1])

        
    print(total_month)
    print(total)
    print(profit_list)

    

    int_profit_list=[int (i) for i in profit_list]
    print(int_profit_list)
    
    for j in range(len(int_profit_list) -1) :
        profit_change = int_profit_list[j+1] - int_profit_list[j] 
        profit_change_list.append(profit_change)
    
    
    print (profit_change_list)
    len_change_list = len(profit_change_list)
    change_sum = sum(profit_change_list)
    average_change = change_sum / len_change_list
    print(average_change)
