from hashlib import sha256


def hash_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()

    return sha256(data).hexdigest()


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


# Enter multiple files
file_names = input("Enter file names separated by comma: ")

files = file_names.split(",")

original_hashes = {}
original_contents = {}


print("\nGenerating original hashes...\n")


for file in files:

    file = file.strip()

    original_hashes[file] = hash_file(file)
    original_contents[file] = read_file(file)

    print(file)
    print("Original Hash:", original_hashes[file])


input("\nModify any file, save it, then press Enter...")


print("\n========== INTEGRITY REPORT ==========")


for file in files:

    file = file.strip()

    current_hash = hash_file(file)

    print("\nFile:", file)
    print("Original Hash:", original_hashes[file])
    print("Current Hash :", current_hash)


    if original_hashes[file] == current_hash:

        print("Status: UNMODIFIED")

    else:

        print("Status: MODIFIED")

        current_contents = read_file(file)

        print("Changed lines:")

        for i in range(len(original_contents[file])):

            if original_contents[file][i] != current_contents[i]:

                print("Line", i + 1)
                print("Original:", original_contents[file][i])
                print("Current :", current_contents[i])
