#say hello and ask the name of the user //this hastag is used to comment the line 
#pseudo code:helps us to explain or perform any code of line in very structured way 
#ask user for their name
name=input("what is your name ? ")
#say hello to the user 
#print("hello,",end=" ")
#end=" ":combines the next line with the previous one 
#print("hello,", name, sep="  ")
#sep=" "----this bacically stands for seperator which seperates strings in a line 
#print(name)
#STR=strig--basically a string is a sequence of text.
#------------------------------------------------------------
name=name.strip().title()#white space ko hata dega.
#bascially it removes the white space from the string and capitalize users name


#capitalize name of the user
name=name.capitalize()
name=name.title()#only very first letter

print("hello,", name)

