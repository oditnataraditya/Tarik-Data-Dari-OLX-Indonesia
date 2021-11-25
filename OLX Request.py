import requests
import json
import pandas as pd


url = ['https://www.olx.co.id/api/relevance/v2/search?category=5158&facet_limit=100&location=2000002&location_facet_limit=20&platform=web-desktop&price_max=400000000&price_min=200000000&user=17d5266ccc0x5b2f2d3c',
]
headers = {
    'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

### Kumpulkan semua link yang tersedia dari OLX API
for i in url:
    r = requests.get(i, headers=headers)
    response = json.loads(r.text)
    try:
        if response['metadata']['next_page_url'] != None:
            ul =  response['metadata']['next_page_url']
            url.append(ul)
    except:
        break

### Persiapkan wadah untuk scraping
deskripsi_bsr = []
deskripsi_kcl = []
lokasi = []
kamar = []
luas_tanah = []
luas_bangunan = []
sertifikat = []
harga = []
alamat = []

### Scraping
for i in url:
    r = requests.get(i, headers=headers)
    response = json.loads(r.text)
    for x in response['data']:
        try:
            desc = x['description']
            mini_desc = x['title']
            size = x['main_info']
            loc = x['locations_resolved']['ADMIN_LEVEL_3_name']
            price = x['price']['value']['display']
            build = x['parameters'][1]['value']
            land = x['parameters'][2]['value']
            if x['parameters'][-2]['key'] == 'p_certificate':
                serti = x['parameters'][-2]['formatted_value']
            else:
                serti = 'tidak ada'
            address = x['parameters'][-1]['formatted_value']
        finally:
            deskripsi_bsr.append(desc)
            deskripsi_kcl.append(mini_desc)
            lokasi.append(loc)
            kamar.append(size)
            luas_tanah.append(land)
            luas_bangunan.append(build)
            sertifikat.append(serti)
            harga.append(price)
            alamat.append(address)

dict_to_pd = {
    'Harga Iklan' : harga,
    'Deskripsi Singkat': deskripsi_kcl,
    'Lokasi': lokasi,
    'Alamat Lengkap': alamat,
    'Jumlah Kamar' : kamar,
    'Luas Bangunan': luas_bangunan,
    'Luas Tanah': luas_tanah,
    'Bentuk Sertifikat': sertifikat,
    'Deskripsi Lengkap': deskripsi_bsr
}

### masukkan ke dataframe dan csv
df = pd.DataFrame(dict_to_pd)
df.to_csv('Rekapan OLX.csv', index=False)