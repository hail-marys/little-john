# have main impot add_to_target_list
# import os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)

import json
import os
import pyfiglet
from termcolor import colored, cprint
# from little_john.main import start

import finnhub
finnhub_client = finnhub.Client(api_key="brqm9efrh5rce3ls8mdg")


def sub_menu():
    """
    Prints menu to add company to targeted company list. Takes in user input to navigate this menu.
    after user input of 1-5, sub_menu() gets called again, and menu redisplayed. If 6 is seleceted,
    returns user back to main menu which calls this function.
    """
    os.system('clear' if os.name == 'nt' else 'clear')
    title = pyfiglet.figlet_format('TARGETED COMPANIES LIST')
    print(title)
    print("""
Would you like to:
1. View current companies
2. Add a company
3. Add all S&P 500 Index companies to list
4. Remove a company
5. Remove all companies
6. Go back to main menu
    """)
    choice = input('>')
    while choice.isnumeric() == False or int(choice) < 0 or int(choice) > 6:
        print('\nPlease input a number between 1 and 6\n')
        choice = input('>')

    if int(choice) == 1:
        print(view_companies())
        input('Press any key to continue')
        os.system('clear' if os.name == 'nt' else 'clear')
        sub_menu()

    if int(choice) == 2:
        print('\nEnter symbol of company to add to list')
        print(add_company_to_targeted_companies(input('>')))
        input('Press any key to continue')
        os.system('clear' if os.name == 'nt' else 'clear')
        sub_menu()

    if int(choice) == 3:
        print('\nAre you sure you want to add all S&P 500 companies to the targeted list? y/n')
        response = input('>')
        while response.lower() != 'y' and response.lower() != 'n':
            print('Please enter y to confirm, or n to go back')
            response = input('>')
        if response == 'n':
            os.system('clear' if os.name == 'nt' else 'clear')
            sub_menu()
        else:
            print('Adding all 500 companies now...')
            with open('user_data/sp500_companies.json', 'r') as file:
                for i in json.load(file):
                    add_company_to_targeted_companies(i)
            print('Successfully added all S&P 500 companies.')
            input('Press any key to continue')
            os.system('clear' if os.name == 'nt' else 'clear')
            sub_menu()

    if int(choice) == 4:
        print('\nEnter company symbol to remove from targeted list')
        print(remove_company_from_targeted_companies(input('>')))
        input('Press any key to continue')
        os.system('clear' if os.name == 'nt' else 'clear')
        sub_menu()

    if int(choice) == 5:
        print('\nAre you sure you want to clear your targeted list? y/n')
        response = input('>')
        while response.lower() != 'y' and response.lower() != 'n':
            print('Please enter y to confirm, or n to go back')
            response = input('>')
        if response == 'n':
            os.system('clear' if os.name == 'nt' else 'clear')
            sub_menu()
        else:
            with open('user_data/sp500_companies.json', 'r') as file:
                for i in json.load(file):
                    remove_company_from_targeted_companies(i)
            print('Targeted companies list was cleared')
            input('Press any key to continue')
            os.system('clear' if os.name == 'nt' else 'clear')
            sub_menu()

    if int(choice) == 6:
        # this way when main.py calls sub_menu(), it can return to the main menu
        return


def add_company_to_targeted_companies(company):
    """
    Accepts string as input, checks to make sure it is a valid company
    then adds company to targeted_companies.json file.
    """
    company = company.upper()
    if is_real_company(company):
        target = None
        with open('user_data/target_list.json', 'r+') as file:
            if is_unique(company):
                response = json.load(file)
                response["companies"].append(company)
                target = response
            else:
                return f'{company} is already on the list.'
        with open('user_data/target_list.json', 'w+') as file:
            file.write(json.dumps(target))
            return f'Successfully added {company} to list.'
    else:
        return f'{company} symbol does not match a company, please try again.'


def remove_company_from_targeted_companies(company):
    """
    Accepts string as input, checks to make sure it is a valid company, and is currently on list,
    then removes company from targeted_companies.json file.
    """
    company = company.upper()
    if is_real_company(company):
        target = None
        with open('user_data/target_list.json', 'r+') as file:
            if is_unique(company) == False:
                response = json.load(file)
                response["companies"].remove(company)
                target = response
            else:
                return f'{company} was not on the list.'
        with open('user_data/target_list.json', 'w+') as file:
            file.write(json.dumps(target))
            return f'Successfully removed {company} from list.'
    else:
        return f'{company} symbol does not match a company, please try again.'


def is_real_company(ticker):
    """
    Takes in string as input. Returns true if ticker is in sp500_companies.json file. If not,
    then it checks if the finnhub API returns any data on company. If not in json file and 
    finnhub returns no data then returns False.
    """
    with open('user_data/sp500_companies.json', 'r') as file:
        if ticker in json.load(file):
            return True
    data = finnhub_client.company_profile(symbol=ticker)
    if data == {}:
        return False
    else:
        return True


def is_unique(ticker):
    """
    Takes in one string argument. Returns True if the ticker given is not in the target_list.json
    file. Returns False if the ticker is in the file. This prevents the user from adding the same company
    multiple times or removing a company that is not there.  
    """
    with open('user_data/target_list.json', 'r+') as file:
        response = json.load(file)
        for i in response["companies"]:
            if i == ticker:
                return False
        return True


def view_companies():
    """
    Takes in no arguments. Reads the list of companies in target_list.json file, and returns them as
    a multi line string. 
    """
    companies = ''
    with open('user_data/target_list.json', 'r') as file:
        response = json.load(file)
        for i in response['companies']:
            companies += f'-{i}\n'
    return f'\nYour target companies are:\n{companies}'

if __name__ == "__main__":
    sub_menu()
