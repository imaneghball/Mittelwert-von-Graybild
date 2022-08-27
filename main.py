import cv2
img=cv2.imread("lenagray.jpg",0)
def mittelwert(img):# Mittlewert von Graubilder
    w,h=img.shape
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    mittel=0
    for i in range(256):
        mittel=((hist[i]/(w*h))*i)+mittel
    return mittel
def Abweichung(img):
    w,h=img.shape
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    a = 0
    m=mittelwert(img)
    for i in range(256):
        a=(((i-m)**2)*hist[i])/(w*h)+a
    return (a)**0.5
print(f"MittelWert ist gleich:{mittelwert(img)}")
print(f"Abweichung ist gleich: {Abweichung(img)}")
cv2.imshow("add",img)
while True:
    k=cv2.waitKey(0) & 0XFF
    if k==27: break
