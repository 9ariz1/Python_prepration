'''
Create and existing dictionary and take a word as input form user and find the meaning of that word in dictionary (handle Keyerror)
'''
dict={'1': 'Ariz', 
      '2': 'python',
      '3': '9305178391', 
      '5': 'data science', 
      '4': 'integral university'
}
word=input("Enter a key to find its value : ")
try:
    print("The meaning of the word is :",dict[word])
except KeyError:
    print("Sorry, the word is not found in the dictionary.")
finally:
    print("Dekho Shi HAi")