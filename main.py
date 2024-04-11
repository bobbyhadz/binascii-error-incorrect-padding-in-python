# Python binascii.Error: Incorrect padding


import base64

data = bytes('{"name": "bobby hadz"}', encoding='utf-8')

encoded_bytes = base64.b64encode(data)
print(encoded_bytes)  # b'eyJuYW1lIjogImJvYmJ5IGhhZHoifQ=='


decoded_bytes = base64.b64decode(encoded_bytes)
print(decoded_bytes)  # 👉️ b'{"name": "bobby hadz"}'

# 👇️ b'{"name": "bobby hadz"}'
print(base64.b64decode(encoded_bytes[:-2] + b'=='))

# 👇️ True
print(data == base64.b64decode(encoded_bytes[:-2] + b'=='))
