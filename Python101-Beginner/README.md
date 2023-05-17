

# 1)Executing Python Code 


suppose 

print("helloworld hahahahahah ")

is written in vs code or any other editor 

// Through Terminal Method :
    there you need to type 
    there you need to type 
To run the code and see ,you need to open the terminal (terminal can be any ex vs code or cmd etc )
,there you need to type 

    python filename
    ex:python helloworld.py

you will get to see the result in terminal as 


      helloworld hahahahahah


# 2)Basic Arithmetic 

in terminal you need to type the python first (path should be correct ex:/Desktop or whereever your file is etc .)

then you willsee the version name as follows 
        
        Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

after this you can write your basic arithmetic commands and hit enter ,you will be able to see the result ,examples ->

                >>> 5 + 5
                10
                >>> 99-11
                88
                >>> 4 *4
                16
                >>> 100/25
                4.0
                >>> 4**4            // 4 power 4
                256


suppose you typed something wrong and error came up as follows 
              
                >>> ddddd
            Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            NameError: name 'ddddd' is not defined

so ,in this case you can press ctrl+L and you  can continue further 

            >>> ^L
            >>>
# 3)Introduction to variables in Python(variables.py) and FOrmatting code in the Python(indentation.py)

variables -its jus a little piece of memory aloocated to a named association 

ncourse = "Python 101"
python works on new lines and the indentation,it doesnt need the semicolon 
    a) # no semicolon its fine 
    b)it works on new lines  and indentation
    c)#when it comes to function ,we will see ,if something == "something else":# here we dont need to worry about the curly spaces,instead we use colon : and write next lines and if we have no code inside function ,we simply write in next line as pass
                       
                        if something == "something else":              
                             pass 
 d) #after colon indent is neccessary ,else you will get error -syntax error ,but if you are declaring a variable and there before you give the indentation then also you will get the error for indentation
 e)In conclusion ,indetation after function or condition is mandatory and indentation before var declaration will give error
 f)whenever you want to end the code after function code etc ,you simply unindent 
 g)Indentation is very imp in python -note it 


 # 4)Code Comment (coment.py)and Intro to python data type (data_types.py)


a)comments are being doen by putting # sign and then followed by our message ,they are great for sharing thoughts and writing infos for ourselves and for other developers ,comments are not executable 
b)#TODO:do a thing her (this is also a kind of comment ,to let you reming what you want to do in fututre ,if nt working then you may be needing the extension TOO tree)

a-a)string = "A sentence"       # its basically a sentence inside " " or '',and this allows any form of sentence or characters that just not a number or decimal 
b-b) integers = 99 #whole numbers 
c-c) floats = 3.14 #whole numbers witht the decimals 
d-d) list = ["Item1","Item2","3","5.5"]      
e-e) tuple = ("Item 1",floats ,integers )          # its something we cant change it ,once its settled its settled 
f-f) sets  ={"Item1","Item2","Item3"}     # they are lot like a list as well,but uses curly braces and they will not maintain their order of the listing ,so whenever we are going to access the sets in the future it may come out as item 3 first and randomlisting 
g-g) dictionary = {
    "key": "value",
    "key2": "value 2",
}
h-h) booleans = True # or False    (it should be CAPS T and F)
i-i) none = None 



