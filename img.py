from PIL import Image
import requests
from io import BytesIO

img1_offset = (248, 284)
img2_offset = (1108, 284)
party_hat1_offset = (200, 50)
party_hat2_offset = (1060, 50)


def draw_image(img1, img2):
    background = Image.open("background.png")
    party_hat = Image.open("feesthoed.png").convert("RGBA").resize((350, 350), Image.BILINEAR)
    new_image = Image.new("RGBA", background.size, "WHITE")
    new_image.paste(background, (0, 0), background)

    img1_pil = Image.open(img1).convert("RGBA").resize((512, 512), Image.BILINEAR)
    img2_pil = Image.open(BytesIO(requests.get(img2).content)).convert("RGBA").resize((512, 512), Image.BILINEAR)

    new_image.paste(img1_pil, img1_offset, img1_pil)
    new_image.paste(img2_pil, img2_offset, img2_pil)
    new_image.paste(party_hat, party_hat1_offset, party_hat)
    new_image.paste(party_hat, party_hat2_offset, party_hat)
    new_image.save('banner.png', "PNG")
