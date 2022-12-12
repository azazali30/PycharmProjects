from PIL import Image
import sys
import os

source_folder = sys.argv[1] if len(sys.argv) >= 2 else "../Pokedex"
dest_folder = sys.argv[2] if len(sys.argv) >= 3 else "../dest_pokedex"

if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)
os.chdir(source_folder)
converted_images = []
for img_path in os.listdir():
    img = Image.open(f'{source_folder}/{img_path}')
    #suffix_index = int(img_path.index('.jpg'))
    #img.save(f"{dest_folder}/{img_path[0:suffix_index]}.png", "png")
    clean_name = os.path.splitext(img_path)
    print(clean_name)
    img.save(f"{dest_folder}/{clean_name[0]}.png")
