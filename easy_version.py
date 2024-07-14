def find_correct_position_brackets (str):
    copy_str = str[:]

    if copy_str == '':
        return 'valid'
    
    return 'valid'

print (find_correct_position_brackets('(())')) #valid
print (find_correct_position_brackets('')) #valid
print (find_correct_position_brackets('(()')) #invalid
print (find_correct_position_brackets('())')) #invalid
print (find_correct_position_brackets(')(()')) #invalid
print (find_correct_position_brackets(')))')) #invalid
print (find_correct_position_brackets('(((')) #invalid