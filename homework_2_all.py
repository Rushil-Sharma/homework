import time
x = 0
print("First (input) natural numbers")
nat = int(input("How many number(/s) ? :- "))
for x in range (nat):
    x=x+1
    print(x)
print("############################# second:- ")
print("Printing 1\n12\n123\n1234\n12345\nWith for loops")
time.sleep(5.0)
for i in range(1,7):
        for j in range(1,i):
            print(j,end="")
            j+=1
        i+=1
        print("\n")
print("######################## third :- ")
print("using inputs printing the sum of all the number's from 0 \nExample:-(input = 4 output = '1+2+3+4 = '10)")
time.sleep(5.0)
fgh = int(input("enter a number:-  "))
lol = 0 
for i in range(1,fgh+1): 
	lol += i 
print(lol) 
print("####################### fourth:-")
print("Printing the table of (input)\nFrom x 1 to x 10")
time.sleep(5.0)
v = int(input("Enter a number :-   "))
print("your number is  :-",v)
b = 10
for c in range(b+1):
    sol = c*v 
    print(v,"x",c,"=",sol)
print("######################### fifth :-")
print("Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration")
time.sleep(5.0)
xyz = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
idk = 0
print(xyz,"\nThe numbers divisable are")
for idk in range(10):
    if xyz[idk]%5 == 0:
        print(xyz[idk])
    else:
        print("______")
    idk = idk + 1
print("######################### sixth :-")
print("""Given a number count the total number of digits in a number Print the following pattern using for loop
54321
4321
321
21
1""")
time.sleep(5.0)
v1v2 = 5
for row in range(v1v2,0,-1):
    for col in range(1,row+1): 
        print(col,end="")
    print()
print("######################### seventh :-")
time.sleep(5.0)
dfg = 0
for i in range (10):
    dfg = dfg - 1
    print(dfg)  