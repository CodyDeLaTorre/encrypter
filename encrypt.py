import random

item_to_encrypt = input("Give me a string to encrypt...")


def encrypter3000(item_to_encrypt,n):
    additive = str(random.randint(0,1000))
    additive2 = str(random.randint(0,1000))
    additive3 = str(random.randint(0,1000))
    ans = " "
    for i in range(len(item_to_encrypt)):
        ch = item_to_encrypt[i]
        
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return additive + ans + additive2 + additive3

print(encrypter3000(item_to_encrypt,random.randint(1,20)))
