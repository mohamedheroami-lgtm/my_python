import string
alphabet = string.ascii_lowercase
pp = string.ascii_uppercase
massage = input("Enter the word....\n")
   
shift_u = int(input("Enter a shift number\n")) 
def crybet(word,shift):
    encrybtedcode = ""
    for i in word :
        if i in string.ascii_lowercase :
            position = alphabet.index(i)
            newposition = (position + shift_u )%26 
            encrybtedcode += alphabet[newposition]
        elif i in string.ascii_uppercase:
            position = pp.index(i)
            newposition = (position + shift_u )%26 
            encrybtedcode += pp[newposition]
            
        else:
            encrybtedcode += i    
    print(encrybtedcode)        
crybet(word=massage,shift=shift_u)
