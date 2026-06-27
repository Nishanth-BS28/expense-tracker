import json
try:
    with open ('expences.json', 'r') as f:
        expences=json.load(f)
except FileNotFoundError:
    expences = []

while True:
    add_expense = input('do you want to add expense? (yes/no)')
    if add_expense=='yes':
        item =input('enter item')
        amount = int(input('enter amount'))
        expense = {"item": item, "amount": amount}
        expences.append(expense)
        with open ('expences.json', 'w') as f:
            json.dump(expences, f)
        print('added')
    else:
        print('done')  
        break 
    