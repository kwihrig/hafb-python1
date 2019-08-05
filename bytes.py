"""
Learn about bytes
Bytes are similar to str type, but they are a swquence of
bytes instead of Unicode code points.

Use for raw binary data, fixed width records, single-byte encoding: ASCII

Use the byte() constructor
"""
d= b'data'
print (d, type(d))

info = b'some bytes here'
#SPlit the bytes using split() method for bytes
print (info.split())

# Encoding Alt+ 162 = ó
message = "Vamos al zoológico"
print (message)
# Encode the string
data = message.encode("utf-8")
print (data)
# Decoding the string
new_message = data.decode ("utf-8")
print (new_message)