def find_correct_position_brackets (str):
    copy_str = str[:]
    balance = 0

    if copy_str == '':
        return 'valid'
    
    for symbol in copy_str:
        if symbol in ['(', '{', '[']:
            balance += 1
        elif symbol in [')', '}', ']']:
            balance -= 1
    
    return 'valid' if balance == 0 else 'invalid'

print ('1: ' + find_correct_position_brackets('(())')) #valid
print ('2: ' + find_correct_position_brackets('')) #valid
print ('3: ' + find_correct_position_brackets('(()')) #invalid
print ('4: ' + find_correct_position_brackets(')(()')) #invalid
print ('5: ' + find_correct_position_brackets('(((')) #invalid

#TODO
print ('6: ' + find_correct_position_brackets('({)}')) #invalid
print ('7: ' + find_correct_position_brackets('[{()}]')) #valid
print ('8: ' + find_correct_position_brackets('{[(])}')) #invalid