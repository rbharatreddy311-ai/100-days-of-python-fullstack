'''
BMI usecase --> BMI(Body Mass INdex)

weight--> kgs
height--> metres
feet-->12 inches-->inch-->2.54cm

BMI=(weigth)/((height)**2))

store_re=[]
no_of_=int(input("enter a value"))
for i in range(no_of_):
    weight=float(input("enter the weight in kgs"))
    height=float(input("enter the height in metres"))
    name=input("enter the user name")
    bmi=(weight)/((height)**2)
    store_re.extend([name,weight,height])
    if weight>0 and height>0:
        print(bmi)
        if bmi<18.5:
            print("Under weight")
        elif 18.5<=bmi<=24.9:
            print("Normal weight")
        elif 25<=bmi<=29.9:
            print("Over weight")
        else:
            print("obesity") 
    else:
        print("make sure to enter a positive nubber")
print(store_re)
'''

while True:
    weight=int(input("enter the weight in kgs"))
    height=float(input("enter the height in meters"))
    name=input("enter the name")
    try:
        if weight >0 and height>0:
            break
        else:
            name=input("enter the user name")
            bmi=(weight)/((height)**2)
            if weight>0 and height>0:
                print(bmi)
                if bmi<18.5:
                    print("Under weight")
                elif 18.5<=bmi<=24.9:
                    print("Normal weight")
                elif 25<=bmi<=29.9:
                    print("Over weight")
                else:
                    print("obesity") 
            else:   
                print("make sure to enter a positive nubber")
        

            
