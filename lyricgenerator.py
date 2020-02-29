
from PIL import Image, ImageDraw, ImageFont
import os

def getLines(song):
	f = open("lyrics/%s" % song, "r")
	lines = f.readlines()
	f.close()
	return [line.strip() for line in lines]

def makeDirectory():
	if not os.path.isdir("lyric-images"):
		os.mkdir("lyric-images")

def makeDirectoryForSong(title):
	global counter
	title = title.split(".")[0] # removeing ending
	if (counter < 1):
		search = title
	else:
		search = "%s-%s" % (title, counter)
	if os.path.isdir("lyric-images/%s" % search):
		counter += 1
		return makeDirectoryForSong(title) # recurrency
	else:
		os.mkdir("lyric-images/%s" % search)
		return "lyric-images/%s" % search
	print("did not return")


def nameify(s):
	return s.strip().replace(' ', '').lower().replace('å', 'a').replace('æ', 'ae').replace('ø', 'o')
		

def generateImage(input, path, count):
	zeros = '00'
	if count > 9:
		zeros = '0'
	if count > 99:
		zeros = ''
	width, height = 1920, 100
	fontSize = 68
	img = Image.new('RGB', (width, 1200), color = (0, 0, 0))
	font = ImageFont.truetype("/Users/revy/fonts/Roboto-regular.ttf", fontSize) 
	d = ImageDraw.Draw(img)
	w, h = font.getsize(input)
	d.text(((width - w)/2, height), input, font=font, fill=(255,255,255))
	img.save('%s/%s%s-%s.png' % (path, zeros, count, nameify(input[:20])))

def generateImages(lines, path):
	pad = 2
	count = 0
	tot = len(lines)
	for image in lines:
		generateImage(image, path, count)
		count += 1
		if count % pad == 0:
			print("proccess %3s %%" % round(count/tot*100))
	if round(count/tot*100) != 100 or count % pad != 0:
		print("proccess %3s %%" % round(100))

if __name__ == '__main__':
	global counter
	counter = 0

	title = "sang.txt"
	
	makeDirectory()
	
	lines = getLines(title)
	directory = makeDirectoryForSong(title)

	generateImages(lines, directory)

	print("%i images have been saved to %s " % (len(lines), directory))
