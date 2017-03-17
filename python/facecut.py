import cv2
import os
from os import path

def faceCut(path):
    # 定数
    FACE_PATH = 'ayana1.jpg'
    FACE_COLOR = (255, 0, 0)
    IMAGE_SIZE = 112

    # cascadeファイルをロードする
    cascades_dir = "python/haarcascades/haarcascade_frontalface_alt2.xml"
    cascade_f = cv2.CascadeClassifier(cascades_dir)
    
    # 画像を読み込む
    img = cv2.imread('image/original/' + path)

    # グレイスケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 検出して四角で囲む
    face = cascade_f.detectMultiScale(gray)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), FACE_COLOR, 2)

    # 切り抜き
    face = img[y:y+h, x:x+h]
    face = cv2.resize(face, (IMAGE_SIZE, IMAGE_SIZE))

    #認識結果の保存
    cv2.imwrite('image/cut/' + path, face)

# メイン
if __name__ == '__main__':
  files = os.listdir('./image/original')
  for file in files:
      print(file)
      faceCut(file)