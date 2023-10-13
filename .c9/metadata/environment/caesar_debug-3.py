{"filter":false,"title":"caesar_debug-3.py","tooltip":"/caesar_debug-3.py","undoManager":{"mark":25,"position":25,"stack":[[{"start":{"row":1,"column":0},"end":{"row":1,"column":23},"action":"remove","lines":["Your module description"],"id":1},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["R"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["i"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["c"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["a"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":[" "],"id":2},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["C"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["e"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["r"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["c"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["e"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["r"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["e"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":[" "],"id":3},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["I"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["b"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["a"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["r"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["r"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["a"]}],[{"start":{"row":3,"column":0},"end":{"row":58,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, cipherKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":4}],[{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"remove","lines":["*"],"id":5}],[{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"insert","lines":["+"],"id":6}],[{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"remove","lines":["+"],"id":7}],[{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"insert","lines":["*"],"id":8}],[{"start":{"row":40,"column":40},"end":{"row":40,"column":41},"action":"remove","lines":["r"],"id":9}],[{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"remove","lines":["e"],"id":10},{"start":{"row":40,"column":38},"end":{"row":40,"column":39},"action":"remove","lines":["h"]},{"start":{"row":40,"column":37},"end":{"row":40,"column":38},"action":"remove","lines":["p"]},{"start":{"row":40,"column":36},"end":{"row":40,"column":37},"action":"remove","lines":["i"]},{"start":{"row":40,"column":35},"end":{"row":40,"column":36},"action":"remove","lines":["c"]}],[{"start":{"row":40,"column":35},"end":{"row":40,"column":36},"action":"insert","lines":["d"],"id":11},{"start":{"row":40,"column":36},"end":{"row":40,"column":37},"action":"insert","lines":["e"]},{"start":{"row":40,"column":37},"end":{"row":40,"column":38},"action":"insert","lines":["c"]},{"start":{"row":40,"column":38},"end":{"row":40,"column":39},"action":"insert","lines":["r"]},{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"insert","lines":["i"]}],[{"start":{"row":40,"column":40},"end":{"row":40,"column":41},"action":"insert","lines":["p"],"id":12},{"start":{"row":40,"column":41},"end":{"row":40,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":40,"column":41},"end":{"row":40,"column":42},"action":"remove","lines":["t"],"id":13},{"start":{"row":40,"column":40},"end":{"row":40,"column":41},"action":"remove","lines":["p"]},{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"remove","lines":["i"]}],[{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"insert","lines":["y"],"id":14},{"start":{"row":40,"column":40},"end":{"row":40,"column":41},"action":"insert","lines":["p"]},{"start":{"row":40,"column":41},"end":{"row":40,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":40,"column":56},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":4},"end":{"row":41,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["s"],"id":16},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":[" "],"id":17},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["e"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["s"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["t"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["a"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["b"]},{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["a"]}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":[" "],"id":18},{"start":{"row":41,"column":15},"end":{"row":41,"column":16},"action":"insert","lines":["u"]},{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":["t"]},{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":["i"]},{"start":{"row":41,"column":18},"end":{"row":41,"column":19},"action":"insert","lines":["l"]},{"start":{"row":41,"column":19},"end":{"row":41,"column":20},"action":"insert","lines":["i"]},{"start":{"row":41,"column":20},"end":{"row":41,"column":21},"action":"insert","lines":["z"]},{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["a"]},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["n"]},{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"insert","lines":["d"]},{"start":{"row":41,"column":24},"end":{"row":41,"column":25},"action":"insert","lines":["o"]}],[{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"insert","lines":[" "],"id":19},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["c"]},{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"insert","lines":["y"]}],[{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"remove","lines":["y"],"id":20}],[{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"insert","lines":["i"],"id":21},{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["p"]},{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"insert","lines":["h"]},{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"insert","lines":["e"]},{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"insert","lines":["r"]},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["k"]},{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["e"]},{"start":{"row":41,"column":34},"end":{"row":41,"column":35},"action":"insert","lines":["y"]}],[{"start":{"row":41,"column":35},"end":{"row":41,"column":36},"action":"insert","lines":[" "],"id":22},{"start":{"row":41,"column":36},"end":{"row":41,"column":37},"action":"insert","lines":["e"]},{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"insert","lines":[" "],"id":23},{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":["l"]},{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"insert","lines":["u"]},{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"insert","lines":["g"]},{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"insert","lines":["a"]},{"start":{"row":41,"column":43},"end":{"row":41,"column":44},"action":"insert","lines":["r"]}],[{"start":{"row":41,"column":44},"end":{"row":41,"column":45},"action":"insert","lines":[" "],"id":24},{"start":{"row":41,"column":45},"end":{"row":41,"column":46},"action":"insert","lines":["d"]},{"start":{"row":41,"column":46},"end":{"row":41,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":47},"end":{"row":41,"column":48},"action":"insert","lines":[" "],"id":25},{"start":{"row":41,"column":48},"end":{"row":41,"column":49},"action":"insert","lines":["D"]},{"start":{"row":41,"column":49},"end":{"row":41,"column":50},"action":"insert","lines":["e"]},{"start":{"row":41,"column":50},"end":{"row":41,"column":51},"action":"insert","lines":["c"]},{"start":{"row":41,"column":51},"end":{"row":41,"column":52},"action":"insert","lines":["r"]}],[{"start":{"row":41,"column":52},"end":{"row":41,"column":53},"action":"insert","lines":["y"],"id":26},{"start":{"row":41,"column":53},"end":{"row":41,"column":54},"action":"insert","lines":["p"]},{"start":{"row":41,"column":54},"end":{"row":41,"column":55},"action":"insert","lines":["t"]},{"start":{"row":41,"column":55},"end":{"row":41,"column":56},"action":"insert","lines":["K"]},{"start":{"row":41,"column":56},"end":{"row":41,"column":57},"action":"insert","lines":["e"]},{"start":{"row":41,"column":57},"end":{"row":41,"column":58},"action":"insert","lines":["y"]}]]},"ace":{"folds":[],"scrolltop":366.30000000000126,"scrollleft":0,"selection":{"start":{"row":41,"column":58},"end":{"row":41,"column":58},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":25,"state":"start","mode":"ace/mode/python"}},"timestamp":1696994168151,"hash":"e46f2d76bae7a3c62c51222ac35d48db66a256aa"}