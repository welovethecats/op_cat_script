import hashlib
import random

def mine(target):
    hashFound = False
    num = 0
    while not hashFound:
        num = random.randint(0,10000)
        h = hashlib.sha256(str(num).encode()).hexdigest()
        print(h)
        if h.startswith(target):
            hashFound = True
    return (num, h)

def main():
    # let us define a public key, here it's sha256(6166)
    pubkey = '0xe17048119e86c59f66498e4fc2a28278b109a3a1128a4d64234457f0ab000233'
    # now let us split this key in two
    pubkeyFirstN = 'e1704811'
    pubkeyLastK = '9e86c59f66498e4fc2a28278b109a3a1128a4d64234457f0ab000233'
    # important to note that we can pick an arbitrary number of bits for the puzzle
    # if anybody can provide a hash starting with pubkeyHead, we release the coins
    print(f"Number: {mine(pubkeyHead)[0]}, associated hash is {mine(pubkeyHead)[1]}")

if __name__=="__main__":
    main()
