good_credit= True
price=1000000

if good_credit:
    down=price*0.1

else:
    down=price*0.2

print(f"The down payment you need to pay is ${down}.")