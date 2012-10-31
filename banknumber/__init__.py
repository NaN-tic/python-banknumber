#This file is part of banknumber. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Check the Bank code depending of the country
'''
__version__ = '1.0'

def countries():
    '''
    Return the list of country's codes that have check function
    '''
    res = [x.replace('check_code_', '').upper() for x in globals()
            if x.startswith('check_code_')]
    res.sort()
    return res

def check_code_es(number):
    '''
    Check Spanish Bank code.
    '''
    def get_control(ten_digits):
        valores = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6];
        valor = ten_digits
        control = 0;
        for i in range(10):
            control += int(int(valor[i]) * valores[i])
        control = 11 - (control % 11)
        if control == 11: 
            control = 0
        elif control == 10:
            control = 1
        return control;

    if len(number) !=20 or not number.isdigit():
        return False

    valor = '00'+ number[0:8]
    d1 = get_control(valor);
    if d1 != int(number[8]):
        return False

    valor = number[10:20]
    d2 = get_control(valor);
    if d2 != int(number[9]):
        return False

    return True

def check_code(account):
    '''
    Check Bank code.
    '''
    code = account[:2].lower()
    number = account[2:]
    try:
        checker = globals()['check_code_%s' % code]
    except KeyError:
        return False
    return checker(number)
