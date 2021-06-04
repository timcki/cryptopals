BSIZE = 16
        
def count_repetitions(ciphertext, block_size):
    chunks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    reps = len(chunks) - len(set(chunks))
    return (ciphertext, reps)

if __name__ == '__main__':
    ciphers = [bytes.fromhex(l.strip()) for l in open('8.txt')]
    repetitions = [count_repetitions(c, BSIZE) for c in ciphers]

    candidates = sorted(repetitions, key=lambda x: x[1], reverse=True)[:3]
    for c in candidates:
        print(f'{c[1]} repetitions: {"".join("{:02x}".format(x) for x in c[0])}')
