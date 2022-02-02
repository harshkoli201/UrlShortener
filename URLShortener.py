import pyshorteners

url = input("Enter the URL to shorten: ")

typeurl = pyshorteners.Shortener(api_key='a489c6c0fd716e34ae803a957aa37ce1d192cf72')
short = typeurl.bitly.short(url)


print("The Shortened URL is: " + short)

