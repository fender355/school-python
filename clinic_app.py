name=str(input("Please enter your name: "))

age=int(input("Please enter your age: "))

answer='wrong'

while answer=='wrong':

    exist=str(input("Are you a new or existing patient? (New/Existing): "))

    if exist.lower()=="new":
        exist="a new patient."
        answer="1"

    elif exist.lower()=="existing":
        exist="an existing patient."
        answer="1"

    else:
        print("Please follow the instrunctions.")

msg=f"We checked in a patient named {name}. He's {age} years old and is {exist}"

print(msg)