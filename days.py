from datetime import datetime , timedelta
def f(y):
    x = datetime.now()
    y = datetime.strptime(y,"%d-%m-%Y")
    z = x-y
    exclu_fry = 0
    for i in range (z.days +1):


        day =y+timedelta(days=i)
        if day.weekday() != 4:

         exclu_fry += 1

    return exclu_fry
    

s= input("start date (DD-MM-YY)")
print (f(s))
