from flask import Flask, request, redirect, render_template, session
from flask.json import jsonify
import os

app = Flask(__name__)

# convert transaction Hach to a 6 base

def reVal(num): 
  
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0'))
    else: 
        return chr(num - 10 + ord('A'))
  
# Utility function to reverse a string 
def strev(str): 
  
    len = len(str)
    for i in range(int(len / 2)): 
        temp = str[i]
        str[i] = str[len - i - 1]
        str[len - i - 1] = temp
  

def fromDeci(res, base, inputNum): 
  
    #index = 0 Initialize index of result 
  
    # Convert input number is given base  
    # by repeatedly dividing it by base  
    # and taking remainder 
    while (inputNum > 0): 
        res+= reVal(inputNum % base)
        inputNum = int(inputNum / base)
  
    # Reverse the result 
    res = res[::-1]
  
    return res
  
# Driver Code 
#convert hach of a transaction to 6 base
Hash=0x755e1278c22c92c4ea0b5a44b3dd52a8a84ca59531849d0e279c84eb289da8f2
Hash_in_dec = int(Hash[1:],16)
base = 6 
res = ""
Hash_in_dec_list=str(fromDeci(res, base, Hash_in_dec))

# address of transaction converted to decimal
address_bradg=0xfff923f5a1016e422ddb5d5b7d3ef8152957d2a5
address1=int(address_bradg[1:], 16)

# write in text file note using the disposition from Hash_in_dec_list and note number from address

Hash_in_dec_list=[int(i) for i in str(list)]

j=0
while j < len(Hash_in_dec_list):
    with open("note.txt",'r+') as f:
        line = f.readlines()
        note=""
        f.seek(0)
        for index,line in enumerate(line):
            if index==Hash_in_dec_list[j]:
                note+=line.strip()+ str(address1[j])+'\n'
            else: 
                note+=line.strip()+ '-\n'
        f.write(note)
    f.close()   
    j+=1

# import Hash from javascrypt web page 


@app.route('/', methods=['POST'])
def postmethod():
    TxHash = request.get_json()
    print(TxHash)
    return jsonify()
    
