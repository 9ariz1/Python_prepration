import datetime
import os
lst=os.listdir()
pahle=datetime.datetime.now()
for file in lst :
    print(file)
print(pahle)
print(datetime.datetime.now()-pahle)