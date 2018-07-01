while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("Bad user! You did not provide a valid integer! Please try again ...")
print("Good job. You are a nice obedient user.")
