while 1:
    try:
        x, y = input("How much fuel is in the tank: ").split("/")
        x=int(x)
        y=int(y)
        x/y
        if x<0 or y<0 or x>y:
            print("Must be a fraction with two non-negative integers.")
            raise ValueError
    except ZeroDivisionError:
        print("The denominator cannot be zero.")
        continue
    except ValueError:
        print("Must be a proper fraction with non-negative integers.")
        continue
    else:
        break
if x/y >= 0.99:
    print("F")
elif x/y <= 0.01:
    print("E")
else:
    dec = round(100*x/y)
    print(f"{dec}%")
