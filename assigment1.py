costprice=float(input("enter the cost price"))
sellprice=float(input("enter the selling price"))
if sellprice>costprice:
    print("profit")
elif sellprice<costprice:
    print("loss")
else:
    print("niether")