# -*- coding: utf-8 -*-
"""
Created on Sun May 25 18:22:07 2025

@author: demir
"""

import cv2
import sys

def main():
    # Haar cascade XML dosyasının tam yolu
    cascade_path = r"haarcascade_parking.xml"  # Burayı cascade dosyanın tam yolu ile değiştir
    
    # Görsel dosyasının tam yolu
    img_path = r"park2.jpg"  # Burayı görsel dosyanın tam yolu ile değiştir
    
    # Cascade sınıflandırıcıyı yükle
    parking_cascade = cv2.CascadeClassifier(cascade_path)
    if parking_cascade.empty():
        print("HATA: Cascade dosyası yüklenemedi! Yol doğru mu kontrol et.")
        sys.exit()
    
    # Görseli oku
    img = cv2.imread(img_path)
    if img is None:
        print("HATA: Görsel dosyası bulunamadı! Yol doğru mu kontrol et.")
        sys.exit()
    
    # Görseli griye çevir
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Park yeri tespiti yap
    spots = parking_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    
    # Tespit edilen yerlerin etrafına dikdörtgen çiz
    for (x, y, w, h) in spots:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    print(f"Tespit edilen park yeri sayısı: {len(spots)}")
    
    # Sonucu göster
    cv2.imshow("Park Yeri Tespiti", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
