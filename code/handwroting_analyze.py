import cv2
import numpy as np

def analyze_s_traits(contour, image):
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / h
    hull = cv2.convexHull(contour)
    hull_points = len(hull)
    personality_traits = []

    if aspect_ratio > 1.0:
        personality_traits.append("Creative, expressive")
    elif aspect_ratio < 0.8:
        personality_traits.append("Practical, methodical")

    if hull_points > 10:
        personality_traits.append("Social, adaptable")
    elif hull_points < 8:
        personality_traits.append("Logical, direct")
    if personality_traits:
        print("Personality Traits:", ", ".join(personality_traits))
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

def analyze_t_traits(contour, image):
    x, y, w, h = cv2.boundingRect(contour)
    if h >= 580: 
        print("Detected a tall 't':")
        print("Aspect Ratio: Higher than usual")
        print("Crossbar Height: Relatively high up the stem")
        print("Width to Height Ratio: Lower")
        print("Personality Traits: introvert")
    elif h <= 300: 
        print("Detected a short 't':")
        print("Aspect Ratio: Around standard")
        print("Crossbar Height: Lower down the stem")
        print("Width to Height Ratio: Higher")
        print("Personality Traits: smart")
    else:  
        print("Detected a standard 't':")
        print("Aspect Ratio: Around standard")
        print("Crossbar Height: Midway down the stem")
        print("Width to Height Ratio: Standard")
        print("Personality Traits: extrovert")
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

def analyze_a_traits(contour, image):
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / h
    area = cv2.contourArea(contour)
    personality_traits = []

    if aspect_ratio > 1.0:
        personality_traits.append("Open-minded, communicative")
    elif aspect_ratio < 0.8:
        personality_traits.append("Detail-oriented, focused")

    if area > 100:
        personality_traits.append("Generous, expansive")
    elif area < 50:
        personality_traits.append("Conservative, reserved")

    if personality_traits:
        print("Personality Traits:", ", ".join(personality_traits))

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

def main():
    letter = input("Enter the letter to analyze (s, t, a): ").lower()
    image_path = input("Enter the path to the image file: ")

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Unable to load image")
        return

    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if h > 10 and w > 5: 
            if letter == 's':
                print(f"Dimensions of 's': {w}x{h}")
                analyze_s_traits(contour, image)
            elif letter == 't':
                print(f"Length of 't': {h}")
                analyze_t_traits(contour, image)
            elif letter == 'a':
                print(f"Dimensions of 'a': {w}x{h}")
                analyze_a_traits(contour, image)
            else:
                print("Error: Unsupported letter")
                return

    cv2.imshow('Detected Letters', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
