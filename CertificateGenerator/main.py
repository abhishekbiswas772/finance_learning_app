from PIL import Image, ImageFont, ImageDraw
import io
import base64

FONT_FILE = ImageFont.truetype(r'CertificateGenerator/font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#000000"
template = Image.open(r'CertificateGenerator/template.png')
WIDTH, HEIGHT = template.size

def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def make_certificates(name):
    image_source = Image.open(r'CertificateGenerator/template.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = textsize(name, font=FONT_FILE)
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2  - 140), name.capitalize(), fill=FONT_COLOR, font=FONT_FILE)
    img_buffer = io.BytesIO()
    image_source.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    base64_image = base64.b64encode(img_buffer.read()).decode('utf-8')
    img_buffer.close()
    return base64_image

