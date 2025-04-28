# HTTP Brute Force Login Script

This Python script performs a brute-force attack on a web login form by iterating through a list of passwords for a given username and target URL.

## Features

- Reads passwords from a file
- Sends HTTP POST requests to the login endpoint
- Detects success based on response text or status code
- Customizable login form path and success condition

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/http-bruteforce-login.git
   cd http-bruteforce-login
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or directly:
   ```bash
   pip install requests
   ```

## Usage

1. Run the script:
   ```bash
   python brute_force_login.py
   ```
2. When prompted, enter:
   - **Target IP Address** (e.g., `103.119.179.101`)
   - **Port** (default `80`)
   - **Login Path** (e.g., `/login`)
   - **Username** (e.g., `admin`)
   - **Path to Password File** (e.g., `passwords.txt`)

The script will try each password and print whether it succeeded or failed.

## Customization

- **Success condition**: By default, the script checks for the substring `"Welcome"` in the response or a `302` status code. You can modify this in the `brute_force_login` function:

  ```python
  if "Welcome" in response.text or response.status_code == 302:
      # success logic
  ```

- **Timeout**: Adjust the `timeout` parameter in `requests.post()` if needed.

## Example

```bash
Enter Target IP Address (e.g., 103.119.179.101): 192.168.1.10
Enter Port (default 80 if unknown): 81
Enter Login Path (e.g., /login): /doc/page/login.asp
Enter Username (e.g., admin): admin
Enter Path to Password File: /path/to/password_file.txt
```

## Disclaimer

Use this script only on systems you own or have explicit permission to test. Unauthorized access to systems is illegal and unethical.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

