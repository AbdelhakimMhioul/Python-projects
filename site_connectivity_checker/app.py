import urllib.request as urllib

input_url = input("Enter a URL: ")


def main(url):
    print("Site connectivity checker")
    response = urllib.urlopen(url)

    print(f"Connected to {url} successfully")
    print(f"Status code: {response.getcode()}")
    print(f"Content type: {response.info()['Content-Type']}")


main(input_url)
