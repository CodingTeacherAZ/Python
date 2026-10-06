class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = [] 

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        
        # if self.check_funds(amount):
        #     self.withdraw(amount,f"Transfer to {destination.name}" )
        #     destination.deposit(amount,f"Transfer from {self.name}")
        #     return True
        # else:
        #     return False
        

        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
       
    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance
        # return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount, destination):
        if not self.withdraw(amount, f"Transfer to {destination.name}"):
            return False
        
        destination.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        '''
        example output:
        *************Food*************
        initial deposit        1000.00
        groceries               -10.15
        restaurant and more foo -15.89
        Transfer to Clothing    -50.00
        Total: 923.96
        '''
        lines = [f"{self.name:*^30}"]

        for entry in self.ledger:
            lines.append(
                f"{entry['description']:<23.23s}" 
                f"{entry['amount']:>7.2f}"
            )
                         
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)

        
def create_spend_chart(categories):
    '''
    example output:
    Percentage spent by category
    100|          
     90|          
     80|          
     70|          
     60| o        
     50| o        
     40| o        
     30| o        
     20| o  o     
     10| o  o  o  
      0| o  o  o  
        ----------
        F  C  A  
        o  l  u  
        o  o  t  
        d  t  o  
            h     
            i     
            n     
            g     

    '''
    
    bar_chart = "Percentage spent by category\n"

    ## Subtask 1

    category_spending = []
    for account in categories:
        spending_record = {'name': account.name}
        running_total = 0
        for index in range(len(account.ledger)):
            if account.ledger[index]["amount"] < 0 and not account.ledger[index]["description"].startswith("Transfer"):
                running_total += account.ledger[index]["amount"] * -1
        spending_record['withdrawals'] = round(running_total,2)
        category_spending.append(spending_record)

    ## Subtask 2

    total_spent = 0
    for account in category_spending:
        total_spent += account["withdrawals"]
    
    for record in category_spending:
        record["percent"] = record["withdrawals"] / total_spent * 100 // 10 * 10
    
    # Subtask 3

    master_graph = ""        
    for level in range(100,-1,-10): 
        current_line = f"{level:>3}| "
        for index in range(len(category_spending)):
            if category_spending[index]['percent'] >= level:
                current_line += f"{'o':<3}"
            else:
                current_line += "   "
        current_line += "\n"
        master_graph += current_line
    bar_chart+= master_graph
    bar_chart += "    "+"---"*len(category_spending)+"-"

    longest = 0
    for record in category_spending:
        if len(record['name']) >longest:
            longest = len(record['name'])
    
    titles = ""
    for character_index in range(longest): 
        current_line = "    "

        for record in category_spending:
            name = record["name"]
            if character_index < len(name):
                current_line += f"{name[character_index]:^3}"
            else:
                current_line += "   "



        current_line += " \n"
        titles += current_line
    bar_chart +="\n"
    bar_chart+= titles[0:-1]

   


    return bar_chart


## Tests
checking = Category('Checking')
food = Category('Food')
clothing = Category('Clothing')
savings = Category('Savings')
auto = Category('Auto')

checking.deposit(1844.99, 'payroll deposit')
checking.transfer(200,food)
checking.transfer(75, clothing)
checking.transfer(7*50+100+100, auto)
checking.transfer(1000,savings)


food.withdraw(143.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')


auto.withdraw(48.90, 'off-roading gas')
auto.withdraw(48.90, 'off-roading gas')
auto.withdraw(48.90, 'off-roading gas')
auto.withdraw(48.90, 'off-roading gas')
auto.withdraw(48.90, 'off-roading gas')
auto.withdraw(48.90, 'off-roading gas')
auto.withdraw(38.50, 'off-roading gas')
auto.withdraw(45.75, 'off-roading gas')




print(checking)
print(food)
print(auto)
print(clothing)
print(savings)

all_accounts = [checking,food, auto, clothing,savings]
print(create_spend_chart(all_accounts))
