import zipfile
import itertools

# simple_password_bruteforce
def simple_password_bruteforce():
    for password_length in range(1, 100000):
        # all_symbols = 'abcdefghijklmnopqrstuvwxyz0123456789'
        # To shorten process
        all_symbols = 'crupes'
        for password in itertools.product(all_symbols, repeat=password_length):
            yield ''.join(password)

zip_file = ".\\Rupees.zip"

zip_file = zipfile.ZipFile(zip_file)


for word in simple_password_bruteforce():
    print(word)
    try:
        zip_file.extractall(pwd=word.encode("utf-8"))
    except:
        continue
    else:
        print("[+] Password found:", word)
        exit(0)

print("[!] Password not found, try other wordlist.")

# Spoiler Alert
# password = "rupees"
# zip_file.extractall(pwd=passwordassword.encode("utf-8"))