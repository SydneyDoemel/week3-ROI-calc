class RoiCalc:
    def __init__(self):
        self.rental_income_month = None
        self.total_expenses = None
        self.cash_flow = None
        self.total_investment = None
        self.roi = None
       

#THE BELOW DIDNT WORK, BUTT TRY  SOMETING ELSE
    def test_digit(self, x, my_string):
        valid = False
        while not valid: #loop until the user enters a valid int
            try:
                self.x = int(input(self.my_string))
                valid = True #if this point is reached, x is a valid int
            except ValueError:
                print('Please only input digits')



                
    def income(self):
        input("To begin calculating your cash on cash ROI, press enter: ")
        valid = False
        while not valid: #loop until the user enters a valid int
            try:
                self.rental_income_month = int(input("Enter your total monthly rental income: $"))
                valid = True #if this point is reached, x is a valid int
            except ValueError:
                print('Please only input digits')                                                                                   
                                                                                             
        #question about miscelannious or no?
        
        



        while True:
            go_back = input(f"Your total monthly income from this rental property is ${self.rental_income_month}. Press Y to confirm or N to change: ")
            if go_back.lower() == "y":
                return self.expenses()
            elif go_back.lower() == "n":
                valid = False
                while not valid: #loop until the user enters a valid int
                    try:
                        self.rental_income_month = int(input("Enter your total monthly rental income: $"))
                        valid = True #if this point is reached, x is a valid int
                    except ValueError:
                        print('Please only input digits')
            else:
                print("Invalid input")

            
    def expenses(self):
        expense_lst = {}

        #expense_lst["tax"] = int(input("Enter your monthly tax expense: $"))
        valid = False
        while not valid:
            try:
                expense_lst["tax"] = int(input("Enter your monthly tax expense: $"))
                valid = True 
            except ValueError:
                 print('Please only input digits')
        
        
        
        #expense_lst["insurance"] = int(input("Enter your insurance tax expense: $"))
        valid = False
        while not valid:
            try:
                expense_lst["insurance"] = int(input("Enter your insurance tax expense: $"))
                valid = True 
            except ValueError:
                 print('Please only input digits')


        expense_lst["utilities"] = int(input("Enter your monthly utilities expense, if not paid by tenant: $"))
        
        expense_lst["hoa"] = int(input("Enter your monthly HOA fee: $"))
       
        expense_lst["lawn"] = int(input("Enter your monthly lawn/snow expense: $"))
       
        expense_lst["vacancy"] = int(input("Enter your monthly vacancy expense: $"))
        
        expense_lst["repairs"] = int(input("Enter your monthly repairs expense: $"))
       
        expense_lst["capex"] = int(input("Enter your monthly CaPex expense: $"))
        
        expense_lst["prop_man"] = int(input("Enter your monthly property management expense: $"))
       
        expense_lst["mortgage"] = int(input("Enter your monthly mortgage payment: $"))



        
        print([f"{k}:{v}" for k,v in expense_lst.items()]) # how can i get this to print if not a list
        self.total_expenses = sum(expense_lst.values())
        print(f"Your total monthly expenses: ${self.total_expenses}.")
        self.cash_flow = self.rental_income_month - self.total_expenses
        print(f"Your total monthly cash flow is ${self.cash_flow}.")
        self.return_on()

    def return_on(self):
        invest_dict = {}
        input("Press enter to calculate your total investment: ")
        
        invest_dict["Down payment"] = int(input("Enter your down payment on this property: $"))
        
        invest_dict["Closing cost"] = int(input("Enter your closing costs on this property: $"))
       
        invest_dict["Rehab costs"] = int(input("Enter your rehab costs on this property: $"))
        
        invest_dict["Misc. costs"] = int(input("Enter any misc. costs on this property: $"))
        print(invest_dict)
        self.total_investment = sum(invest_dict.values())
        print(f"Your total investment is ${self.total_investment}")
        self.roi = ((self.cash_flow *12) /(self.total_investment)) * 10
        print(f"Your cash on cash ROI is {round(self.roi, 3)}%.")


new = RoiCalc()

new.income()