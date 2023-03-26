import requests
import json
import csv

# unhidden api key??? in *my* code??? it's more common than you think
api_key = '?key=6894504f927ce11d26da06fe17972703'

deposits = requests.get('http://api.nessieisreal.com/enterprise/deposits' + api_key)
deposits = deposits.json()

months = {}

for i in deposits['results']:  # excluding feb of the first year because it's not a full month, so it'd skew the data
    #print(i)
    try:  # this data is fuckign aids to work with        
        year_month = i['transaction_date'].split('-')[:-1]
        wacky_date = int(year_month[0]) * 12 + int(year_month[1])  # this gon be the month number
        if wacky_date not in months:  # if the month changed
            months[wacky_date] = float(i['amount'])
            prev_date = i['transaction_date'][:-3] 
        else:  # we're adding money to this month's total
            months[wacky_date] += float(i['amount']) 
    except:
        months[wacky_date] += float(i['amount'])

#print(months)
months_list = []
for i in months.keys():
    months_list.append([i, months[i]])
months_list.sort()

# add numbers to csv
f = open('month_deposit.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['month', 'deposits'])
writer.writerows(months_list)