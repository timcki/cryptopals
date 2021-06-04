from c6 import parse_b64
from Crypto.Cipher import AES

if __name__ == '__main__':
    contents = None
    key = bytes(ord(c) for c in 'YELLOW SUBMARINE')
    with open('7.txt') as f:
        contents = parse_b64(f.read())
    cipher = AES.new(key) 
    pt = cipher.decrypt(contents)


    print(pt.decode('utf-8'))
