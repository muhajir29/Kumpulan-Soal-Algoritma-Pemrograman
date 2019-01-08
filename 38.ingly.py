kata = input()
 
if kata[-3:] == "ing":
    print(kata + "ly")
elif len(kata) > 2:
    print(kata +  "ing")
else:
    print(kata)
