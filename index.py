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

def hash_translate(hash_target, daftar_kata):
    print(f"\n[*] Memulai brute-force hash: {Fore.YELLOW}{hash_target}...")
    
    for kata in daftar_kata:
        # Mengubah kata dari wordlist menjadi MD5 lalu dicocokkan
        if hashlib.md5(kata.encode()).hexdigest() == hash_target:
            return kata
    return None

def main():
    show_banner()
    
    # Inisialisasi parser argparse
    parser = argparse.ArgumentParser(description='SKY - Hash Cracker Tool')
    parser.add_argument('hash', type=str, help='the hash you want to translate')
    parser.add_argument('--wordlists', "-w", type=str, required=True, help='the wordlists you want to use')

    args = parser.parse_args()

    # Membaca berkas wordlist secara aman
    try:
        with open(args.wordlists, "r") as f:
            kata_kunci = [line.replace('\r', '').strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Error: File '{args.wordlists}' tidak ditemukan di folder ini.")
        sys.exit(1)

    # Eksekusi pencarian sandi
    hasil_tebakan = hash_translate(args.hash, kata_kunci)

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
