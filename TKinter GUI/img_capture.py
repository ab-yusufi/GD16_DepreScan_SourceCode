import cv2


def main():
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    cv2.imwrite(filename='img.jpg', img=frame)
    webcam.release()
    print("Processing image...")
    img_ = cv2.imread('img.jpg', cv2.IMREAD_ANYCOLOR)
    print("Image saved!")


if __name__ == "__main__":
    main()