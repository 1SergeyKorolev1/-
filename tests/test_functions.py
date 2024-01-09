import startPack
import tests
from utils import functions


def test_get_five_operations():
    assert len(functions.get_five_operations(startPack.operations)) == 5

def test_get_from():
    assert functions.get_from_and_to(tests.test_operation_1) == ['Maestro', '1596 83** **** 5199', '**9589', 'Счет']
    assert functions.get_from_and_to(tests.test_operation_2) == ['Счет', '**6952', '**6702', 'Счет']
    assert functions.get_from_and_to(tests.test_operation_3) == [0, 0, '**2431', 'Счет']
    assert functions.get_from_and_to(tests.test_operation_4) == ['Visa Classic', '6831 98** **** 7658', '8990 92** **** 5229', 'Visa Platinum']

def test_grouper_card():
    assert functions.grouper_card('7777777777777777') == '7777 77** **** 7777'

def test_grouper_account():
    assert functions.grouper_account('77777777777777777777') == '**7777'

def test_get_date_reverse():
    assert functions.get_date_reverse(tests.test_operation_3) == '23.03.2018'
