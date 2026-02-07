import cv2

image = cv2.imread("graph text.png")

if image is None:
    print("Error: Image not found")
    exit()

print("1. Save image")
print("2. Find dimensions")
print("3. Display image")
print("4. Convert to grayscale")

choose = int(input("Enter your choice: "))

if choose == 1:
    success = cv2.imwrite("saved_image.png", image)
    if success:
        print("Image saved successfully")
    else:
        print("Failed to save image")

elif choose == 2:
    h, w, c = image.shape
    print(f"Height: {h}")
    print(f"Width: {w}")
    print(f"Channels: {c}")

elif choose == 3:
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choose == 4:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Invalid choice")
