brackets = {
        "(": ")",
        }

def find_correct_position_brackets (str):
    copy_str = str[:]
    
    if copy_str == '':
        return 'valid'
    
    while copy_str != '':

        if copy_str[0] == "(":

            if copy_str.find(")") != -1:
                copy_str = copy_str.replace("(", '', 1)
                copy_str = copy_str.replace(")", '', 1)

            else:
                return "invalid"
            
        else:
            return "invalid"
                
            
    return "valid"

print (find_correct_position_brackets('(())')) #valid
print (find_correct_position_brackets('')) #valid
print (find_correct_position_brackets('(()')) #invalid
print (find_correct_position_brackets('())')) #invalid
print (find_correct_position_brackets(')(()')) #invalid
print (find_correct_position_brackets(')))')) #invalid
print (find_correct_position_brackets('(((')) #invalid