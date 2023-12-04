# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:31:21 2023

@author: christopher.squires
"""

sales = [{'Date':'2020-12-22', 'Quarter':'4', 'Region':'West', 'Amount':12493},
         {'Date':'2021-09-15', 'Quarter':'3', 'Region':'East', 'Amount':13761},
         {'Date':'2021-05-15', 'Quarter':'2', 'Region':'East', 'Amount':9710},
         {'Date':'2021-08-08', 'Quarter':'3', 'Region':'Central', 'Amount':8934}]

regions = {'w':'West', 'm':'Mountain', 'c':'Central', 'e':'East'}

import csv

def write_file():
    with open('sales_data_importer', 'w') as fh:
        for row in sales:
            string_to_write = row['Date']+ ',' + row['Quarter']+ ',' + row['Region']+ ',' + row['Amount']+ '\n'
            fh.write(string_to_write)

def title():
    print("SALES DATA IMPORTER\n")
    
def menu():
    print("COMMAND MENU")
    print('view\t - View all sales')
    print('add\t\t - Add sales')
    print('import   - Import sales from file')
    print("menu\t - Show menu")
    print('exit\t - Exit program')
    print()
    
def view():
    total = 0
    print('\tDate\t\tQuarter\t\tRegion\t\tAmount')
    print('-'*50)
    for i, info in enumerate(sales):
        total += float(info['Amount'])
        print('{}. {}\t\t{}\t\t{}\t\t${}'.format(i + 1, info['Date'], info['Quarter'], info['Region'], float(info['Amount'])))
    print('-'*50)
    print(f'TOTAL: \t\t\t\t\t\t\t\t\t${total}')
    
def new_sale_amount():
    new_amount = float(input('Sale amount: '))
    return new_amount
    
def get_year():
    loop = True
    while loop:
        try:
            year = int(input('Year: '))
            if year < 1900 or year > 3000:
                print("Invalid selection")
            else:
                break
        except:
            print("Invalid selection")
    return year

def get_month():
    loop = True
    while loop:
        try:
            month = int(input('Month: '))
            if month < 1 or month > 12:
                print('Invalid selection')
            else:
                break
        except:
            print('Invalid selection')
    return month

def get_day(get_month):
    month = get_month()
    while True:
        try:
            if month == 4 or month == 6 or month == 9 or month == 11:
                days = 30
            elif month == 2:
                days = 28
            else:
                days = 31
            day = int(input(f'Day (1-{days}): '))
            if day < 1 or day > days:
                print('Invalid selection')
            else:
                break
        except:
            print("Invalid selections")
    return day

def get_quarter(get_month):
    month = get_month()
    quarter = 0
    if month == 1 or month == 2 or month == 3:
        quarter = 1
    elif month == 4 or month == 5 or month == 6:
        quarter = 2
    elif month == 7 or month == 8 or month == 9:
        quarter = 3
    elif month == 10 or month == 11 or month == 12: 
        quarter = 4
    return quarter

def get_region():
    while True:
        region = input(f'Enter region {regions.keys()}: ').lower()
        if region in regions.keys():
            return regions[region]
        else:
            print(f'Enter a valid region. The supported regions are {regions.keys()}')
            
def add_sale():
    amount = new_sale_amount()
    year = get_year()
    month = get_month()
    day = get_day(get_month)
    region = get_region()
    print()
    
    quart = get_quarter(get_month)
    
    sales_data = {'Amount':amount, 'Year':year, 'Month':month, 
                  'Day':day, 'Quarter':quart, 'Region':region}
    sales.append(sales_data)
    print(f'sale for {year}-{month}-{day} added')
    
def main():
    title()
    menu()
    
    command = input('Command: ')
    
    loop = True
    while loop:
        if command == 'view':
            view()
        elif command == 'add':
            add_sale()
        elif command == 'import':
            print('lol no')
        elif command == 'menu':
            menu()
        elif command == 'exit':
            break
    print('Bye!')
    
main()