import codecs
from c4 import charset, process_xord
from c5 import xor

KEYSIZE = 40

#print(hamming_distance('this is a test', 'wokka wokka!!!')) == 37
def hamming_distance(s1, s2) -> int:
    bin = lambda s: ''.join(format(c, 'b').zfill(8) for c in s)
    return sum([int(c1 != c2) for c1, c2 in zip(bin(s1), bin(s2))])

def parse_b64(text) -> bytes:
    return codecs.decode(codecs.encode(text, 'utf-8'), 'base64')

if __name__ == '__main__':
    contents = None
    with open('6.txt') as f:
        contents = parse_b64(f.read())
    lens = {}
    blocks = {}
    for n in range(2, KEYSIZE):
        blocks[n] = list(contents[i:i+n] for i in range(0, len(contents), n))
        dists = 0
        for i in range(0, len(blocks[n])-1, 2):
            dists += (hamming_distance(blocks[n][i], blocks[n][i+1]))
        lens[n] = (dists/(len(blocks[n])//2))/n
    candidates = sorted(lens.items(), key=lambda x: x[1])[:3]
    for keysize, dist in candidates:
        print(f"Testing keysize {keysize} with hamming distance {dist}")
        transposed = [[] for i in range(keysize)]
        for i in range(keysize):
            for b in blocks[keysize]:
                try:
                    transposed[i].append(b[i])
                except:
                    transposed[i].append(0)


        keys = [[] for i in range(keysize)]
        for k, block in enumerate(transposed):
            for i in range(0, 130):
                key, pt = process_xord(block, i, delta=9)
                if key != None:
                    keys[k].append(key)
                    #print("Key:", key, "|| PT:", pt)
        for letter in keys:
            if len(letter) > 1:
                print("(", end="")
            for var in letter:
                print(chr(var), end="")
            if len(letter) > 1:
                print(")", end="")
        print()


    guessed_key = 'Terminator X: Bring the noise'
    key = bytes([ord(s) for s in guessed_key])
    print(xor(contents, key).decode('utf-8'))
