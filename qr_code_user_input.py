import qrcode
from PIL import Image

def create_qr_code():
    data = input("Enter the data to encode in the QR code (e.g., URL, text): ")
    fill_color = input("Enter the fill color for the QR code (e.g., 'black'): ")
    back_color = input("Enter the background color for the QR code (e.g., 'white'): ")
    logo_path = input("Enter the path to the logo file (leave blank if no logo): ")
    output_file = input("Enter the output file name (e.g., 'qrcode.png'): ")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    if logo_path:
        try:
            logo = Image.open(logo_path)
            logo_size = (img.size[0] // 5, img.size[1] // 5)
            logo = logo.resize(logo_size, Image.LANCZOS)

            logo_position = (
                (img.size[0] - logo.size[0]) // 2,
                (img.size[1] - logo.size[1]) // 2,
            )
            img.paste(logo, logo_position, mask=logo)
        except Exception as e:
            print(f"Error loading logo: {e}")

    try:
        img.save(output_file)
        print(f"QR code successfully saved as '{output_file}'")
    except Exception as e:
        print(f"Error saving QR code: {e}")

    img.show()

if __name__ == "__main__":
    create_qr_code()
