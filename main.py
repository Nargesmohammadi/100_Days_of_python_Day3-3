year = int(input("witch year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("loap year")
        else:
            print("not loap year")
    else:
        print("not loap year")
else:
    print("not leap year")
