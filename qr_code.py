import qrcode as qr

img = qr.make(
    "https://github.com/navaneeth0041"
)


img.save("github.png")
