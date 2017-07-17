from PIL import Image							#must have pillow installed
import time
import sys

def main():
	file_paths = sys.argv[1:]					#drop file onto script to ruin it
	filename = file_paths[0]

	print("Let me JPEG that for you")
	time.sleep(2)

	img = Image.open(filename)
	x = img.size[0]
	y = img.size[1]

	for i in range(1, 21):						#exponential resizing ~ image must be greater than 20x20
		img = Image.open(filename)				#need to reopen image after saving it
		img = img.resize((int(x/i), int(y/i)))			#scale down by factor of i
		img = img.resize((x, y))				#bring image back to regular size
		img.save(filename)					#save the image
		#img.save("{}.jpg".format(i))
		time.sleep(1)						#wait a second so that it can save correctly

main()