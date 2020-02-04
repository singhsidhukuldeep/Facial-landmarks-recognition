# import the necessary packages
from imutils import face_utils
import dlib
import cv2
import os.path
from os import path
import pathlib
current_path = str(pathlib.Path().absolute())

def detectFaces (image_loaction = "", model_location = ""):

	# checking files
	if (path.exists(current_path + model_location.replace("./",""))):
		raise ValueError('No file found at model_location: ' + model_location)
	if (path.exists(current_path + image_loaction.replace("./",""))):
		raise ValueError('No file found at image_loaction: ' + image_loaction)

	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	print ("Loading model " + model_location)
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(model_location)

	camera_feed = False

	print ("Loading image " + image_loaction)
	# load the input image and convert it to grayscale
	image = cv2.imread(image_loaction)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	def rect_to_bb(rect):
		# take a bounding predicted by dlib and convert it
		# to the format (x, y, w, h)
		x = rect.left()
		y = rect.top()
		w = rect.right() - x
		h = rect.bottom() - y

		# returning a tuple of (x, y, w, h)
		return (x, y, w, h)

	print ("Detecting faces")
	# detect faces in the grayscale image
	rects = detector(gray, 0)
	print (str(len(rects)) + " faces found")

	print ("Detecting facial features")
	# loop over the face detections
	for (i, rect) in enumerate(rects):
	    # determine the facial landmarks for the face region, then
	    # convert the facial landmark (x, y)-coordinates to a NumPy
	    # array
	    shape = predictor(gray, rect)
	    shape = face_utils.shape_to_np(shape)
	    # loop over the (x, y)-coordinates for the facial landmarks
	    # and draw them on the image
	    if (not len(rects) == 1):
	        (x, y, w, h) = face_utils.rect_to_bb(rect)
			# drawing rectangles
	        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)
	    for (x, y) in shape:
			# drawing points
	        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
	        shown_text = str(i)
	        if (len(rects) == 1):
				# drawing point numbers
	            cv2.putText(image, shown_text,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
	        i += 1

	# save the output image with the face detections + facial landmarks
	output_filename = "detected_" + image_loaction.replace("./","")
	cv2.imwrite(output_filename, image)
	print ("Output image with the face detections + facial landmarks saved at: " + output_filename + "\n")

	print ("Drawing Jawline")
	# loop over the face detections
	for (i, rect) in enumerate(rects):
	    # determine the facial landmarks for the face region, then
	    # convert the facial landmark (x, y)-coordinates to a NumPy
	    # array
	    shape = predictor(gray, rect)
	    shape = face_utils.shape_to_np(shape)

	    # loop over the (x, y)-coordinates for the facial landmarks
	    # and draw them on the image for jawline i.e 0-16 points
	    for i in range(1,17):
	        (x1, y1) = shape[i-1]
	        (x2, y2) = shape[i]
	        lineThickness = 1
			# draw jawline
	        cv2.line(image, (x1, y1), (x2, y2), (0,0,255), lineThickness)

	# save the output image with the face detections + facial landmarks + jawline
	jawline_output_filename = "jawline_detected_" + image_loaction.replace("./","")
	cv2.imwrite(jawline_output_filename, image)
	print ("Output image with the face detections + facial landmarks + Jawline saved at: " + jawline_output_filename + "\n")

	# closing any open windows
	try:
	    cv2.destroyAllWindows()
	except:
	    pass
	print ("Done!\n\n")


# for commandline functionality

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print ()

if (len(sys.argv) >= 3):
	image_loaction = sys.argv[1]
	model_location = sys.argv[2]

	detectFaces (image_loaction = image_loaction, model_location = model_location)
