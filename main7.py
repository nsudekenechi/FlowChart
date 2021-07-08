
print("Is it Raining")
choice=input()

if choice.lower()=='yes':
    print("Have an Umbrella?")
    choice = input()

    if choice.lower()=='yes':
        print("Go Outside")

    else:
        print("Wait a While")

        print("Is it Raining")
        choice1 = input()
        while choice1 == 'yes':
            print("Wait a While")
            print("Is it Raining")
            choice1 = input()
        else:
            print("Go Outside")











