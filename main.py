from functions_date import *


def uploadFiles():
    print("Feature will be updated soon")

def Yr_revenue():
    basic_rev = year_rev("basic")
    year_selection(basic_rev)

def Mo_revenue():
    basic_rev = year_rev("basic")
    month_selection(basic_rev)

def month_selection(basic_rev):
    print("we have following year:")
    for x in basic_rev:
        print(x)
    select_year = input("Which year you want to check? : ")
    if (int(select_year) in basic_rev):
        get_rev_details(int(select_year))
    else:
        print("Please enter year number")
        month_selection(basic_rev)


def year_selection(basic_rev):
    print("we have following year:")
    for x in basic_rev:
        print(x)
    select_year = input("Which year you want to check? : ")
    if (int(select_year) in basic_rev):
        get_rev_details(int(select_year))
    else:
        print("Please enter year number")
        year_selection(basic_rev)

def main():
    message = """Hello Owner,
    enter the number to check respective details
    1. Upload updated files
    2. Yearly Revenue Totals
    3. Monthly Revenue Totals
    4. Total Revenue
    5. Exit
    Enter Number: """
    inputVal = input(message)
    try:
        inputVal = int(inputVal)
    except:
        print("Please entter number either 1,2,3,4 or 5")
    if inputVal == 1:
        uploadFiles()
    elif inputVal == 2:
        Yr_revenue()
    elif inputVal == 3:
        Mo_revenue()
    elif inputVal == 4:
        Total_revenue()
    elif inputVal == 5:
        exit()
    else:
        print("Invalid Selection. Please try again")
        main()
        print("else")
    print("else")
    
    
if __name__ == "__main__":
    main()