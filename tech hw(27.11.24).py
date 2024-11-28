name=input("Enter name:") 
roll_no=int(input("Enter roll number:")) 
a=int(input("Enter the marks obtained in subject 1:")) 
b=int(input("Enter the marks obtained in subject 2:")) 
c=int(input("Enter the marks obtained in subject 3:")) 
totalmark=a+b+c 
per=(totalmark/300)*100 
if per>=85: 
 print("Grade S") 
elif per>=75: 
 print("Grade A") 
elif per>=65: 
 print("Grade B") 
elif per>=55: 
 print("Grade C") 
elif per>=50: 
 print("Grade D") 
else: 
 print("Fail") 
