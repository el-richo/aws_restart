{"filter":false,"title":"caesar-cipher.py","tooltip":"/caesar-cipher.py","undoManager":{"mark":20,"position":20,"stack":[[{"start":{"row":1,"column":0},"end":{"row":1,"column":23},"action":"remove","lines":["Your module description"],"id":21},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["R"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["i"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["c"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["a"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":[" "],"id":22},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["C"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["e"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["r"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["c"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["e"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["r"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["e"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":17},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":23}],[{"start":{"row":4,"column":0},"end":{"row":6,"column":25},"action":"insert","lines":["def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet"],"id":24}],[{"start":{"row":6,"column":25},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":26}],[{"start":{"row":8,"column":0},"end":{"row":10,"column":26},"action":"insert","lines":["def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt"],"id":27}],[{"start":{"row":10,"column":26},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":4},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":29}],[{"start":{"row":12,"column":0},"end":{"row":14,"column":22},"action":"insert","lines":["def getCipherKey():","    shiftAmount = input( \"Please enter a key (whole number from 1-25): \")","    return shiftAmount"],"id":30}],[{"start":{"row":14,"column":22},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "],"id":32}],[{"start":{"row":16,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage",""],"id":33}],[{"start":{"row":28,"column":0},"end":{"row":30,"column":56},"action":"insert","lines":["def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)"],"id":34}],[{"start":{"row":27,"column":27},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":31,"column":56},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]},{"start":{"row":32,"column":4},"end":{"row":33,"column":0},"action":"insert","lines":["",""]},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "],"id":37}],[{"start":{"row":33,"column":0},"end":{"row":45,"column":52},"action":"insert","lines":["def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decypted Message: {myDecryptedMessage}')"],"id":38}],[{"start":{"row":45,"column":52},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]},{"start":{"row":46,"column":4},"end":{"row":47,"column":0},"action":"insert","lines":["",""]},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"remove","lines":["    "],"id":40}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":24},"action":"insert","lines":["runCaesarCipherProgram()"],"id":41}]]},"ace":{"folds":[],"scrolltop":252.90000000000012,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":25,"state":"start","mode":"ace/mode/python"}},"timestamp":1696645458245,"hash":"ed84bfa64f5b962ad314d00be9a2fefe7815b454"}