
def student(**kwagrs):
    for key,value in kwagrs.items():
        print(key,":",value)
student(name="Ariz",age=22,course="data science")


# def result(**kwagrs):
#     for s in kwagrs.items():
#         print(s)

# result(Python=90,Java=80,MySQL=85)