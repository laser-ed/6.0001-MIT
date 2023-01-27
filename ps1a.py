annual_salary = float(input('Enter your annual salary: '))
monthly_salary = annual_salary / 12
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the value of your dream home: '))

portion_down_payment = 0.25 * total_cost
current_savings = 0
annualized_rate = 0.04
months = 0

while current_savings < portion_down_payment:
    current_savings += (current_savings * annualized_rate / 12) + ( portion_saved * monthly_salary)
    months += 1
    
    
print('Number of Months: ', months)
