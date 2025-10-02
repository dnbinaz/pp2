def check_palin (str):
    for i in range (0, int(len(str)/2)):
        if str [i] != str[len(str)-i-1]:
            return False 
        return True

str1 = input()
ans = check_palin(str1)
if (ans):
    print("Yes")
else:
    print("No")