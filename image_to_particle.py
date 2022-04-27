import cv2
import numpy as np
import os
import config


def main(img,name):
  height = img.shape[0]
  width = img.shape[1]
  shape_int = config.max_pixel
  if height >= width:
    mag = shape_int / height
    img = cv2.resize(img, (int(width*mag) ,shape_int))
  elif height <= width:
    mag = shape_int / width
    img = cv2.resize(img, (shape_int, int(height*mag)))
  if img.ndim == 3:  
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
  else:
      img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

  img_array = np.asarray(img)
  y = shape_int
  lines = []
  for i in img_array:
    x = shape_int
    for v in i:
      command = f"particle dust {round(v[0] / 256, 8)} {round(v[1] / 256, 8)} {round(v[2] / 256, 8)} {round(v[3] / 255 * 0.5, 6)} ^{round(x*0.1,1)} ^{round(y*0.1,1)} ^ 0 0 0 0 1 force\n"
      x -= 1

      lines.append(command)
    y -= 1
  with open(f"{name}.mcfunction",mode="w",encoding="utf-8") as f:
    f.writelines(lines)
  

if __name__ == "__main__":
  img_path = input("ファイル名を入力してください(画像): ")
  img = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
  name = os.path.splitext(os.path.basename(img_path))[0]
  main(img,name)
  print(f"変換が完了しました！\nファイル名: {name}.mcfunction")
