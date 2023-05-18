filename = input("Whats is the file name ? :")
content = input("Enter the content : ")

with open(filename,'w') as file :
    file.write(content)

open_file = input("Would you like to read this file ?")

if open_file  in ['y','n']:
    if open_file == 'y':
        with open(filename,'r') as file:
            print(file.read())

#^ it will create file with whatever filename you give and write inside the content,whatever you provide it with 
#^ and then ask with user if you want to open the file and then open or show the content inside the file 