import qrcode

from PIL import Image


qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4
)

qr.add_data("")

qr.make(fit=True)

img = qr.make_image(fill_color="", back_color="").convert("RGB")

logo = Image.open(
    ""
)
logo_size = (img.size[0] // 5, img.size[1] // 5)
logo = logo.resize(logo_size, Image.LANCZOS)

logo_position = (
    (img.size[0] - logo.size[0]) // 2,
    (img.size[1] - logo.size[1]) // 2,
)
img.paste(logo, logo_position, mask=logo)

img.save("")
