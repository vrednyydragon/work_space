# README.md

## Test QR Library

This project is a Python-based QR code generator. It uses the `qrcode` library to create QR codes with different styles and error correction levels.

### Features

- Generate QR codes with different styles using the `StyledPilImage` image factory.
- Apply different color masks to the QR codes, such as `SolidFillColorMask` and `VerticalGradiantColorMask`.
- Use different module drawers to create unique QR code designs, such as `RoundedModuleDrawer` and `CircleModuleDrawer`.
- Set different error correction levels for the QR codes.

### Requirements

- Python
- qrcode library

### Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run `python-qrcode.py`.

This will generate three QR code images: `img_1.png`, `img_2.png`, and `img_3.png`.

### Customization

You can customize the QR code generation by modifying the `python-qrcode.py` file. Here are some of the things you can change:

- The data encoded in the QR code: Modify the argument to `qr.add_data()`.
- The error correction level: Change the `error_correction` argument when creating the `QRCode` object.
- The QR code style: Change the `image_factory`, `color_mask`, and `module_drawer` arguments to `qr.make_image()`.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
