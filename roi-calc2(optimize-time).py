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
        expense_dict= {}
        expense_dict["Tax"] = check_digit("Enter your monthly tax expense: $")
        expense_dict["Insurance"] = check_digit("Enter your monthly insurance expense: $")
        expense_dict["Utilities"] = check_digit("Enter your monthly utilities expense: $")
        expense_dict["HOA"] = check_digit("Enter your monthly HOA fee expense: $")
        expense_dict["lawn/snow"] = check_digit("Enter your monthly lawn/snow expense expense: $")
        expense_dict["Vacancy"] = check_digit("Enter your monthly vacancy expense: $")
        expense_dict["Repairs"] = check_digit("Enter your monthly repairs expense: $")
        expense_dict["CaPex"] = check_digit("Enter your monthly CaPex expense: $")
        expense_dict["Property Management"] = check_digit("Enter your monthly property management expense: $")
        expense_dict["Mortgage"] = check_digit("Enter your monthly mortgage payment: $")
        
        print("\n")
        print("\n".join("{}: ${:,}".format(k, v) for k, v in expense_dict.items()))
        self.total_expenses = sum(expense_dict.values())
        print("\nYour total monthly expenses: $"+ "{:,}".format(self.total_expenses))
        self.cash_flow = self.rental_income_month - self.total_expenses
        print("Your total monthly cash flow: $"+"{:,}".format(self.cash_flow))
        self.return_on()

    def return_on(self):
        invest_dict = {}
        input("Press enter to calculate your total investment: ")
        invest_dict["Down Payment"]= check_digit("Enter your down payment for this property: $")
        invest_dict["Closing cost"]= check_digit("Enter your your closing costs for this property: $")
        invest_dict["Rehab costs"]= check_digit("Enter your your rehab costs for this property: $")
        invest_dict["Misc. costs"]= check_digit("Enter any miscellaneous costs for this property: $")
        
        print("\n")
        print("\n".join("{}: ${:,}".format(k, v) for k, v in invest_dict.items()))
        self.total_investment = sum(invest_dict.values())
        print(f"\nYour total investment is $" + "{:,}".format(self.total_investment))
        self.roi = ((self.cash_flow *12) /(self.total_investment)) * 10
        print(f"Your cash on cash ROI is {round(self.roi, 3)}%")


my_property  = RoiCalc()
my_property.income()