from PIL import Image
import textwrap

def encode_text_as_trollface(text, image_file):
    # Open the template image
    template = Image.open("trollface.png")
    # Convert the text to binary
    binary = ''.join(format(ord(char), '08b') for char in text)
    # Resize the template to fit the binary data
    width = int(len(binary) ** 0.5) + 1
    height = int(len(binary) ** 0.5) + 1
    template = template.resize((width, height))
    # Create a new image with the same dimensions as the template
    image = Image.new('RGBA', (width, height))
    # Overwrite the alpha channel of each pixel with the binary data
    pixels = template.load()
    new_pixels = image.load()
    for i in range(width):
        for j in range(height):
            if i * width + j < len(binary):
                r, g, b, a = pixels[i, j]
                new_pixels[i, j] = (r, g, b, int(binary[i * width + j]) * 255)
            else:
                new_pixels[i, j] = (0, 0, 0, 0)
    # Save the image
    image.save(image_file, format="PNG")

def decode_text_from_trollface(image_file):
    # Open the image
    image = Image.open(image_file)
    # Read the pixels from the image
    pixels = image.load()
    # Convert the binary data to text
    binary = ''
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b, a = pixels[i, j]
            binary += str(int(a / 255))
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    # Format and return the text
    return textwrap.fill(text, width=80)

def encode_text_as_image(text, image_file):
    # Convert the text to binary
    binary = ''.join(format(ord(char), '08b') for char in text)
    # Determine the size of the image needed
    image_size = (int(len(binary) ** 0.5) + 1, int(len(binary) ** 0.5) + 1)
    # Create the image
    image = Image.new('RGBA', image_size)
    # Add the binary data to the image
    pixels = image.load()
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            if i * image_size[0] + j < len(binary):
                r, g, b, a = pixels[i, j]
                pixels[i, j] = (r, g, b, int(binary[i * image_size[0] + j]) * 255)
    # Save the image
    image.save(image_file, format="PNG")

def decode_text_from_image(image_file):
    # Open the image
    image = Image.open(image_file)
    # Read the pixels from the image
    pixels = image.load()
    # Convert the binary data to text
    binary = ''
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b, a = pixels[i, j]
            binary += str(int(a / 255))
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    # Format and return the text
    return textwrap.fill(text, width=80)

userinput = input("Encode or decode? (E/D): ")
if userinput == "E":
    userinput = input("What mode? (T/N): ")
    if userinput == "T":
        userinput = input("Text: ")
        encode_text_as_trollface(userinput,"trollfaceimage.png")
        print("Completed.")
        exit(69420)

    elif userinput == "N":
        userinput = input("Text: ")
        encode_text_as_image(userinput,"image.png")
        print("Completed.")
        exit(69420)
    else:
        print("Incorrect option! Quitting...")
if userinput == "D":
    userinput = input("What mode? (T/N): ")
    if userinput == "T":
        userinput = input("File name? (Must be in this directory): ")
        print(decode_text_from_trollface(userinput))
        print("Completed.")
        exit(69420)
    if userinput == "N":
        userinput = input("File name? (Must be in this directory): ")
        print(decode_text_from_image(userinput))
        print("Completed.")
        exit(69420)
    else:
        print("Incorrect option! Quitting...")
else:
    print("Incorrect option! Quitting...")