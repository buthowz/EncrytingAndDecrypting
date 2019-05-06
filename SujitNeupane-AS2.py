print("Sujit Neupane")
print("Oct 8, 2018")
print("Assignment 2")
print("---------------------------")

#
# A
#

def GF2_addBit(b1,b2):
    if (b1 == b2):
        return '0'
    else:
        return '1'

#
# B, C
#

def addTwoBitsNew(a,b):
    c = ""
    for i in range(len(a)):
        c += GF2_addBit(a[i],b[i])  
    return c
    
   
def GF2_addWord(w1,w2):
    length = len(w1)
    bound = range(length)
    
    for i in bound:
        print('\n' + w1[i] + ' : ')
        for j in range(i,length):
            c = addTwoBitsNew(w1[i],w2[j])
            print('\t' + w1[i] + ' + ' + w2[j] + ' = ' + c)
    print('\n ==== Done ====')

#
# E,F
#

endingMessage = ['10000', '00000', '00000', '01000', '11010', '00000', '01000', 
     '10111', '00110', '11111', '01001', '01000', '11001', '11010', 
     '11111', '10110', '10010', '00011', '01000', '10010', '11001', 
     '10100', '10110', '10011', '00011', '10010', '01000', '10000',
     '10010', '11111', '01000', '10010', '11001', '00000', '11100', 
     '01000', '10011', '10110', '01000', '10111', '00110', '11111', 
     '01111', '01000', '00001', '10101', '11010', '00000', '01000', 
     '10000', '11001', '10010', '00000', '00000', '01000', '11010', 
     '00000', '01000', '10111', '00110', '11111', '01110', '01000']
def userInteraction():
        plainText = input('Please enter your message: ')
        if (len(plainText) != 0):
            code = input('Please enter your 5 bit code: ')
            print("This is the coded message: ")
            print(encode(plainText,code))
        while (len(plainText) != 0): 
            plainText = input('Please enter your message: ')
            if (len(plainText) != 0):
                code = input('Please enter your 5 bit code: ')
                print("This is the coded message: ")
                print(encode(plainText,code))
        else:
            print("Thanks for playing!! See you soon. Bye")
            decode(endingMessage)
       

def createDictionary():
    i = 65
    myDict = {}
    for x in range(26):
        myDict[chr(i)] = '{0:05b}'.format(x)
        i+=1
    myDict[" "] = "11010"
    myDict["."] = "11011"
    myDict["!"] = "11100"
    myDict[","] = "11101"
    myDict["?"] = "11110"
    myDict[":"] = "11111"
    return myDict

def getValue(key):
    c = createDictionary()
    return c[key]

def encode(plainText,code):
    c = []
    for x in range(len(plainText)):
        bitForLetter = getValue(plainText[x])
        encodedBit = addTwoBitsNew(bitForLetter,code)
        c.append(encodedBit)
    return c

#
# D
#

def decode(listOfBits):
    c = createDictionary()
    d = {c[key]:key for key in c}
    keysList = [x for x in d.keys()]
    a = []
    for i in range(len(keysList)):
        printKey = "Key = " + keysList[i]
        ans = ""
        for j in range(len(listOfBits)):
            codedBits = addTwoBitsNew(listOfBits[j],keysList[i])
            matchDict = d.get(codedBits)
            ans += matchDict
        print(printKey + " ==> " + ans)

                  
def main():
    a1 = ['0', '1']
    b1 = ['0', '1']
    a2 = ['00', '01', '10', '11']
    b2 = ['00', '01', '10', '11']
    a3 = ['000', '001', '010', '011', '100', '101', '110', '111']
    b3 = ['000', '001', '010', '011', '100', '101', '110', '111']
    print("Answer for A, B, and C: ")
    print("Test results for 1 bit")
    GF2_addWord(a1,b1)

    print("\nTest results for 2 bits")
    GF2_addWord(a2,b2)

    print("\nTest results for 3 bits")
    GF2_addWord(a3,b3)
    example = ['10101', '00100', '10101', '01011', '11001', '00011',
               '01011', '10101', '00100', '11001', '11010']
    print("\nD. \nDecoding coded message from the book:\ndecoding...")
    decode(example)

    print("\nE. ")
    message = "THIS IS BORING! NOT FUN AT ALL."
    key = "01010"
    print("Message: " + message)
    print("Key: " + key)
    print("This is the coded message: ")
    print(encode(message, key))

    print("\nF. ")
    userInteraction()

   
   
main()


    
