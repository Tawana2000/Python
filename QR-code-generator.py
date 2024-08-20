import pyqrcode

text = 'https://www.unitedautorepairandbody.com/'
qr_code = pyqrcode.create(text)
qr_code.svg('qr_code.svg', scale = 8)