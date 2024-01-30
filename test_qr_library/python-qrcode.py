import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer,
                                               RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer)
from qrcode.image.styles.colormasks import (SolidFillColorMask, RadialGradiantColorMask, SquareGradiantColorMask,
                                            HorizontalGradiantColorMask, VerticalGradiantColorMask, ImageColorMask)

# Image, ImageDraw)

# colors
main_color = (25, 25, 112)
# main_color = (164, 1, 87)


# qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% or less errors can be corrected.
# qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_`CORRECT_Q, # About 25% or less errors can be corrected.
# qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, # About 30% or less errors can be corrected.
# (default) About 15% or less errors can be corrected.
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,
                   version=1,
                   box_size=10,
                   border=1,
                   )
qr.add_data('Hello, World #2!!!!')
# qr.add_data('https://nextjs.org/')


# img_1 = qr.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(front_color=main_color),
# module_drawer = RoundedModuleDrawer())
img_1 = qr.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(),
                      module_drawer=RoundedModuleDrawer())
# img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(),
# module_drawer=VerticalBarsDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage,
                      color_mask=VerticalGradiantColorMask(top_color=main_color,
                                                           # edge_color=(141, 90, 243)
                                                           bottom_color=(164, 1, 87)
                                                           ),
                      module_drawer=CircleModuleDrawer())
img_3 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
                      embeded_image_path="circle-transparent-background.png")

img_1.save("img_1.png")
img_2.save("img_2.png")
img_3.save("img_3.png")
