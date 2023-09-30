import qrcode
# img =qr.make("Hello My name is Prakash")
# img.save("self_Details.png")
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=10)
qr.add_data("https://kharigo.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="Blue")
img.save("Color_qrcode.png"
         )
