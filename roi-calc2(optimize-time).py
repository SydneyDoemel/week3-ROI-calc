
def try_catch(self,my_string):
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
        self.rental_income_month = self.try_catch("Enter your total monthly rental income: $")                                                                                                                      
        while True:
            go_back = input(f"Your total monthly income from this rental property is ${self.rental_income_month}.\nEnter Y to confirm or N to change: ")
            if go_back.lower() == "y":
                return self.expenses()
            elif go_back.lower() == "n":
                self.rental_income_month = self.try_catch("Enter your total monthly rental income: $")
            else:
                print("Invalid input. Enter Y to confirm or N to change:")

            
    def expenses(self):
        expense_dict= {}
        expense_dict["Tax"] = self.try_catch("Enter your monthly tax expense: $")
        expense_dict["Insurance"] = self.try_catch("Enter your monthly insurance expense: $")
        expense_dict["Utilities"] = self.try_catch("Enter your monthly utilities expense: $")
        expense_dict["HOA"] = self.try_catch("Enter your monthly HOA fee expense: $")
        expense_dict["lawn/snow"] = self.try_catch("Enter your monthly lawn/snow expense expense: $")
        expense_dict["Vacancy"] = self.try_catch("Enter your monthly vacancy expense: $")
        expense_dict["Repairs"] = self.try_catch("Enter your monthly repairs expense: $")
        expense_dict["CaPex"] = self.try_catch("Enter your monthly CaPex expense: $")
        expense_dict["Property Management"] = self.try_catch("Enter your monthly property management expense: $")
        expense_dict["Mortgage"] = self.try_catch("Enter your monthly mortgage payment: $")
        

        print("\n","\n".join("{}: ${}".format(k, v) for k, v in expense_dict.items()))
        self.total_expenses = sum(expense_dict.values())
        print(f"Your total monthly expenses: ${self.total_expenses}.")
        self.cash_flow = self.rental_income_month - self.total_expenses
        print(f"Your total monthly cash flow: ${self.cash_flow}.")
        self.return_on()

    def return_on(self):
        invest_dict = {}
        input("Press enter to calculate your total investment: ")
        invest_dict["Down Payment"]= self.try_catch("Enter your down payment for this property: $")
        invest_dict["Closing cost"]= self.try_catch("Enter your your closing costs for this property: $")
        invest_dict["Rehab costs"]= self.try_catch("Enter your your rehab costs for this property: $")
        invest_dict["Misc. costs"]= self.try_catch("Enter any miscellaneous costs for this property: $")
        
       
        print("\n","\n".join("{}: ${}".format(k, v) for k, v in invest_dict.items()))
        self.total_investment = sum(invest_dict.values())
        print(f"Your total investment is ${self.total_investment}")
        self.roi = ((self.cash_flow *12) /(self.total_investment)) * 10
        print(f"Your cash on cash ROI is {round(self.roi, 3)}%.")


my_property  = RoiCalc()
my_property.income()