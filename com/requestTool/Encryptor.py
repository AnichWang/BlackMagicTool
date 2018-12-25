import base64

from Crypto.Cipher import AES


# str不是16的倍数那就补足为16的倍数
def add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)  # 返回bytes


key = '99b2bc8c31e45118'  # 密码

text = 'appkey=f47967e9e88a3644&phone=13301165332&requestId=nsjdl&timestamp=1545209593'  # 待加密文本

to_encrypted_text = 'NCLQ49zd2Nuq6vZ9R9/F/YU0J7rXqQvoQeTufhY5R1h+Be4xQM1/2THd9zGx8syABfhoES2y7jp8N6dSiIIpPOXzmveEJAsaJSPE9JFcFFw\\u003d' # 待解密文本

aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器

encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')  # 加密

text_decrypted = str(aes.decrypt(base64.decodebytes(bytes(to_encrypted_text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))  # 解密

print('加密值：', encrypted_text)

print('解密值：', text_decrypted)