#!/usr/bin/python

tag = '<a href="https://www.offensive-security.com/blog">Blog</a>'
#url = tag[9:48]
start = "http"
end = "\">"

print(tag.index(start))
print(tag.index(end))

url = tag[tag.index(start):tag.index(end)]

print(url)
