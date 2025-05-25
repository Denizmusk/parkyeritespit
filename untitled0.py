import cv2
import numpy as np



# Görseli yükle (örneğin: otopark görüntüsü)
img = cv2.imread('park.jpg')
img_copy = img.copy()

# Önceden belirlenmiş park yeri bölgeleri [(x, y, w, h), ...]
park_spots = []
start_x = 20

start_y = 350

width = 70
height = 170
gap = 80# Park yerleri arası boşluk

for i in range(11):
    x = start_x + i * gap
    park_spots.append((x, start_y, width, height))

# Her park yerini kontrol et
for i, (x, y, w, h) in enumerate(park_spots):
    roi = img[y:y+h, x:x+w]                    # İlgili bölgeyi kırp
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY_INV)[1]
    white_pixels = cv2.countNonZero(thresh)

    status = "DOLU" if white_pixels > 2000 else "BOŞ"

    # Görselleştir
    color = (0, 0, 255) if status == "DOLU" else (0, 255, 0)
    cv2.rectangle(img_copy, (x, y), (x + w, y + h), color, 2)
    cv2.putText(img_copy, status, (x + 5, y + 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

# Sonuç göster
cv2.imshow("Park Yeri Tespiti", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

