import os
import sys
import hashlib

dir_path = sys.argv[1]
files = os.listdir(dir_path)
print(f"{len(files)} files found in {dir_path}")
duplicates = []
hash_keys = dict()
for index, filename in enumerate(files):
    full_filename = os.path.join(dir_path, filename)
    if os.path.isfile(full_filename):
        with open(full_filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash]=(index, filename)
        else:
            print(f"{filename} is duplicate of {hash_keys[filehash][1]}")
            duplicates.append(full_filename)
if len(duplicates) > 0:
    print("Following files are duplicates and can be removed: ", duplicates)
    response = input("Should I go ahead and delete?")
    if response=="Y":
        for elem in duplicates:
            print("Deleting ", elem)
            os.remove(elem)
else:
    print("No duplicates found")




