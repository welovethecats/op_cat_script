# Puzzle by Leveraging OP_CAT

The idea is to create a fully fair puzzle where one person can release coins if they are able to prove that they own the public key

   
	pubkey = '0xe17048119e86c59f66498e4fc2a28278b109a3a1128a4d64234457f0ab000233'
	# split the key and accept first N bits as proof
	pubkeyFirstN = 'e1704811'
    pubkeyLastK = '9e86c59f66498e4fc2a28278b109a3a1128a4d64234457f0ab000233'

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

We are able to brute force our way to the public key, which, in this case is, SHA256(6166)

When it comes to scripting, the corresponding Tapscript would look like this

    Input script: <signature_pubkey> <pubkeyLastK>  
	Output script: <pubkeyFirstN> OP_SWAP OP_CAT OP_CHECKSIG

Below the associated stack:

| Stack | Script  | Comment  |
|--|--|--|
| Empty | <signature_pubkey> <pubkeyLastK\> <pubkeyFirstN> <pubkeyFirstN\> OP_SWAP OP_CAT OP_CHECKSIG | Initial state  |
| <signature_pubkey> | <pubkeyLastK\> <pubkeyFirstN\> OP_SWAP OP_CAT OP_CHECKSIG |  
| <signature_pubkey> <pubkeyLastK\> | <pubkeyFirstN\> OP_SWAP OP_CAT OP_CHECKSIG |  
| <signature_pubkey> <pubkeyLastK\> <pubkeyFirstN\> | OP_SWAP OP_CAT OP_CHECKSIG |  Both parts on the stack
| <signature_pubkey> <pubkeyLastK\> <pubkeyFirstN\> | OP_SWAP OP_CAT OP_CHECKSIG |  Swap last k with first n
| <signature_pubkey> <pubkeyFirstN\> <pubkeyLastK\>  | OP_CAT OP_CHECKSIG |  Concatenate parts
| <signature_pubkey> <pubKeyToCheck\>  | OP_CHECKSIG |  Check signature
| OP_TRUE  |  |  True if correct and bitcoins are released
