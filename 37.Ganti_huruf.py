string = input()
 
 
nilai =''
for i in string[1:]:
    if string[0] != i:
        nilai += i
    else:
        nilai += "_"
print(string[0]+nilai)
