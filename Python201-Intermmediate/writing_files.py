with open ('writing_files.txt','w') as file :
  #^ w stands for write 
    file.write("Hello from  python 201")            

    #^ when we run this new file with writing_files.txt will appear and it will have content as HEllo from python 201

    #^ NOw what happens when we run this again?

    #^ so when you run it second time with Hello from python 201 second time ,it will replace the previous content 

    #^ what if you want to append to the previous content,you need to do as follows 

with open ('writing_files.txt','a') as file :

    #^ here a stands for append 
    file.write("\n A second line ")       
    file.write("\n\t A tabbed line ")            


    #^ \n is used for appending in new line and \t for tab







