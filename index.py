import sys
import argparse 
import hashlib
from colorama import Fore, Style, init


# Inisialisasi pewarnaan terminal
init(autoreset=True)

def show_banner():
    """Menampilkan banner bergaya hacker untuk SKY-HashCracker"""
    banner = fr"""
{Fore.CYAN}     ____  _  ____     _   _           _     
{Fore.CYAN}    / ___|| |/ /\ \   | | | | __ _ ___| |___  
{Fore.BLUE}    \___ \| ' /  \ \  | |_| |/ _` / __| '_  \ 
{Fore.BLUE}     ___) | . \   \ \ |  _  | (_| \__ \ | | |
{Fore.GREEN}    |____/|_|\_\   \_\|_| |_|\__,_|___/_| |_|
{Fore.CYAN}  ===========================================
{Fore.GREEN}   [+] SKY - Hash Cracker Tool v1.0
{Fore.GREEN}   [+] Engine: MD5 Brute-Force (Stealth Core)
{Fore.CYAN}  ===========================================
    """
    print(banner)

def hash_translate(hash_target, daftar_kata, hash_type):
    print(f"\n[*] Memulai brute-force hash: {Fore.YELLOW}{hash_target}...")
    
    for kata in daftar_kata:
        # Mengubah kata dari wordlist menjadi hash sesuai tipe yang ditentukan
        if hash_type == 'md5':
            hash_result = hashlib.md5(kata.encode()).hexdigest()
        elif hash_type == 'sha1':
            hash_result = hashlib.sha1(kata.encode()).hexdigest()
        elif hash_type == 'sha256':
            hash_result = hashlib.sha256(kata.encode()).hexdigest()
        
        if hash_result == hash_target:
            return kata
    return None

def main():

    # Inisialisasi parser argparse
    parser = argparse.ArgumentParser(description='SKY - Hash Cracker Tool')
    parser.add_argument('hash', type=str, help='the hash you want to translate')
    parser.add_argument('--wordlists', "-w", type=str, required=True, help='the wordlists you want to use')
    parser.add_argument('--version',"-v", action='version', version='v1.0')
    parser.add_argument('--type', "-t", type=str, choices=['md5', 'sha1', 'sha256'], default='md5', help='the type of hash (default: md5)')

    args = parser.parse_args()

    if not args.hash or not args.wordlists:
        parser.print_help()
        sys.exit(1)

    show_banner()
    

    # Membaca berkas wordlist secara aman
    try:
        with open(args.wordlists, "r") as f:
            kata_kunci = [line.replace('\r', '').strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Error: File '{args.wordlists}' tidak ditemukan di folder ini.")
        sys.exit(1)

    # Eksekusi pencarian sandi
    hasil_tebakan = hash_translate(args.hash, kata_kunci, args.type)

    # Tampilkan hasil akhir ke layar terminal
    if hasil_tebakan:
        print(f"{Fore.GREEN}[+] KATA SANDI DITEMUKAN: {Fore.WHITE}{Style.BRIGHT}{hasil_tebakan}")
    else:
        print(f"{Fore.RED}[-] Maaf, kata sandi tidak ditemukan di dalam wordlist.")
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Proses pembongkaran sandi dibatalkan oleh pengguna.")
        sys.exit(0)
