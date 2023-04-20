from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
 "type": "service_account",
  "project_id": "refined-sunup-382223",
  "private_key_id": "8e2645d2e15b7a4448c8c7187d31c7c49a3645aa",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCZc6oAftZF9M1o\n5c6x4Jgjwwtqa47MaTtdg3fWvQVoPNipq79EN8Fp97f0rUHe0GB4IenvmHvGqa8b\nFE7hZhTycWsDepBv4JdnyxK4QZZSySOAMgCHMwfWH2Gwn2SBK0Bj1b3FeTStzGam\nCULOD7gFQfWvo/nSJGLJdntuvD8AGpeYIaDhAY/+UsVOkdAA+zkuxHPK/yGXJdcl\ncpRSRqSXN5LCDjp1yeXhcJ8dpfXlaTI2c8Sx12Zn/q0Kout6CvaRWUl7XgVBbO4k\nnjy2Y5LXNvsg/Tpgi2pJgYlvnTLW0EDa7eZ26lGODPO29uEvorqAzrvnj3aAld0j\n8dCmAknNAgMBAAECggEAC3/pgOQAds75CHVrCgAve+6apRJZFI8w+GRpJK9BqnrK\nLzJEa9Op1kvO011F5HFv6VDRUTf3fqnUtON5YywylwCnk7kpqINc6qsDRMpVfkVo\njauG8prWaYDXN1SamZDTiyfHcvcPBZSd1K+OUWxIJCIPTBGudRsY9B7BnUjU3ShY\nmmSzmSRZ0fhGDrsGyjpsTEf/nk6CORYgD9R1/mKDvBjQR0EMDDkZsEcVzs8dW37m\n5/l7JynO04FQVXwDvru/QdIXt6BIZykYcvfNhHfOby3NLiIWi9pKT9AzKZTpolWN\nm/nX+QzxnN5jus+ydP2BYlkg5m5yISP10UlEkpo6QQKBgQDP4XSC9kVGD009f2gy\n6JGExpLVYq29YKUAeZsR6+y23S1nt6PtPVNVpO2zeWHeUyBbkZUbP9m95bxgj7Hc\nuzXGZ6VdU9m06wVpnlQ7jPwfe59Ll9W+wNVAOlAMiu08GXlcQEAmFBHnOV4uJ/yS\n9MLAtgd5t2PUs4pVvtPObNeK6QKBgQC8+OAqFmIz2dqu0L1BOLx8SNWSir+FG2pL\ntcmnS2TVcIzyJvHuSb5KhsQAfzWpjqg0fdxPRXYZyx8bGCFmT2H1hzaJEDMsDaFT\nmAhxCowHlTHrlh6EUHlGRUWOl5vifDENvMvqsv/kGl9xKKKrq6OhiS3g4KmsmEpg\nKtIEzTFxRQKBgFTPBQqc0Dw55+gr/2WtjhieLq9Rl9IICKj9867HEoa0C18iA4W5\nHDN3muY6ohviy/OvnCZG0V1wyX6XgRetZM3x4PwHRm1R6J5jUrgM15s8gwuDAVfW\nMeoHIDtNvmVjeyiQqdsfGwK7W9n2xEtsAbw/RyN4FwliyhAbTywLKZBpAoGBALAD\nlDA/hxrKuWEJNq5wXUfaQ2vqZndh0MFSQtDbbcFMw0utsLyF3YPnQNtBocccBFpY\nPQNtLJLb2k5PTJTSLekXF1nVSASpcXG+c2ZvL3zEn6nSuvv9ROiKDz7AwkbT7JDi\nIIGsVqKtWea5tcL27UPB1YTXXdNQSj6Gw/YK9hmNAoGAMietd46JHcNKnidAo95L\nSv7TlZCbeQUPV8sEbFs9C/Hs3hyG4c+qaOm2KeHC0ne8SfjVu69ger4Nd9lUpDxC\nT5VAja+QabUsKBn8oNjOnjkColTYVln/EYZcccn3rfwYSqoeDUbJmL7r1ZjeiPe3\n1Wlb57fb5k+KIA/b2VZzRE0=\n-----END PRIVATE KEY-----\n",
  "client_email": "servi-o@refined-sunup-382223.iam.gserviceaccount.com",
  "client_id": "110001377144186716902",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/servi-o%40refined-sunup-382223.iam.gserviceaccount.com"
}

try:
  res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

  print("Loading...")

  soup = BeautifulSoup(res.text, 'html.parser')

  info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
  
  print(info)

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('weather_00')
  blob = bucket.blob('weather_info.txt')

  blob.upload_from_string(info + '\n')

  print('File uploaded.')

  print("Finished.")
except Exception as ex:
  print(ex) 