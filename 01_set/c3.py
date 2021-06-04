import codecs

hs1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

h1 = codecs.decode(hs1, 'hex')

#for i in range(ord('a'), ord('z')+1):
    #print(bytes(i^h for h in h1))

#for i in range(ord('A'), ord('Z')+1):
print(bytes(ord('X')^h for h in h1))