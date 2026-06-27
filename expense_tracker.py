import json
try:
    with open ('expenses.json', 'r') as f:
        expenses=json.load(f)
except FileNotFoundError:
    expenses = []

while True:
    add_expense = input('do you want to add expense? (yes/no)')
    if add_expense=='yes':
        item =input('enter item')
        amount = int(input('enter amount'))
        expense = {"item": item, "amount": amount}
        expenses.append(expense)
        with open ('expences.json', 'w') as f:
            json.dump(expenses, f)
        print('added')
    else:
        print('done')  
        break 
    