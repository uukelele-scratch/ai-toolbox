import base64
import requests
import io
from PIL import Image
import re

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer API_KEY"}

urilv = []

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)

	if response.status_code == 200:
		return response.content
	else:
		print(f"Error: {response.status_code}, {response.text}")
		return None

def rgb_to_number(rgb):
	r, g, b = rgb
	return r * 256**2 + g * 256 + b

def generate_image(prompt):
	size = 64
	image_bytes = query({
		"inputs": f"{prompt}",
	})

	if image_bytes:
		try:
			image = Image.open(io.BytesIO(image_bytes))
		except UnidentifiedImageError:
			print("Could not identify the image file.")
	else:
		print("No image data received.")

	global urilv
	urilv = uril(image)

	resized_img = image.resize((size, size))
	image_data = []
	for y in range(size):
		row = []
		for x in range(size):
			rgb = resized_img.getpixel((x, y))[:3]
			row.append(rgb_to_number(rgb))
		image_data.append(row)
	return image_data

def uril(image):
	buffered = io.BytesIO()
	image.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
	return f"data:img/jpeg;base64,{img_str}"

def what_uril():
	return urilv