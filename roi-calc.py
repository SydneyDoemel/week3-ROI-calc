def check_digit(my_string):
            while True:
                try:
                    val = int(input(my_string))
                    return val
                except ValueError:  #should I use TypeError instead of ValueError?
                    print('Enter digits only.')

class RoiCalc:
    def __init__(self):
        self.rental_income_month = None
        self.total_expenses = None
        self.cash_flow = None
        self.total_investment = None
        self.roi = None
       
    def income(self):
        input("\nTo begin calculating your cash on cash ROI, press enter: ")
        self.rental_income_month = check_digit("Enter your total monthly rental income: $")                                                                                                                      
        while True:
            go_back = input("Your total monthly income from this rental property is $" + "{:,}".format(self.rental_income_month) + "\nEnter Y to confirm or N to change: ")
            if go_back.lower() == "y":
                return self.expenses()
            elif go_back.lower() == "n":
                self.rental_income_month = check_digit("Enter your total monthly rental income: $")
            else:
                print("Invalid input.")

            
    def expenses(self):
        expense_dict= {"Tax":"tax expense", "Insurance": "insurance expense", "Utilities": "utilities expense", "HOA": "HOA fee", "Lawn/snow": "lawn/snow expense", "Vacancy": "vacancy expense", "Repairs": "repairs expense", "CaPex": "CaPex expense", "Property Management":"property management expense", "Mortgage": "mortgage payment"}
        print("\n")
        for k,v in expense_dict.items():
            expense_dict[k]= check_digit(f"Enter your monthly {v}: $")
        print("\n")
    
        print("\n".join("{}: ${:,}".format(k, v) for k, v in expense_dict.items()))
        self.total_expenses = sum(expense_dict.values())
        print("\nYour total monthly expenses: $"+ "{:,}".format(self.total_expenses))
        self.cash_flow = self.rental_income_month - self.total_expenses
        print("Your total monthly cash flow: $"+"{:,}".format(self.cash_flow))
        self.return_on()

    def return_on(self):
        invest_dict = {"Down payment": "your down payment", "Closing cost": "your closing costs", "Rehab costs":"your rehab costs", "Misc. costs": "any miscellaneous costs"}
        input("Press enter to calculate your total investment: \n")
        for k,v in invest_dict.items():
            invest_dict[k] = check_digit(f"Enter {v} for this property: $")
        print("\n")

        print("\n".join("{}: ${:,}".format(k, v) for k, v in invest_dict.items()))
        self.total_investment = sum(invest_dict.values())
        print(f"\nYour total investment is $" + "{:,}".format(self.total_investment))
        self.roi = ((self.cash_flow *12) /(self.total_investment)) * 10
        print(f"Your cash on cash ROI is {round(self.roi, 3)}%")


my_property  = RoiCalc()
my_property.income()