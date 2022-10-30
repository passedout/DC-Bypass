# ALL CREDITS RESERVED TO SIEGFRIED/SURGUD! CONTACT / TELEGRAM: https://t.me/siegfried_tos ~ https://t.me/tosviolators

#Run the script and input a proxy/verification url once it asks for it then wait till the proxy did the request

import requests

def bypass_doubleCounter(url: str, proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }

    headers = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "Accept-Encoding": 'gzip, deflate, br',
        "Accept-Language": 'en-US,en;q=0.9',
        "Cache-Control": 'max-age=0',
        "Connection": 'keep-alive',
        "Host": 'verify.dcounter.space',
        "sec-ch-ua": '"Chromium";v="95", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": 'document',
        "Sec-Fetch-Mode": 'navigate',
        "Sec-Fetch-Site": 'cross-site',
        "Sec-Fetch-User": '?1',
        "Upgrade-Insecure-Requests": '1',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4624.0 Safari/537.36',
    }

    r = requests.get(url, headers=headers, proxies=proxies)
    if r.status_code == 200:
        print("Successfully bypassed double counter")
    else:
        print(r)
        print(r.text)
        print("Failed bypassing double counter, above is return data from the request")
    
def main():
    # you need a good proxy that wasnt used before with double counter (free ones might work)
    proxy = input("Proxy: (http://USERNAME:PASSWORD@HOST:PORT or http://HOST:PORT)")
    # url should look something like: https://verify.dcounter.space/v/ID
    url = input("Double counter verify url: ")
    
    bypass_doubleCounter(url, proxy)

if __name__ == "__main__":
    main()

# ALL CREDITS RESERVED TO SIEGFRIED/SURGUD! CONTACT / TELEGRAM: https://t.me/siegfried_tos ~ https://t.me/tosviolators
