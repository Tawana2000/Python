# Write a function to extract the domain name from a given URL

def extract_domain(url):
    
    url = url.replace("https://", "").replace("http://", "").replace("www.", "")
    return url.split('/')[0]

print(extract_domain("https://www.example.com/path"))
print(extract_domain("http://test.co.uk"))