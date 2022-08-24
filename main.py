from sys import argv
from time import sleep

from env import *

from test_cases.test_case_3_find_token import check_token


if __name__ == '__main__':
    try:
        testcase_name: str = argv[1]
    except Exception:
        raise Exception('You\'re retard! Testcase argument is required!')

    if testcase_name == 'testcase_3':
        timeout: int = 3_600

        while 1:
            print(f'Starting \"{testcase_name}\".')

            check_token()

            print(f'End \"{testcase_name}\".\nSleeping in \"{timeout}\" sec...')

            sleep(timeout)
    elif testcase_name == 'testcase_2':
        pass
    elif testcase_name == 'testcase_1':
        pass
    else:
        print(f'Testcase with the name \"{testcase_name}\" not found. Exiting...')
