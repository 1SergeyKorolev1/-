import json


def get_five_operations(operations_json):
    with open(operations_json, encoding='utf-8') as f:
        list_operation = json.load(f)

        def sort_(e):
            if e == {}:
                return tuple(map(int, [2019, 8, 26]))
            else:
                return tuple(map(int, (e['date'].split('T'))[0].split('-')))

        sorted_date = sorted(list_operation, key=sort_)
        five_last_operations = sorted_date[-5:]
        five_last_operations.reverse()
        return five_last_operations


def get_from_and_to(operation):
    to_num = operation['to'].split()[-1]
    if len(to_num) == 20:
        to_num_hide = grouper_account(to_num)
    else:
        to_num_hide = grouper_card(to_num)
    to_name = ' '.join(operation['to'].split()[:-1])
    if len(operation) > 6:
        from_num = operation['from'].split()[-1]
        if len(from_num) == 20:
            from_num_hide = grouper_account(from_num)
        else:
            from_num_hide = grouper_card(from_num)
        from_name = ' '.join(operation['from'].split()[:-1])
        return [from_name, from_num_hide, to_num_hide, to_name]
    return [0, 0, to_num_hide, to_name]


def grouper_card(iterable):
    list_ = []
    for i in range(0, 16):
        if i < 6 or i > 11:
            list_.append(iterable[i])
            if i == 3:
                list_.append(' ')
        else:
            list_.append('*')
            if i == 7 or i == 11:
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
