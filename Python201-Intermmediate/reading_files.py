
# ^ with open('filename','r') as file:          /// r stand for read 
#^     print(file.read())

with open('README.md','r') as ctx   :   
 #^ in place of ctx you can just write file or something with f string it doesnt matter, it is just a variable name
    print(ctx.read())

#^ now if  you run tis file inside the terminal ,it will display all that is insdie the mentioned file 


with open('README.md','r') as ctx   :   
    pass

print(ctx.read())

#^ this will give an error 
#^ when you are reading file with WITH keyword ,simply means we dont have access to the file ,outside of that indentation of with keyword,so error -as on line 13 ,file is closed,as indentation is closed  and we need to not worry of closing the file .

#^ if we want the context of the file to be closed in the variable that is accessible to ,outside of the with keyword indentation ,we can say 

with open('README.md','r') as ctx   :   
    content = ctx.read()
print("The content is : ",content)


#^ now we have acces to entire content outside the contaxt manager that we open with with keyword 

#^ now why is that imp ,becoz we have a context manager ,we store the contents of the file in a variable called content ,and then behind the scenes ,python close this file,it did for us ,so its not using too much memory ,tryign to be as efficient as possible ,becoz lot of people forget to close their file,this is a safe way to do it and then we can access that content variable outside od context manager 