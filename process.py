# from detect import run 
from detect1 import *
from image_detect import run
import pyttsx3

# ref_image = cv2.imread("Ref_image.jpg")
Known_distance = 90  # Inches

Known_width = 45  # Inches



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(distance1,side1):
	distance1 = round(distance1/12,2)
	engine.say("the distance until the door is  "+str(distance1)+f" Feet and on the {side1} O clock")
	engine.runAndWait()
smaple_co =  run(source = 'Ref_image.jpg',weights = 'last.pt',nosave= False,sample=True)
def get_sample(co):
    w  =  (int(co[0].item()),int(co[1].item()),int(co[2].item()),int(co[3].item()) )
    return w
w = get_sample(smaple_co)


Focal_length_found = FocalLength(Known_distance, Known_width,w[2]-w[0])#(ref_image.shape[1]/2)+10)

def get_route(img,cent):
	diff = img.shape[1]/9
	start = 8
	for i in range(1,11):
		if i==6:	
			start=0
		if int(cent[0])<=(i*diff):
			if i==1:
				dir1 = start
			else:
				if i>=6:
					k = i-5
				else:
					k = i-1
				dir1= start+k
			break
	return dir1
	

def get_coordinates(coor,img,old_d,source):
	obj_x, obj_y, obj_w, obj_h = int(coor[0].item()),int(coor[1].item()),int(coor[2].item()),int(coor[3].item())
	cent = centroid(coor)
	# mid  = img.shape[1]//2
	dir1 = get_route(img,cent)
	obj_width_in_frame = obj_w
	if obj_width_in_frame != 0:
		Distance = Distance_finder(Focal_length_found, Known_width, obj_width_in_frame-obj_x)
		Distance = round(Distance/12,2)
		d= str(Distance).split(".")[0]
		cv2.putText(img, f"Distance {d}- {dir1} O'clock",
					(obj_x-6, obj_y-6), fonts, 0.5, (0,255,0), 1)
		cv2.circle(img, cent, 2,GREEN, 4)
		if d.isdigit() and source=='0':
			if (int(d)-old_d >= 20) or (int(d)+20 <= old_d):
				old_d = int(d)
				speak(d,dir1)
	return img,old_d 