def find_correct_position_brackets (str):
    copy_str = str[:]
    
    if copy_str == '':
        return 'valid'
    
    while copy_str != '':
        if ('()') in copy_str:
            copy_str = copy_str.replace('()', '')
        elif ('[]') in copy_str:
            copy_str = copy_str.replace('[]', '')
        elif ('{}') in copy_str:
            copy_str = copy_str.replace('{}', '')
        else:
            return 'invalid'
            
    return 'valid'

print (f'1 - (()): {find_correct_position_brackets('(())')}') #valid
print (f'2 - "": {find_correct_position_brackets('')}') #valid
print (f'3 - ((): {find_correct_position_brackets('(()')}') # invalid
print (f'4 - )((): {find_correct_position_brackets(')(()')}') #invalid
print (f'5 - (((: {find_correct_position_brackets('(((')}') #invalid
print (f'6 - ))): {find_correct_position_brackets(')))')}') #invalid

print ('7 - [{()}]: ' + find_correct_position_brackets('[{()}]')) #valid
print ('8 - {[(])}: ' + find_correct_position_brackets('{[(])}')) #invalid
print ('9 - ({]}: ' + find_correct_position_brackets('({]}')) #invalid
print ('10 - ({)}: ' + find_correct_position_brackets('({)}')) #invalid