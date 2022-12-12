from PIL import Image, ImageFilter


img = Image.open('../Pokedex/astro.jpg')

# filtered_img = img.convert('L')
# crooked = filtered_img.resize((30,30))
# crooked.save("blur.png", "png")

print(img.size)

new_image = img.resize((400, 400))
#new_image.save("astro_1.png", "png")

print(new_image.size)

img.thumbnail((400, 400))
#img.save("thumbnail.jpg")
print(img.size)