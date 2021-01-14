from cryptography.fernet import Fernet



def encrypt_text(text):
    
    key=Fernet.generate_key()
    
    print("Your secret key is:",key.decode('ascii'))
   
    b = bytes(text, 'utf-8')
    
    f=Fernet(key)
    
    print()
    
    token=f.encrypt(b)

    print("Your encrypted text is:",token.decode('ascii'))
   
def decrypt_text(key,text):
    k=bytes(key, 'utf-8')
    b = bytes(text, 'utf-8')
    f=Fernet(k)
    
    dec=f.decrypt(b)

    print("Your decrypted text is:",dec.decode('ascii'))
    
    
print("Enter text:")
text=(input())
print()
print("For encryption,press 1.\nFor decryption press 2:")
enorde=int(input())


if enorde==1:
    encrypt_text(text)
else:
    print("Enter Secret Key:")
    secret_key=input()
    print()
    decrypt_text(secret_key,text)
