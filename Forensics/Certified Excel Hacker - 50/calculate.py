import hashlib
import base64
answer = ""
#16777216

def encode(answer):
    m = hashlib.sha1()
    m.update(answer.encode("utf-8"))
    a = m.digest()
    b = base64.encodestring(a)
    b = b.decode().split("\n")[0]
    return b
#16777216
for i in range(16777216):
    answer = encode(answer)
print (answer)
