import os
from PIL import Image

def scale_image(image_path, width, height):
    img = Image.open(image_path)
    h, w, c = img.shape;
    if h == height or w == width:
        return img
    img_resized = img.resize((width, height), Image.LANCZOS)
    return img_resized

def main():
    target_width = 224
    target_height = 350
    cwd = os.getcwd()
    png_images = [file for file in os.listdir(cwd) if file.lower().endswith('.png')]

    for image in png_images:
        try:
            image_path = os.path.join(cwd, image)
            img_resized = scale_image(image_path, target_width, target_height)
            img_resized.save(image_path)
            print(f"resize image '{image}'")
        except Exception as e:
            print(f"error while resizing '{image}': {str(e)}")

if __name__ == "__main__":
    main()
