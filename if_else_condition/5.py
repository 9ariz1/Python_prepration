# wap in py to read the temperature in centigrate and display a suitable message according to the temperature 
# state below:
# temp <0 then freezing weather 
# temp 0-10 then very cold weather 
# temp 11-20 then cold weather 
# temp 21-30 then normal in temp
# temp 31-40 then its Hot
# temp > 40 then its Very hot

a=int(input("Enter temprature : "))
if a<0 :
    print("The weather is freezing")
elif a>0 and a<=10 :
    print("The weather is very cold")
elif a>10 and a<=20:
    print("The weather is cold")
elif a>20 and a<=30 :
    print("The weather is normal")
elif a>30 and a<=40 :
    print("The weather is Hot")
else :
    print("The wether is very hot")