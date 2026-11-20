import http.client

conn = http.client.HTTPSConnection("api.scrapingant.com")

conn.request("GET", "/v2/general?url=https%3A%2F%2Fautofactsdb.com%2Fpart%2F&x-api-key=e564b487cef04cbd97a2321329b8bfe4")

res = conn.getresponse()
data = res.read()

conn.close()

text = data.decode("utf-8")

with open('..\\html_pages_collected\\autofactsdb.html', 'w', encoding= 'utf-8') as f:
    f.write(text)



