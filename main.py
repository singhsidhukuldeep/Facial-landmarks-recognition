# import the necessary packages
from imutils import face_utils
import dlib
import cv2

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
model_location = "./model/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_location)

image_loaction = "face.jpg"
camera_feed = False

# load the input image and convert it to grayscale
image = cv2.imread(image_loaction)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def rect_to_bb(rect):
	# take a bounding predicted by dlib and convert it
	# to the format (x, y, w, h) as we would normally do
	# with OpenCV
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y

	# return a tuple of (x, y, w, h)
	return (x, y, w, h)

# detect faces in the grayscale image
rects = detector(gray, 0)

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
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)
    for (x, y) in shape:
        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
        shown_text = str(i)
        if (len(rects) == 1):
            cv2.putText(image, shown_text,(x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
        i += 1

# show the output image with the face detections + facial landmarks
output_filename = "detected_" + image_loaction.replace("./","")
cv2.imwrite(output_filename, image)

# loop over the face detections
for (i, rect) in enumerate(rects):
    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
    for i in range(1,17):
        (x1, y1) = shape[i-1]
        (x2, y2) = shape[i]
        lineThickness = 1
        cv2.line(image, (x1, y1), (x2, y2), (0,0,255), lineThickness)

jawline_output_filename = "jawline_detected_" + image_loaction.replace("./","")
cv2.imwrite(jawline_output_filename, image)

# closing any open windows
try:
    cv2.destroyAllWindows()
except:
    pass
