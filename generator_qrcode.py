import segno

qrcode = segno.make_qr("https://raclette.my.canva.site/affiche-consignes-toilettes-propres-bleu")
qrcode.save(
    "qrcode/test.png",
    scale=10,
    dark="#FFFFFF",
    light="#00ff0000",
)