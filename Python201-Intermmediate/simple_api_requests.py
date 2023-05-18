import requests

req = requests.get("https://kalob.io")
print(req.status_code)

answer : 200
200 status code means the site is up and running

#^ Now at this point you can make the site monitoring program quite easily 

# import requests
# import time 
# while True:
#     req = requests.get("https://kalob.io")
#     print(req.status_code)
#     if req.status_code!= 200:
#         #Email me or text me using twilio api or something
#         pass 
#     time.sleep(3)

#^ so every second this is going to make a request and if yourun it will constantly saying 200 every 3 sec 
