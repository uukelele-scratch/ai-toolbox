# Imports
import scratchattach as sa
import scratchgpt
import stablediff

# Setup
session = sa.login("username", "password")
cloud = session.connect_cloud("1088420865")
client = cloud.requests(respond_order="finish",no_packet_loss=True)

@client.request
def ping():
	print("[toolbox] pinged!")
	return "pong"

@client.event
def on_ready():
	print("[toolbox] Cloud handler is running")

@client.request
def oldscratchgpt(msg, usr):
	response = scratchgpt.respondto(msg)
	return response

@client.request
def gen_image(prompt, usr):
    # These are here for the filter, okay!
	MATURE_KEYWORDS = ['nude', 'sex', 'porn', 'erotic', 'adult', 'nsfw', '18+', 'fetish', 'explicit', 'sensual', 'xxx', 'strip', 'lingerie', 'sexual', 'mature', 'inappropriate', 'kink', 'penis', 'vagina', 'naked', 'sexy']
	prompt = prompt.lower()
	words = prompt.split(" ")
	for keyword in MATURE_KEYWORDS:
		for word in words:
			if word == keyword:
				return "MATURE"
	image_data = stablediff.generate_image(prompt)
	return image_data

@client.request
def uril():
	return stablediff.what_uril()

client.start()