while True:
     
    x=input('enter x value');
    y=input('enter y value');
    x=int(x);
    y=int(y);

    def add():
    
      print("addition=",x+y);

    def sub():
      print("sub=",x-y);

    def mult():
      print("multiplication=",x*y);

    def div():
      print("division=",x/y);

    add()
    sub()
    mult()
    div()

    another = input("Do you want to do another calculation? (yes/no): ")
    if another.lower() != 'yes':
       print("Exiting program!")
       break


