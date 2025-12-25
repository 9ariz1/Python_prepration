# Count frequency of characters using dictionary.
s=input("Enter a string: ").lower()
freq={}

for ch in s:
    if ch !="." and ch!=" ":
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
for k,v in freq.items():
    print(f"{k} : {v}")
