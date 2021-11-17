import zipfile
from multiprocessing import Process


# extract_file brutes passwords to open zip archive
def extract_file(passwords):
    with zipfile.ZipFile('archive_name.zip') as zip_file:
        for password in passwords:
            try:
                zip_file.extractall(pwd=password)
                print("[+] Password found:", password.decode().strip())
            except Exception as e:
                pass


def main():
    with open('common_passwords.txt', 'rb') as pass_file:
        passwords = [i.strip() for i in pass_file]

    NUMBER_OF_THREADS = 8
    for i in range(NUMBER_OF_THREADS):
        p = Process(target=extract_file, args=[passwords[i::NUMBER_OF_THREADS]])
        p.start()


if __name__ == '__main__':
    main()
