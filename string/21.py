sentence=input(" Enter A  line : ").lower()

replace_what=input("Replace what ?? - ").lower()
replace_with=input("Replace with ?? - ").lower()

new=sentence.replace(replace_what,replace_with)
print(sentence)
print(new)