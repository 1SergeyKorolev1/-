import json


def get_five_operations(operations_json):
    with open(operations_json, encoding='utf-8') as f:
        list_operation = json.load(f)
        five_last_operations = list_operation[-5:]
        five_last_operations.reverse()
        return five_last_operations

def get_from_and_to(operation):
    to_list = operation['to'].split()
    if len(to_list) == 3:
        to_num = to_list[2]
        name_2 = f'{to_list[0]} {to_list[1]}'
    else:
        to_num = to_list[1]
        name_2 = to_list[0]
    if len(to_num) == 16:
        num_2 = grouper_card(to_num)
    else:
        num_2 = grouper_account(to_num)
    if len(operation) > 6:
        from_list = operation['from'].split()
        if len(from_list) == 3:
            from_num = from_list[2]
            name = f'{from_list[0]} {from_list[1]}'
        else:
            from_num = from_list[1]
            name = from_list[0]
        if len(from_num) == 16:
            num = grouper_card(from_num)
            return [name, num, num_2, name_2]
        else:
            num = grouper_account(from_num)
            return [name, num, num_2, name_2]
    else:
        return [0, 0, num_2, name_2]

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

def get_date_reverse(operation):
    date_ = (operation['date'].split('T'))[0].split('-')
    date_.reverse()
    return '.'.join(date_)



