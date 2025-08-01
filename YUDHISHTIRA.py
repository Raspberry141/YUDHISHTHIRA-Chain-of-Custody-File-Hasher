from pyfiglet import figlet_format
from colorama import Fore, Style
import hashlib

print(Fore.CYAN + figlet_format("YUDHISHTIRA"))
print(Fore.RED + "[*] Created by Vizz\n" + Style.RESET_ALL)

def get_hash(file_path, algo):
    h = hashlib.new(algo)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

hash1 = get_hash("original.img", "sha256")
hash2 = get_hash("copied.img", "sha256")

print(Fore.YELLOW + f"Original: {hash1}\nCopied: {hash2}" + Style.RESET_ALL)
print(Fore.GREEN + "[+] Integrity Verified" if hash1 == hash2 else Fore.RED + "[!] Hash Mismatch!")