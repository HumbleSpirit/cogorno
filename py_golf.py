import requests
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)] 
for f in files:
    if f.endswith("quick-fix-breaking-80.json.txt"):
        #print(os.path.join(f))
        filename = (os.path.splitext(f)[0])
        clean_filename = (os.path.splitext(filename)[0].title())
        print(clean_filename)

        with open(f) as f:
            list_items = f.read().splitlines()
            #print(list_items)


            headers = {
    'authority': 'www.cogornogolf.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'x-thinkific-client-app-version': '3e9547b40243ba6df4212abda625af4c559f966c',
    'x-thinkific-client-date': '2021-10-26T19:51:59.273Z',
    'dnt': '1',
    'traceparent': '00-6f71f2e8cc21a75f5e6dbf37706bda78-09ea85f49e48c562-01',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'accept': 'application/json',
    'x-client-id': 'KOBAYASHI',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cogornogolf.com/courses/take/quick-fix-breaking-80/texts/6034747-breaking-80',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8,uk;q=0.7,no;q=0.6,nb;q=0.5,nn;q=0.4,bg;q=0.3,af;q=0.2',
    'cookie': 'visitor_id=1083656131; _thinkific_session=QXY4WXdGMndTMTNXWjB4Mmh3c1hHNVRzRTNndDEwNUNRTWJONkptck9JV2dIZzJZL1J5S21RWHZVMWhUdTVIUnRjWGJDaUh6QWJUU0ZYckhsT1pUUjEwTjN5eHE2V3dHdTR3aTlSVkNFQ2gxZFlhNjI1cFVjK292SHJpVEZLSy96ZGdCUU5nVFNuZG9vK2pVTDdYSUdxemJSa2lXcE1qOWo3VWdKVG1vS3hCUGpzRWdxT3p1RnlocEp0WFNsVjBEaXQvTE9tVVkyeUh0dXAyWTEzdDVzZEt3YWtjU0lkRkdHaU95UXVpaEVGdUVUQmF1RmExTmtDOTVibWhVN0grbi83NjdmV3lmMEU1UWdJcCsvVzNzSUY5dWp4Y3JlaWxNb21SbGtXYXMvQms2M3FnTXdpeElFZXBKc0J2bHJYZTRTeTNzSzBFaEFROVprYlpCRnhoYXIxYUZrY0ZIY0pubFdkOXhHUnhhdFZocjJuSVpWalpIMEVCTzhPbXNNWG95OXFsdVFRUmdkQzhJamdSandRalVtdz09LS1UUWk4VzZRSDR4cXFjZmdRcUpqQkVBPT0%3D--e1d6e45c1cb9c0bc26acbbc0e21d61e2a476e603',
}



            for item in list_items:
                response = requests.get('https://www.cogornogolf.com/api/course_player/v2/lessons/' + str(item) + '/download', headers=headers, stream=True)
                print(str(item))
                index = list_items.index(item)
                #print(index)

                handle = open(clean_filename + '_' +str(index) + '_' + str(item) + '.mp4', "wb")
                for chunk in response.iter_content(chunk_size=1048576):
                    if chunk:  # filter out keep-alive new chunks
                        #print(chunk)
                        handle.write(chunk)
