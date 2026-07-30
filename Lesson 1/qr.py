import qrcode

# 1. Set up your YouTube link
youtube_url = "https://www.youtube.com/@Awesome_Explorer24"

# 2. Create the QR object with extra settings if you want
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)

qr.add_data(youtube_url)
qr.make(fit=True)

# 3. Customize the colors here! 
# You can use color names like "red", "blue", "purple", or use HEX codes like "#FF0000"
img = qr.make_image(fill_color="blue", back_color="white")

# 4. Save your custom QR code
img.save("youtube_qr_red.png")

print("Custom colored QR code generated successfully!")