
#^ suppose in a file with list of email i want to find out if kalob@gmail.com is there or not ?

with open('emails.txt','r') as emails:
  print(emails.readlines())  

  #^ this will print all the emails in the file in an --->  array,we can now work with an array also point to note is its adding \n at the end of every email
  #['email1@gmail.com\n', 'email2@gmail.com\n', 'kiara@gmail.com\n', 'email3@gmail.com\n', 'email4@gmail.com\n', 'jogga@gmail.com\n', 'kittu@gmail.com\n', 'kalob@gmail.com\n', 'gully@hotmail.com\n']
with open('emails.txt','r') as emails:
    emails = emails.readlines()

for email in emails:
   if "email" in email:
      print(email.rstrip())

      #^ without rstrip we were getting new lines added after every email list ,and to get rid of that we used r strip 
      #^ The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.


