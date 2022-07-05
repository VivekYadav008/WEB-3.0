import time
import hashlib
str3 = input("Enter the header string ")
encoded_str = str3.encode()
sha256str = hashlib.sha256()
sha256str.update(encoded_str)
hexst = sha256str.hexdigest()
initial = time.time()
for a in range(2**256 - 1):
    if int(hexst, 16) <= (0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF):
        final = time.time() - initial
        print('The proof of work was done in ', final, "seconds")
        print("the target satisfying number appended to the string is ", a )
        break
    str2 = str3 + str(a)
    encoded_str = str2.encode()
    sha256str.update(encoded_str)
    hexst = sha256str.hexdigest()
