from functions_date import *

# Upload Files Function
def uploadFiles():
    print("Feature will be updated soon")

def yr_revenue():
    basic_rev = year_rev("basic")
    year_selection(basic_rev)

def mo_revenue():
    basic_rev = year_rev("basic")
    mo_selection(basic_rev)

def mo_selection(basic_rev):
    print("we have following year to display:")
    for x in basic_rev:
        print(x)
    select_year = input("Which year you want to check? : ")
    if (int(select_year) in basic_rev):
        monthly_rev = month_rev(int(select_year), "basic")
        print(monthly_rev)
        month_selection(monthly_rev,int(select_year))
    else:
        print("Please enter year number")
        mo_selection(basic_rev)

def month_selection(month_rev,select_year):
    print("We have following months for year " + str(select_year))
    for x in month_rev:
        print(x)
    select_month = input("Which month you want to check? :")
    if(int(select_month) in month_rev):
        month_revenue(int(select_month),select_year)
    else:
        print("Please select month")
        month_selection(month_rev,select_year)


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

def total_revenue():
    get_total_rev_details()


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
        print("Please enter number either 1,2,3,4 or 5")
    if inputVal == 1:
        uploadFiles()
    elif inputVal == 2:
        yr_revenue()
    elif inputVal == 3:
        mo_revenue()
    elif inputVal == 4:
        total_revenue()
    elif inputVal == 5:
        exit()
    else:
        print("Invalid Selection. Please try again")
        main()            

if __name__ == "__main__":
    main()