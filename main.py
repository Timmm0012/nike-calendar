import requests

url = "https://api.nike.com/product_feed/threads/v3/?anchor=0&count=50&filter=marketplace%28NL%29&filter=language%28en-GB%29&filter=upcoming%28true%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&sort=effectiveStartSellDateAsc"

payload={}
headers = {
  'authority': 'api.nike.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'cookie': 'geoloc=cc=NL,rc=,tp=vhigh,tz=GMT+1,la=52.35,lo=4.92; audience_segmentation_performed=true; AKA_A2=A; s_ecid=MCMID%7C39495308731735197882402725361413322743; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C39495308731735197882402725361413322743%7CMCAID%7CNONE%7CMCOPTOUT-1672673036s%7CNONE%7CvVersion%7C3.4.0; bm_mi=C614612F731355609DA2BCBDC9D61EC0~YAAQdPBuaJuChxOFAQAA3S+nchLai7zlmq97WUi9IhtNE9ZlsuM6VJKLHu+ScgEBPo2oESLWYVc/RSOtx8nbrpGCyoyacu8tN62c8rXD7D3qT8oE4xGMZIShqS+UHztfHjdiSRmF/zLpbO0TZJhF0FsIfTdKBjzl6U8/HYezdevbhQJZrK025qucrtkwQfWGJld5N1h56TlIeABd8m5RfAuG7MNxpwe36No5rAOIwOhOIO3QSV9HLjbfi8Ob5xW8SkceKAfPhRbwg4wxOGU7nVKKPOJf59oQ7y712lEqVVxm9K+Cu1JOKbTk3/MLWFgsJyryX79ekag=~1; ak_bmsc=5F4E66E764202F0E0E67013BF178B4F3~000000000000000000000000000000~YAAQdPBuaAODhxOFAQAAyTanchJOrEBE8vVXx54Gk4RVg+lD4Yv8YVgz3i5C3N6QJQkCmKk3onvJCzGflFxur5hYMgTj6DyQnKJYJL7v6HZIXqfBK7IMfLm65ZHrLEz0bKMB1wRtU+sofqCVCMwaHzg2lWU9nujmxqKHlE+8aHB6fVoTOHL+h4HA6QnY9Aw9dcv/Jlr6lulnAgpHlhH1M0g4x1E/c8AtKdMZ3hz7GNGx8sZorVCeVhFEvwG4i1X5WMnsempdBuBHDSTe0onwVH7ibFhibT1tdgdWQUlwT810INkOSuAj0ScbHo3hWPr2acd6kkFPWB3s3LVhW6b8uQIl0UZ70My0QO/wgmLaXPFEmd4WF8+YNoHHifqd/Y8vfHBjCebOGqrEL6HdVlnmZYDQa4ts7E/pId5DYxP0V3M6bTA1V6O+IfjJxCwf8rOwpkBQYXgRtBMpQh1gOJBP3VzKBEKMYjF1zTBgY48RDLvgZz2goQ4TQVEuv2Rf2D6Oj+amLFCzw5ioXgdE; sq=3; anonymousId=C9B1170451F3FF2E92A939004BB21259; _gcl_au=1.1.1784297452.1672665841; _gid=GA1.2.2140637641.1672665841; _scid=5178c5cb-66d4-4cb6-a06d-44fa545b4b35; _fbp=fb.1.1672665841412.2097625493; bluecore_gclid=true; _pin_unauth=dWlkPVlXSmpOMlZrTW1ZdE1UTTNZaTAwT1dZM0xUZzJNVEl0Tm1ObFkySTJOMlEyT1RkaA; AnalysisUserId=689f952b-d984-41dc-894f-09c80d77d6a7; cid=undefined%7Cundefined; _gcl_aw=GCL.1672667605.Cj0KCQiAnsqdBhCGARIsAAyjYjTFWnsEW4JoyrsaMv-37AB7KX95Iqmik_lsqyraK6-newMZ5pu4Ng4aAlZeEALw_wcB; _gcl_dc=GCL.1672667605.Cj0KCQiAnsqdBhCGARIsAAyjYjTFWnsEW4JoyrsaMv-37AB7KX95Iqmik_lsqyraK6-newMZ5pu4Ng4aAlZeEALw_wcB; _gac_UA-167630499-3=1.1672667605.Cj0KCQiAnsqdBhCGARIsAAyjYjTFWnsEW4JoyrsaMv-37AB7KX95Iqmik_lsqyraK6-newMZ5pu4Ng4aAlZeEALw_wcB; bc_nike_netherlands_dutch_triggermail=%7B%22distinct_id%22%3A%20%2218572a73f2076b-03a53a4c4d6eff-26021151-1fa400-18572a73f21768%22%2C%22bc_persist_updated%22%3A%201672665841442%7D; _ga=GA1.1.1208055554.1672665841; _uetsid=b88c8ca08aa011edb46d47d6ab0294bf; _uetvid=b88cbd508aa011edbe0ed39788a8a777; _ga_EWJ8FE8V0B=GS1.1.1672665841.1.1.1672667615.49.0.0; CONSUMERCHOICE=nl/en_gb; NIKE_COMMERCE_COUNTRY=NL; NIKE_COMMERCE_LANG_LOCALE=en_GB; ppd=upcoming|snkrs>upcoming; bm_sz=6989663164589F03DD5FB507B913AEAB~YAAQPsMTAlaNwFWFAQAAA6LXchLRvyLBAcR7mQ67muQhnkAEtkoFIdrcAoeKOAYxw3F/n05TzOHufLr6vshi9fzTCExOZR2WjNSUWUt0dZjBlzem8Zbrp4QcKT3+1zWpXh1RINtRNZdNSB+E68O980W3N2g/dcOmRuEvSi24TJTPnVqYtZ7KwoJw5uPtp1CC5w9G0rgUywWpg9RQoK6ISp2sRBn6n8vDOxuNU2WqBM+Mu76UTm19BaULKPoQjaRQPZ7ptMA9+Y5H9k0O1MZ0IZEqRvOSgtGu/IZf234qsKTqMEMHD4YZtc5h4IbdCj7/Pa7ykJnRn4V5rwHcEfyeTMK/QbhzRlyWQBDPXzSaa/8hs/ZcrrjZnB9fiiYBZi+8LXp1ZfYOmJZmW79/Dhxq4V8hGA70qHo1OwLigSrtes0Fm9prwTNMn6WncYPlD3YlkxKX5ttWpnzRprOAffD59C+NNBI2e8P4154T1Hv2~3617590~4338484; ak_bmsc_nke-2.2-ssn=0gjDSpxrkoS98lTTsN2KxczSYfXrQopXSuKkui3mnkyryyrrj6QrwDK4Wnuv2cffh2gNAmeouC1NzAHZQtVrWuoUY7xkGjuZj6bNjwJWDOl38HMv8xhzWuDgMjjIijsZSFYRhjLq54oO5lsZ7iTmrpvANYc7; ak_bmsc_nke-2.2=0gjDSpxrkoS98lTTsN2KxczSYfXrQopXSuKkui3mnkyryyrrj6QrwDK4Wnuv2cffh2gNAmeouC1NzAHZQtVrWuoUY7xkGjuZj6bNjwJWDOl38HMv8xhzWuDgMjjIijsZSFYRhjLq54oO5lsZ7iTmrpvANYc7; forterToken=b57100f5e36f4985a33faf5444d5c361_1672669013282__UDF43_13ck; _abck=08BD596928F2C1C1FE59806A68A53D56~-1~YAAQXRjdWCw8TjOFAQAAprHXcgnzUGRSMkS6AEx4QU2TKDhbPyKaaVvxQEF8XlnnOV/f8Q6LLmSMLXKsihxRxoXUF6luL1SIrEIo/1+j3akSxNn2iDDVyS9e8tDcwd8VT1iRSR1/q/HO/h+tYcZd4Ud5lQdA+rxfh5SwN7bU6YylhCR7TVvldKTN7WDiEXYKqoQJKolG7Vzz0k+juajceL5iFT94eABomDkHeeicrqoLGR6EuCFp6lo/yIAzncHbNtbStRa865lxB7iYChjNRNPYefqMvgo6k4WxWm7vYEU6a90qVW/0/diXnkZhM3wXBRgWCbUnwBgmT6JwWkNKT7jCj7u7uboOFdllmSjlmBdt6BK2v97503lqeNJgK1gY+jcWJJiSAuprl+re4wbjS/Qujvqe96Ar/qzuN1zzwU3CgAlRmjsYPw6nE4ZlzupnUfqDb2ZDf8KRHK4gIjlI+eQ9lcjaLyuwJHZw3KWsLDcGYsyRw+QinvpyLiOox5Lyz7NTjloI66RnrbwjG463qV6kWfb9rw==~-1~-1~-1; RT="z=1&dm=nike.com&si=5a3614b3-d9a6-469a-934c-54ee8b0c34da&ss=lceu1ugn&sl=g&tt=rvo&bcn=%2F%2F684dd312.akstat.io%2F&ld=1w75u"; bm_sv=1F59CB6FCE959D89B35CBAEB9F39EBFA~YAAQXRjdWN5FTjOFAQAADhPYchLiQXUfO5m72vttaioiONJibq0TL57kvZwlJTbjroe97UcWoJddSuDqJpCH779C3fgaNwNgFB2vI5UuyRCHCdilOiOsztUyaBkOfnA17VvTiWruCrtNv4qWSXpa9KsIuYYcMZMazKp+DBulLoHvlXWBKJfu1CI7gmzxbqykGK38GCOsbhJ1GKSzVi56jDQ2rR6Gcuram3CopjsDWk3+l4wYCe3pjxZ0S4tpyNk=~1',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.json())

obj = response.json()
amount_sneakers = len(obj['objects'])

is_exclusive_access = obj['objects'][0]['productInfo'][0]['merchProduct']['exclusiveAccess']
title = obj['objects'][0]['publishedContent']['properties']['coverCard']['properties']['altText']
date = obj['objects'][0]['productInfo'][0]['merchProduct']['commerceStartDate']
sku = obj['objects'][0]['productInfo'][0]['merchProduct']['styleColor']
price = obj['objects'][0]['productInfo'][0]['merchPrice']['currentPrice']
img_url = obj['objects'][0]['publishedContent']['properties']['coverCard']['properties']['landscapeURL']

print(is_exclusive_access)
print(title + date)
print(sku)
print(price)
print(img_url)


