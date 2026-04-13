try:
    email=input("enter email")
    if "@" not in email or "."not in email:
         raise Exception("invalid email format")
    
    
    print("valid email")

except Exception as a :
     print("error",a)