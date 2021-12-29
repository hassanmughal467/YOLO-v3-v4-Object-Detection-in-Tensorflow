#import subprocess
import os
image_or_video_path = 'E:/C_DOWNLOADS/test_video6.mp4' #video or image path/or for live video put zero intead of path "0" 
#subprocess.run(['python','detect.py','--source',image_or_video_path,'--weights','last.pt'])
os.system(f'python detect.py --source {image_or_video_path} --weights last.pt')
# python .\detect.py --source 'Q:\Test\1.mp4' --weights .\last.pt