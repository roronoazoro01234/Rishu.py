A = int(input("A : "))
G = input("B : ")
if((A == 1 or A == 2) and G == "X"):
    print("fee is 100")
if((A == 3 or A == 4) and G == "Y"):
    print("fee is 200")
if((A == 5 and G == "Z")):
    print("fee is 300")
else:
    print("no fee") 