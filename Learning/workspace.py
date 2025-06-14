savings = input()
monthly = int(savings)/12
weekly = int(savings)/48
daily = int(savings)/365

#cast to string and concatenate
print('To save up' + savings + ' dollars in onle year, you will need to save ' + str(round(monthly,2)))

# use the comma operator when using different data types
print('To save up' + savings + ' dollars in onle year, you will need to save ' , str(round(monthly,2)))
