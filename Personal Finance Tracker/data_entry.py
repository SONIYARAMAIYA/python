from datetime import datetime

date_format="%d-%m-%y"
CATEGORIES={'I':'income','E':'expense'}
 
    
def get_date(prompt, allow_date=False):
    date_str = input(prompt)
    if allow_date and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print(f"Invalid format. Please enter the date in '{date_format}' format.")
        return get_date(prompt, allow_date)


def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError("Amount must be a positive, non-zero value.")
            return amount
        except ValueError as e:
            print(e)

    
def get_category():
    while True:
        category = input("Enter the category ('I' for income or 'E' for expense): ").upper()
        if category in CATEGORIES:
            return CATEGORIES[category]
        print("Invalid category. Please enter 'I' for income or 'E' for expense.")

def get_description():
    return input("enter a description (optional): ")