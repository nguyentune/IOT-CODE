print("Data analyisc")

DA = '	x1^2 + 6*x2 + 9*x3'


import requests
#equation = 'x1 + 2 * x2 + x3'
headers ={}
aio_url = "https://io.adafruit.com/api/v2/nguyentu1402/feeds/da"
x = requests.get(url=aio_url, headers=headers, verify=False)
data = x.json()
print(data["last_value"])
DA = data["last_value"]

def modify_value(x1, x2, x3):
    result = eval(DA)
    print(result)
    return result

a = 5
b = 3
c = 3
d = modify_value(a,b,c)
print(d)