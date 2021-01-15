#!/usr/bin/env python3
# Author: Yogesh Kulkarni
# user id: cpucortexm
# python script to read csv file and writing to a text file. CSV contains name, username and department of the employee.
# The sript reads the csv file as input and generates a text file containing the number of people in each department

import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect',skipinitialspace=True,strict=True)
    employee_file = csv.DictReader(open(csv_file_location),dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list



def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    if __debug__:
        print("department list:")
        print(department_list) # enable for debugging

    department_data = {} # generate dictionary from list
    for department_name in set(department_list):  # set(list) produces unique values and discards repeating values present in the list
        if __debug__:
            print(department_name) # enable for debugging
        department_data[department_name] = department_list.count(department_name) #now create a dictionary with dept_name as key and count as value

    return department_data


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
         for k in sorted(dictionary):  # sort(dict) gives sorted by name
             f.write(str(k)+':'+str(dictionary[k])+'\n')
         f.close()


employee_list = read_employees('/home/yk/Desktop/csv/employees.csv')
print(employee_list)
dictionary = process_data(employee_list)
print(dictionary)
write_report(dictionary, '/home/yk/Desktop/csv/test_report.txt')

