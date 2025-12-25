import qrcode

img=input("Enter the data for the QR code: ").strip()
#img=qrcode.make(img)

a=qrcode.make(img)
a.save('Datascienceplaylist300hours.png')

print("QR code generated and saved as 'Datascienceplaylist300hours.png'")