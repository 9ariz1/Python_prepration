import qrcode

# QRCode object banayein taaki hum colors set kar sakein
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,  # Border hona bahut zaroori hai scan ke liye
)

qr.add_data('Hello! Yeh mera pehla QR Code hai.')
qr.make(fit=True)

# Yahan hum colors fix kar rahe hain (Black aur White)
img = qr.make_image(fill_color="black", back_color="white")

img.save('fixed_qrcode.png')
print("Ab 'fixed_qrcode.png' check karein, yeh pakka scan hoga!")