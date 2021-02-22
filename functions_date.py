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
    elif (fileType == "delux"):
        json_data = extract_data_from_files("Delux.txt")
    elif (fileType == "total"):
        json_data == extract_data_from_files("Total.txt")
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
