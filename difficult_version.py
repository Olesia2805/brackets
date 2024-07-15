brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
        }

def find_correct_position_brackets (str):
    copy_str = str[:]
    
    if copy_str == '':
        return 'valid'
    
    while copy_str != '':
        symbol = copy_str[0]

        if symbol in brackets.keys():
            couple = brackets[symbol]

            if copy_str.find(couple) != -1:
                copy_str = copy_str.replace(symbol, '', 1)
                copy_str = copy_str.replace(couple, '', 1)

            else:
                return "invalid"
            
        else:
            return "invalid"
                
            
    return "valid"

print ('1: ' + find_correct_position_brackets('(())')) #valid
print ('2: ' + find_correct_position_brackets('')) #valid
print ('3: ' + find_correct_position_brackets('(()')) #invalid
print ('4: ' + find_correct_position_brackets(')(()')) #invalid
print ('5: ' + find_correct_position_brackets('(((')) #invalid


#TODO
print ('6: ' + find_correct_position_brackets('({)}')) #invalid
print ('7: ' + find_correct_position_brackets('[{()}]')) #valid
print ('8: ' + find_correct_position_brackets('{[(])}')) #invalid
print ('9: ' + find_correct_position_brackets('({]}')) #invalid