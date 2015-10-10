import urllib.request

# url = "http://duckduckgo.com/html"
# payload = {'q':'python'}
# details = urllib.parse.urlencode({'q':'python'})
# details = details.encode('UTF-8')
# request = urllib.request.Request(url,details)
# request.add_header("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13")
# r = urllib.request.urlopen(request,details)
# responseData = urllib.request.urlopen(r).read().decode('utf8', 'ignore')
# print(responseData)

details = urllib.parse.urlencode({ 'username': 'cswart@outlook.com', 'password': 'hackthebank22' })
details = details.encode('UTF-8')
url = urllib.request.Request('https://rbs.openbankproject.com/oauth/authorize?oauth_token=KGT1342FRALQGKQIJMT2RI1SD42WXVWP1X2SC3HK', details)
url.add_header("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13")

responseData = urllib.request.urlopen(url).read().decode('utf8', 'ignore')
print(responseData)
