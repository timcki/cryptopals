import codecs

hs1 = "1c0111001f010100061a024b53535009181c"
hs2 = "686974207468652062756c6c277320657965"
hs3 = "746865206b696420646f6e277420706c6179"

h1 = codecs.decode(hs1, 'hex')
h2 = codecs.decode(hs2, 'hex')
h3 = codecs.decode(hs3, 'hex')

print(bytes(x^y for x, y in zip(h1, h2)))
print(h3)
    