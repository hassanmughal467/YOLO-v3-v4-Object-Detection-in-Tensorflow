import cv2




# Colors  >>> BGR Format(BLUE, GREEN, RED)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 242)
GOLDEN = (32, 218, 165)
LIGHT_BLUE = (255, 9, 2)
PURPLE = (128, 0, 128)
CHOCOLATE = (30, 105, 210)
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)

fonts = cv2.FONT_HERSHEY_COMPLEX
fonts2 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
fonts3 = cv2.FONT_HERSHEY_COMPLEX_SMALL
fonts4 = cv2.FONT_HERSHEY_TRIPLEX


Distance_level = 0

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output21.mp4', fourcc, 30.0, (640, 480))


# focal length finder function


def FocalLength(measured_distance, real_width, width_in_rf_image):
	# Function Discrption (Doc String)
	
	focal_length = (width_in_rf_image * measured_distance) / real_width
	return focal_length
# distance estimation function

def centroid(coor):
	s_x,s_y,w,h  = int(coor[0].item()),int(coor[1].item()),int(coor[2].item()),int(coor[3].item())
 
	e_x ,e_y= (w) , (h) 

	cX = int((s_x + e_x) // 2.0)

	cY = int((s_y + e_y) // 2.0)
	return (cX, cY)


def Distance_finder(Focal_Length, real_obj_width, obj_width_in_frame):
	
	distance = (real_obj_width * Focal_Length)/obj_width_in_frame
	return distance



