while True:
    print("Who are You? ")
    name=input();
    if name=='Joe':
        print('Hello,Joe. What is the password?(It is a fish.) ')
        password=input()
        if password != 'swordfish':
            break
        print('Access Granted.')

