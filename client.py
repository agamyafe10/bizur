import hashlib
from hashlib import md5


def str_to_hash(client_input="Hello World!"):
    hash_object = hashlib.md5(client_input.encode())
    hashed_code = hash_object.hexdigest()
    print(hashed_code)
    return hashed_code

def start_hashing(fromnum,to):
    for i in range(fromnum, to):
        if str_to_hash(str(i)) == "cc4af25fa9d2d5c953496579b75f6f6c":
            print("Your Number is:{0}",i)
            break

