#WAP to find total bill
VarName=input("Enter Consumer Name    : ")
VarNum=input("Enter Meter    Number  : ")
VarPrevious=int(input("Enter Previous Reading : "))
VarCurrent=int(input("Enter Current  Reading : "))
if(VarCurrent>VarPrevious or VarCurrent==VarPrevious):
    print("\tPress 1 for Print the Bill")
    print("\tPress 2 for Exit")
    input=input("Enter Your Input       : ")
else:
    print("\n\tEnter Valid values !!!")
Unit=VarCurrent-VarPrevious
Amount=80
if(Unit<101):
    AmountChange=Unit*3.44                                      # ex. unit = 20 then amountchange= 20*3.44 =68.8
elif(Unit<301 and Unit>100):
    AmountChange=344+(Unit-100)*7.34                            # ex unit = 150 then amountchange= 100*3.44 + 50*7.34 = 711
elif(Unit<501 and Unit>300):
    AmountChange=344 + 1468 + (Unit-300)*10.36                  # ex unit = 350 then amountchange= 100*3.44 + 200*7.34 + 50*10.36 = 2330
elif(Unit>500):
    AmountChange=344 + 1468 + 2072 +(Unit - 500)*11.82          
                                                                # ex unit = 550 then amountchange= 100*3.44 + 200*7.34 + 200*10.36 + 50*11.82= 4475
if(AmountChange>Amount):
    Amount=AmountChange
print("---------------------------------------------------------")
if(input=="1"):
    print("\t Total Electricity Bill")
    print("\t Nmae  of Cusumer    : ",VarName)
    print("\t Meter Number        : ",VarNum)
    print("\t Total Units  Used   : ",Unit)
    print("\t Total Amount to Pay : ",Amount)
elif(input=="2"):
    print("Enter Values Again")
print("---------------------------------------------------------")