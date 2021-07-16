import PIL.Image
"""
# ASCII CHARACTERS 
ASCII = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Resizing the image
def resize(image, new_width=5 0):
	width, height = image.size
	ratio = height / width
	new_height = int(new_width * ratio)
	resized_image = image.resize((new_width, new_height))
	return resized_image

# Converting the Image into BnW
def gray(image):
	grayscale = image.convert('L')
	return grayscale

# Assign each ASCII char
def ASCIIfy(image):
	pixels = image.getdata()
	char = "".join(ASCII[pixel//25] for pixel in pixels)
	return char

# Getting the image from path
new_width=50
def main(n_w):
	path = input("Enter the Path to the photo =")
	try:
		image = PIL.Image.open(path)
	except:
		print("The given path is not valid")

	return image

# Image in ASCII characters but all in one line
new_image_data = ASCIIfy(gray(resize(main(new_width))))

# Making it readble
pixel_count = len(new_image_data)
ascii_image = "\n".join(new_image_data[i:(i*new_width)] for i in range(0, pixel_count, new_width))

# Printing the ASCII IMAGE
print(ascii_image)

# Saving to a file
with open("ASCII.txt", "w") as file:
	file.write(ascii_image)

main(new_width)
"""
chars = ["B","S","#","&","@","$","%","*","!",":","."]


def find():
	path = input("Enter the Path to the photo =")
	try:
		Image = PIL.Image.open(path)
	except:
		print(path, "The given path is not valid")

	return Image


img = find()

# resize the image
width, height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))
# new size of image

# convert image to greyscale format
img = img.convert('L')

# Pixel Data
pixels = img.getdata()

# replace each pixel with a character from array
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write to a text file.
with open("ascii_image.txt", "w") as file:
	file.write(ascii_image)
	file.close()

with open("ascii_image.txt", "r") as file:
	ASCII_NAME = "".join(i for i in file.readlines())
	print(ASCII_NAME)
	file.close()
