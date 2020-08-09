import json


def add_company_to_targeted_companies(company):
    """
    Accepts string as input, checks to make sure it is a valid company
    then adds company to targeted_companies.json file.
    """
    if is_real_company(company):
        target = None
        with open('../user_data/target_list.json', 'r+') as file:
            if is_unique(company):
                response = json.load(file)
                response["companies"].append(company)
                target = response
            else:
                return
        with open('../user_data/target_list.json', 'w+') as file:
            file.write(json.dumps(target))
    else:
        print('Not real company')


def is_real_company(ticker):
    with open('../user_data/sp500_companies.json', 'r') as file:
        return ticker in json.load(file)


def is_unique(ticket):
        with open('../user_data/target_list.json', 'r+') as file:
            response = json.load(file)
            for i in response["companies"]:
                if i == ticket:
                    return False
            return True


# if __name__ == "__main__":
#     print(is_real_company('AAPL'))
#     add_company_to_targeted_companies('AAPLlll')
