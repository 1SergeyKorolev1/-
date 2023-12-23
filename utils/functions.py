import json


def app_operation(operations_json):
    five_operations = get_five_last_operations(operations_json)
    for operation in five_operations:
        date = '.'.join((operation['date'].split('T'))[0].split('-'))
        num_1, num_2, num_3, num_4 = get_from(operation)
        amount = operation['operationAmount']['amount']
        print(f'\n{date} {operation['description']}')
        if num_3 == 1:
            print(f'{num_1} {num_2} -> Счет {num_4}')
        else:
            print(f'Счет {num_2}')
        print(f'{amount} руб.')


def get_five_last_operations(operations_json):
    with open(operations_json, encoding='utf-8') as f:
        list_operation = json.load(f)
        five_last_operations = list_operation[-5:]
        five_last_operations.reverse()
        return five_last_operations

def get_from(operation):
    if len(operation) > 6:
        len_from = len(operation['from'].split()[1])
        num_1 = operation['from'].split()[0]
        num_2 = grouper_account(operation['to'].split()[1])
        if len_from == 16:
            num = grouper_card(operation['from'].split()[1])
            return [num_1, num, 1, num_2]
        if len_from == 20:
            num = grouper_account(operation['from'].split()[1])
            return [num_1, num, 1, num_2]
    else:
        num = grouper_account(operation['to'].split()[1])
        return [0, num, 0, 0]

def grouper_card(iterable):
    list_ = []
    for i in range(0, 16):
        if i < 6 or i > 10:
            list_.append(iterable[i])
            if i == 3 or i == 11:
                list_.append(' ')
        else:
            list_.append('*')
            if i == 7:
                list_.append(' ')
    return ''.join(list_)

def grouper_account(iterable):
    list_ = []
    for i in range(0, 20):
        if 16 > i > 13:
            list_.append('*')
        elif i > 15:
            list_.append(iterable[i])
    return ''.join(list_)



