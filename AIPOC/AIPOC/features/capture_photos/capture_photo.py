import cv2
def capture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    i=-10
    while i<5:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        i+=1
    img_name = "photo.png"
    cv2.imwrite(img_name, frame)
    print("written!")
    cam.release()
    cv2.destroyAllWindows()