alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'v', 'u', 'w', 'x', 'y', 'z' ]
# Ceasers
print("Ceasers")

txt = "N QNPJ HNUMJWX"

def decipher(txt, key):
    res = []
    for i in range(len(txt)):
        if i == " ": continue
        res.append(alphabets[txt.index(i) - key])

