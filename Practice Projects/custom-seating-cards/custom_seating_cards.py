#! python3
# custom_seating_cards.py - Creates invitations from a list of guests.


from PIL import Image, ImageDraw


file = open('guests.txt')
guests = file.read().splitlines()

flower_image = Image.open('flower.jpg')

for guest in guests:
    image = Image.new('RGBA', (288, 360))
    image.paste(flower_image)

    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 288, 360), outline='black', width=1)
    draw.text((20, 20), guest, fill='black')

    image.save(guest+'.png')
