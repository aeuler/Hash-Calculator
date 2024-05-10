import hashlib

def calculate_hashes(input_string):
    hashes = {
        "md5": hashlib.md5(input_string.encode()).hexdigest(),
        "sha1": hashlib.sha1(input_string.encode()).hexdigest(),
        "sha256": hashlib.sha256(input_string.encode()).hexdigest(),
        "sha512": hashlib.sha512(input_string.encode()).hexdigest()
    }
    return hashes

def find_string_from_hash(target_hash):
    # Iterate through all ASCII characters to find the string that produces the target hash
    for char in range(32, 127):
        for length in range(1, 10):  # Limiting length for demonstration purposes
            test_string = chr(char) * length
            hash_md5 = hashlib.md5(test_string.encode()).hexdigest()
            hash_sha1 = hashlib.sha1(test_string.encode()).hexdigest()
            hash_sha256 = hashlib.sha256(test_string.encode()).hexdigest()
            hash_sha512 = hashlib.sha512(test_string.encode()).hexdigest()

            if hash_md5 == target_hash or hash_sha1 == target_hash or hash_sha256 == target_hash or hash_sha512 == target_hash:
                return test_string

    return None

def main():
    print("1. Calculate Hashes")
    print("2. Find String from Hash")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        input_string = input("Enter the string to calculate hashes: ")
        hashes = calculate_hashes(input_string)
        print("Hashes:")
        for algo, hash_value in hashes.items():
            print(f"{algo}: {hash_value}")
    elif choice == "2":
        target_hash = input("Enter the hash to find the string: ")
        found_string = find_string_from_hash(target_hash)
        if found_string:
            print(f"String producing the hash: {found_string}")
        else:
            print("String not found for the given hash.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()