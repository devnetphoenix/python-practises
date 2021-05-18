text = input("Enter message : ")
shift = int(input("enter the shift : "))
def encrypt(text,shift): 
    result = "" 
   
    for i in range(len(text)): 
        char = text[i] 
   
        if (char.isupper()): 
            result += chr((ord(char) + shift-65) % 26 + 65) 
   
        else: 
            result += chr((ord(char) + shift - 97) % 26 + 97) 
  
    return result

print("your Cipher text : " + encrypt(text,shift))

text2 = input("enter the message to decrypt :")

def decrypt(text2,shift):
    result1 = ""

    for i in range(len(text2)):
        char = text2[i]

        if(char.isupper()):
            result1 += chr((ord(char) - shift-65) % 26 + 65)

        else:
            result1 += chr((ord(char) - shift-97) % 26 + 97)

    return result1

print("you decrypted message is : " + decrypt(text2,shift))

		 

	 

