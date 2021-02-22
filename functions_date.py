import json
import datetime

def extract_data_from_files(fileName):
    text_file = open("files/" + fileName)
    text_data = text_file.read().split("\n")
    text_list = text_data[::-1]
    text_json = dict()
    date_curr = datetime.datetime.today()
    for i in range(len(text_list)):
        if((text_list[i]).isdigit()):
            text_json[date_curr.strftime("%m/%d/%Y")] = int(text_list[i])
            date_curr -= datetime.timedelta(days=1)
    return text_json

def year_rev(fileType):
    json_data = dict()
    if (fileType == "basic"):
        json_data = extract_data_from_files("Basic.txt")
    json_keys = json_data.keys()
    list_of_years = []
    for x in json_keys:
        list_of_years.append(int(x.split("/")[2]))
    list_of_unique_values = set(list_of_years)
    return list_of_unique_values

def get_rev_details(rev_year):
    basic_json_data = extract_data_from_files("Basic.txt")
    delux_json_data = extract_data_from_files("Delux.txt")
    total_json_data = extract_data_from_files("Total.txt")
    basic_list = {key:value for key,value in basic_json_data.items() if int(key.split("/")[2]) == rev_year }
    delux_list = {key:value for key,value in delux_json_data.items() if int(key.split("/")[2]) == rev_year }
    total_list = {key:value for key,value in total_json_data.items() if int(key.split("/")[2]) == rev_year }
    basics_count = sum(basic_list.values())
    delux_count = sum(delux_list.values())
    total_count = sum(total_list.values())
    message = "----" + str(rev_year)+ " Yearly Revenue ----\n"
    message += "You have sold total basic cupcakes " + str(basics_count) + "\n"
    message += "and delux cupcakes " + str(delux_count) + "\n"
    message += "and total amount for year " + str(rev_year) + " is : $" + str(total_count)
    print(message)

def month_rev(year_rev,fileType):
    json_data = dict()
    if (fileType == "basic"):
        json_data = extract_data_from_files("Basic.txt")
    json_keys = json_data.keys()
    list_of_months = []
    for x in json_keys:
        if int(x.split("/")[2]) == year_rev:
            list_of_months.append(int(x.split("/")[0]))
    list_of_unique_values = set(list_of_months)
    return list_of_unique_values

def month_revenue(rev_month, rev_year):
    basic_json_data = extract_data_from_files("Basic.txt")
    delux_json_data = extract_data_from_files("Delux.txt")
    total_json_data = extract_data_from_files("Total.txt")
    basic_list = {key:value for key,value in basic_json_data.items() if (int(key.split("/")[2]) == rev_year) and (int(key.split("/")[0]) == rev_month) }
    delux_list = {key:value for key,value in delux_json_data.items() if (int(key.split("/")[2]) == rev_year) and (int(key.split("/")[0]) == rev_month) }
    total_list = {key:value for key,value in total_json_data.items() if (int(key.split("/")[2]) == rev_year) and (int(key.split("/")[0]) == rev_month) }
    basics_count = sum(basic_list.values())
    delux_count = sum(delux_list.values())
    total_count = sum(total_list.values())
    message = "----" + str(rev_year)+ " - " + str(rev_month) +" Monthly Revenue ----\n"
    message += "You have sold total basic cupcakes " + str(basics_count) + "\n"
    message += "and delux cupcakes " + str(delux_count) + "\n"
    message += "and total amount for month "+ str(rev_month) +" - "+ str(rev_year) + " is : $" + str(total_count)
    print(message)
    
def get_total_rev_details():
    basic_json_data = extract_data_from_files("Basic.txt")
    delux_json_data = extract_data_from_files("Delux.txt")
    total_json_data = extract_data_from_files("Total.txt")
    basics_count = sum(basic_json_data.values())
    delux_count = sum(delux_json_data.values())
    total_count = sum(total_json_data.values())
    message = "---- Total Revenue ----\n"
    message += "You have sold total basic cupcakes " + str(basics_count) + "\n"
    message += "and delux cupcakes " + str(delux_count) + "\n"
    message += "and total amount is : $" + str(total_count)
    print(message)