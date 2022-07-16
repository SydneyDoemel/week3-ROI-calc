class RoiCalc:
    def __init__(self):
        self.rental_income_month = None
        self.total_expenses = None
        self.cash_flow = None
        self.total_investment = None
        self.roi = None
    def income(self):
        input("To begin calculating your cash on cash ROI, press enter: ")
        active  = True
        while active:                                                                           #This is repeated below.
            self.rental_income_month = input("Enter your total monthly rental income: $")       # Should I just
            if self.rental_income_month.isdigit() != True:                                      # have it call back
                print("Please enter only digits.")                                              #instead of repeating
            else:                                                                               #the whole thing
                self.rental_income_month = int(self.rental_income_month)                        #again
                active  = False                                                                 #?
        #question about miscelannious or no?
        while True:
            go_back = input(f"Your total monthly income from this rental property is ${self.rental_income_month}. Press Y to confirm or N to change: ")
            if go_back.lower() == "y":
                return self.expenses()
            elif go_back.lower() == "n":
                active  = True
                while active:
                    self.rental_income_month = input("Enter your total monthly rental income: $")
                    if self.rental_income_month.isdigit() != True:
                        print("Please enter only digits.")
                    else:
                        self.rental_income_month = int(self.rental_income_month)
                        active  = False
            else:
                print("Invalid input")

            
    def expenses(self):
        expense_lst = {}
        expense_lst["tax"] = int(input("Enter your monthly tax expense: $"))
        
        expense_lst["insurance"] = int(input("Enter your insurance tax expense: $"))
      
        expense_lst["utilities"] = int(input("Enter your monthly utilities expense, if not paid by tenant: $"))
        
        expense_lst["hoa"] = int(input(input("Enter your monthly HOA fee: $")))
       
        expense_lst["lawn"] = int(input("Enter your monthly lawn/snow expense: $"))
       
        expense_lst["vacancy"] = int(input("Enter your monthly vacancy expense: $"))
        
        expense_lst["repairs"] = int(input("Enter your monthly repairs expense: $"))
       
        expense_lst["capex"] = int(input("Enter your monthly CaPex expense: $"))
        
        expense_lst["prop_man"] = int(input("Enter your monthly property management expense: $"))
       
        expense_lst["mortgage"] = int(input("Enter your monthly mortgage payment: $"))
        print(expense_lst)
        self.total_expenses = sum(expense_lst.values())
        print(f"Your total monthly expenses: ${self.total_expenses}.")
        self.cash_flow = self.rental_income_month - self.total_expenses
        print(f"Your total monthly cash flow is ${self.cash_flow}.")
        self.return_on()

    def return_on(self):
        invest_dict = {}
        input("Press enter to calculate your total investment: ")
        down = input("Enter your down payment on this property: $")
        invest_dict["Down payment"] = int(down)
        closing = input("Enter your closing costs on this property: $")
        invest_dict["Closing cost"] = int(closing)
        rehab = input("Enter your rehab costs on this property: $")
        invest_dict["Rehab costs"] = int(rehab)
        misc = input("Enter any misc. costs on this property: $")
        invest_dict["Misc. costs"] = int(misc)
        print(invest_dict)
        self.total_investment = sum(invest_dict.values())
        print(f"Your total investment is ${self.total_investment}")
        self.roi = ((self.cash_flow *12) /(self.total_investment)) * 10
        print(f"Your cash on cash ROI is {self.roi}%.")


new = RoiCalc()
new.income()
new.expenses()