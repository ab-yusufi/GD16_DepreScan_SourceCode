from fer import FER
import cv2
import pprint
import os

def main():
    img = cv2.imread("img.jpg")
    detector = FER()
    main.emotion, score = detector.top_emotion(img)
    pprint.pprint(main.emotion)
    # cv2.imshow(emotion , img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    os.remove("img.jpg")


if __name__ == "__main__":
    main()