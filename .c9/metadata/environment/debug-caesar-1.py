{"filter":false,"title":"debug-caesar-1.py","tooltip":"/debug-caesar-1.py","undoManager":{"mark":45,"position":45,"stack":[[{"start":{"row":1,"column":0},"end":{"row":1,"column":23},"action":"remove","lines":["Your module description"],"id":1},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["R"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["i"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["c"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["a"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":[" "],"id":2},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["C"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["e"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["r"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["c"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["e"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["r"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["e"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":[" "],"id":3},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["I"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["b"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["a"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["r"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["r"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["a"]}],[{"start":{"row":1,"column":24},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["#"],"id":6}],[{"start":{"row":4,"column":1},"end":{"row":4,"column":66},"action":"insert","lines":["Exercise 1: Working with the buggy Caesar cipher program - Part 1"],"id":7}],[{"start":{"row":4,"column":66},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":5,"column":0},"end":{"row":7,"column":183},"action":"insert","lines":["In the Functions lab, you created a Caesar cipher program to encrypt and decrypt a message. In this lab, you will use the Python Debugger (pdb) to find and fix errors in buggy versions of the program.","","From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section. Copy the following code and paste it in the file:"],"id":9}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["#"],"id":10}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["#"],"id":11}],[{"start":{"row":5,"column":201},"end":{"row":6,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":6,"column":184},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":63,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #1","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + cipherKey","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":14}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["\"\""],"id":15}],[{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["\""],"id":16}],[{"start":{"row":3,"column":3},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["\"\""],"id":18}],[{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["\""],"id":19}],[{"start":{"row":64,"column":24},"end":{"row":65,"column":0},"action":"insert","lines":["",""],"id":20}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["\"\""],"id":21}],[{"start":{"row":65,"column":2},"end":{"row":65,"column":3},"action":"insert","lines":["\""],"id":22}],[{"start":{"row":65,"column":3},"end":{"row":66,"column":0},"action":"insert","lines":["",""],"id":23}],[{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["\"\""],"id":24}],[{"start":{"row":66,"column":2},"end":{"row":66,"column":3},"action":"insert","lines":["\""],"id":25}],[{"start":{"row":65,"column":3},"end":{"row":66,"column":0},"action":"insert","lines":["",""],"id":26}],[{"start":{"row":66,"column":0},"end":{"row":68,"column":91},"action":"insert","lines":["The program ends in a traceback. A traceback is a stack trace that starts from the point of an exception handler. It then goes down the call chain to the point where the exception was raised. In other words, an error occurred.","","Use the debugger to find and fix the bug in the first lab file for the buggy Caesar cipher."],"id":27}],[{"start":{"row":64,"column":24},"end":{"row":65,"column":0},"action":"insert","lines":["",""],"id":28}],[{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"insert","lines":["i"],"id":29},{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"insert","lines":["n"]},{"start":{"row":36,"column":35},"end":{"row":36,"column":36},"action":"insert","lines":["t"]},{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"insert","lines":["("]}],[{"start":{"row":36,"column":46},"end":{"row":36,"column":47},"action":"insert","lines":[")"],"id":30}],[{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"remove","lines":["("],"id":31}],[{"start":{"row":36,"column":35},"end":{"row":36,"column":36},"action":"remove","lines":["t"],"id":32},{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"remove","lines":["n"]},{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"remove","lines":["i"]}],[{"start":{"row":36,"column":42},"end":{"row":36,"column":43},"action":"remove","lines":[")"],"id":33}],[{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"insert","lines":["i"],"id":34},{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"insert","lines":["n"]},{"start":{"row":36,"column":35},"end":{"row":36,"column":36},"action":"insert","lines":["t"]},{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"insert","lines":["("]}],[{"start":{"row":36,"column":46},"end":{"row":36,"column":47},"action":"insert","lines":[")"],"id":35}],[{"start":{"row":36,"column":47},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":37,"column":0},"end":{"row":37,"column":8},"action":"insert","lines":["        "]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["#"]},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["e"],"id":37}],[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":[" "],"id":38},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["l"]},{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["a"]}],[{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"remove","lines":["a"],"id":39},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"remove","lines":["l"]}],[{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["f"],"id":40},{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["a"]},{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"insert","lines":["l"]},{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["t"]},{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"insert","lines":["a"]},{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"insert","lines":["b"]},{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"insert","lines":["a"]}],[{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"insert","lines":[" "],"id":41},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["e"]},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["l"]},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":[" "]},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["I"]},{"start":{"row":37,"column":24},"end":{"row":37,"column":25},"action":"insert","lines":["N"]},{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"insert","lines":["T"]}],[{"start":{"row":37,"column":26},"end":{"row":37,"column":27},"action":"insert","lines":[" "],"id":42},{"start":{"row":37,"column":27},"end":{"row":37,"column":28},"action":"insert","lines":["a"]},{"start":{"row":37,"column":28},"end":{"row":37,"column":29},"action":"insert","lines":["l"]},{"start":{"row":37,"column":29},"end":{"row":37,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"insert","lines":[" "],"id":43}],[{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"remove","lines":[" "],"id":44},{"start":{"row":37,"column":29},"end":{"row":37,"column":30},"action":"remove","lines":["s"]}],[{"start":{"row":37,"column":29},"end":{"row":37,"column":30},"action":"insert","lines":[" "],"id":45},{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"insert","lines":["C"]},{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"insert","lines":["y"]},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"insert","lines":["p"]},{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"remove","lines":["e"],"id":46},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"remove","lines":["p"]},{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"remove","lines":["y"]}],[{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"insert","lines":["i"],"id":47},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"insert","lines":["p"]},{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"insert","lines":["h"]},{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"insert","lines":["e"]},{"start":{"row":37,"column":35},"end":{"row":37,"column":36},"action":"insert","lines":["r"]},{"start":{"row":37,"column":36},"end":{"row":37,"column":37},"action":"insert","lines":["K"]},{"start":{"row":37,"column":37},"end":{"row":37,"column":38},"action":"insert","lines":["e"]},{"start":{"row":37,"column":38},"end":{"row":37,"column":39},"action":"insert","lines":["y"]}]]},"ace":{"folds":[],"scrolltop":334.10000000000053,"scrollleft":0,"selection":{"start":{"row":37,"column":39},"end":{"row":37,"column":39},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":22,"state":"start","mode":"ace/mode/python"}},"timestamp":1696994225499,"hash":"8e8c9a364336c0aeecd045c1328a85159c1bf841"}