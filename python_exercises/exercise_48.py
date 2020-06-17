# Enter Your PIN

pin = 1234

print("WELCOME TO THE BANK OF MITCHEL.")
entry = int(input("ENTER YOUR PIN: "))

while (entry != pin):
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: "))

print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
