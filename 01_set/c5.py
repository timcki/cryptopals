
def xor(pt, key) -> bytes:
    arr = []
    for counter, ch in enumerate(pt):
        arr.append(ch ^ key[counter % len(key)])

    return bytes(arr)


if __name__ == '__main__':
    # Constants
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    pt = """Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal"""
    key = ['I', 'C', 'E']
    ct = xor(pt, key)
    assert(ct.hex() == expected)
