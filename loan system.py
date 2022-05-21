class Borrower:# making object class
    samount=0
    def __init__(self,borrower_name,mobno,adress,salary):
        
        print("Welcome to the loaning services")
          # initializing the value
        self.borrower_name=borrower_name
        self.mobno=mobno
        self.adress=adress
        self.salary=salary
        
        
 
    def approval(self): # making functions wrt to the class
        lamount=float(input("Enter amount for the loan : "))
        time=float(input("Enter the no of yeras for loan:"))
        
        
        
                   
        if(self.salary>lamount):           
                   
            print("Loan amount approved")
        else:
            print("Loan amount rejected")
        
     
 
    def rate_interest(self):
        lamount=float(input("Enter amount for the loan : "))

        if lamount<=(self.salary)/2:
            
            print("\n Rate of interest", 8)
        else:
            print("\n Rate of interest  ",10)

class Lender(Borrower):
     
     def __init__(lend,lender_name,mobno,adress):
         
         lend.lender_name=lender_name
         lend.mobno=mobno
         lend.adress=adress
        
 

  
# creating an object of class
s =Borrower("vivek",6444355335,"lucknow",4500)
P= Lender("Anuj",9533522556,"Kanpur")
# Calling functions with that class object
s.approval()
s.rate_interest()


