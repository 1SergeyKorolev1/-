from utils import functions

def app_operation(operations_json):
    five_operations = functions.get_five_operations(operations_json)
    for operation in five_operations:
        date = functions.get_date_reverse(operation)
        name, from_num, to_num, name_2 = functions.get_from_and_to(operation)
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f'\n{date} {operation['description']}')
        if name != 0:
            print(f'{name} {from_num} -> {name_2} {to_num}')
        else:
            print(f'{name_2} {to_num}')
        print(f'{amount} {currency}')