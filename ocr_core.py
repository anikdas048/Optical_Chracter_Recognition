try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    # This function will handle the core OCR processing of images.

    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and
    # pressers to detect the string in the image
    return text  # Then we will print the text in the image


print(ocr_core('images/ocr_image_1.png'))