name=input("Enter Name ")

if name=='Alice':
    print("Hi ",name)
else:
    age=int(input("Enter Age "))
    if age < 12:
        print("You are not alice,Kiddo")
    elif age > 2000:
        print("Unlike you, Alice is not an undead,immortal Vampire")
    elif age >100:
        print('You are not Alice,grannie')