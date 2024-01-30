
text = 'Test 1 2 3'
text_lst = [char.upper() for char in text]
print (text_lst)



text2 = ' COMP 216 is a netwroking course for software students'

vowel = 'aeiou'

vowel_list = [char.lower() for char in text2 if char in vowel]

print(vowel_list)


vowel_set = {char.lower() for char in text2 if char in vowel}
print(vowel_set) 

values = [ 1 ,2 ,3 ,4, 5]
new_dict= {num: chr(num) for num in values}
print (new_dict)