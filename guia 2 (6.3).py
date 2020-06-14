school= ' Pontificia Universidad Catolica de Valparaiso'
numVowels = 0
numCons =0

for char in school:
    if char == 'o'or char == 'n'or char == 'a'  \
    or char == 'or' or char == 'i':
        numVowels +=1
    elif char == 's' or char == 'P':
        print(char)
    else:
        numCons -=1
        
        print ('numVowels is: ' + str(numVowels))
        print('numCons is: ' + str (numCons))