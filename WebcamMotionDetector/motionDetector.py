""" Computer with webcam needed!! """
from datetime import datetime
import cv2, pandas

firstFrame = None

video = cv2.VideoCapture(0)
times = []
df = pandas.DataFrame(columns=["Start", "End"])

while True:
    check, frame = video.read()
    movementDetection = 0
    # Check webcam
    if frame == None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # It gives as less noise to make the comparission later
    gray = cv2.GaussianBlur(gray, (21,21),0)

    if firstFrame is None:
        lastMovementDetection = 0
        firstFrame = gray
        continue

    deltaFrame = cv2.absdiff(firstFrame, gray)
    # To get a B&W image with the difference. We need only the frame that is in the 1 positon.
    threshFrame = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)[1]
    threshFrame = cv2.dilate(threshFrame,None,iterations=2)

    # Get Contours to be able to remark them in the video
    (_,contours,_) = cv2.findContours(threshFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        # if the ares is really small it will not be remarked in the video
        if cv2.contourArea(cont) < 2500:
            continue

        movementDetection = 1
        (x, y, w , h) = cv2.boundingRect(cont)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frame", deltaFrame)
    cv2.imshow("Threshold Frame", threshFrame)
    cv2.imshow("Color Frame", frame)
    

    if movementDetection != lastMovementDetection:
        times.append(datetime.now())

    lastMovementDetection = movementDetection
    key=cv2.waitKey(1)
    
    if key==ord('q'):
        break
index = 0
while index < len(times):
    if index + 1 < len(times):
        df = df.append({"Start":times[index], "End":times[index+1]}, ignore_index=True)
    else:
        df = df.append({"Start":times[index], "End":datetime.now()}, ignore_index=True)
    index += 2
df.to_csv("Times.csv")

video.release
cv2.destroyAllWindows