import datetime as dt

sub=[]
def billing_system(**customer):
    print("\n ------Customer Bill--------")
    for key1, value1 in customer.items():
        print(f"{key1}:{value1}")

    print("\n----------------------------------------------------------------\n")
    print("Itemized Details:")
    item_stats={"Milk":[5,30],"Oats":[2,110],"Rice":[3,100],"Silk":[5,65]}
    for key2, value in item_stats.items() :
        print(f"{key2}               Qty:{value[0]}             Price:{value[1]}             Total:{value[0]*value[1]}")
        sub.append(value[0]*value[1])


    def calculate_bill():
        subtotal=sum(sub)
        tax=subtotal*0.18
        total=subtotal+tax
        return subtotal, tax, total
    
    subtotal, tax, total = calculate_bill()

    print("\nSubtotal:",subtotal)
    print("Tax(%) :",tax)
    print("Total Amount to Pay:",total)
    print("----------------------------------------------------------------------")
    for key1, value1 in customer.items():
        print(f"{key1}:{value1}")


billing_system(Name="Aryan",Contact="7895643562",Payment="UPI", Data=dt.datetime.now())