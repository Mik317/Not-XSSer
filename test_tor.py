import requests

proxies = {
   'http': 'socks5://127.0.0.1:9150',
}

def main():
    url = 'http://icanhazip.com'
    response = requests.get(url)
    print('Your IP: {}'.format(response.text.strip()))
    response = requests.get(url, proxies=proxies)
    print('Your IP Under TOR: {}'.format(response.text.strip()))

if __name__ == '__main__':
    main()
