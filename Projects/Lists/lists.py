pages = ["Home", "About", "Features", "Contact"]

for i in pages:
    print(i)

print()
print(pages[-1], (pages[3]))
print(' '.join(pages))

pages += ["FAQ"]
print(pages)

pages_new = pages
print(' '.join(pages_new))

a = b = c = d = e = f = g = pages = pages_new
print("Navigation Bar")
f.append("Login")
print(g)
print(' '.join(pages_new))
f.append("Register")

print("Final Navigation Bar")
print(' '.join(d))
