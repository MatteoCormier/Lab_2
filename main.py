bin_num = int(input("Enter The Binary Number: \n")) #ask user to enter binary number
power = 0 #declare power as 0
dec_num = 0 #declare decimal number as 0
while bin_num > 0: #while the binary number is greater than zero
  dec_num += 2 ** power * (bin_num % 10) #convert a part of the binary number into a decimal number
  bin_num //= 10  #divide bin_num by 10 after every iteration
  power += 1     #increase power by 1 after every iteration
print("The Decimal Equivalent is: ",dec_num) #print the decimal number

# Task 2

text = input("Please enter a string seperated by '?'s between words: \n")

newtext = text.replace("?"," ")

wordcount = (text.count("?") + 1)

print (newtext,"\n The amount of words inputted is:" ,wordcount)