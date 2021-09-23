import cv2

testVideo = cv2.VideoCapture("video/testVideo2.MP4")

frameNo = 0
while(testVideo.isOpened()):
    success, frame = testVideo.read()
    if(success):
        frameNo += 1
    # if(frameNo % 5 == 0):
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

testVideo.release()
cv2.destroyAllWindows()