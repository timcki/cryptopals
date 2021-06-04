import codecs
import string

charset = [l for l in string.ascii_letters]
for n in string.digits: charset.append(n)
for n in string.punctuation: charset.append(n)
for n in string.whitespace: charset.append(n)

test_chars = [l for l in string.ascii_letters]
for n in string.digits: test_chars.append(n)
test_chars.append(' ')
test_chars.append('\n')
test_chars.append('\r')

def process_xord(h1, key, delta=0):
    bs = bytes(key^h for h in h1)
    flag = True
    errors = 0
    for b in bs:
        if flag == False: break
        if chr(b) not in test_chars:
            if errors >= delta: flag = False
            else: errors += 1
    if flag: return (key, bs)
    return None, None

def break_key(ct):
    for i in charset:
        key, pt = process_xord(ct, i)
        if key != None:
            print("Key:", key)
            print(pt)




if __name__ == '__main__':
    with open('04.dat') as f:
        for line in f:
            break_key(codecs.decode(line.strip(), 'hex'))
