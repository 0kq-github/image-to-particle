# coding: utf-8

import cv2
import os
import image_to_particle
import ffmpeg
import config
from tqdm import tqdm
import shutil
import json

mp4path = input("ファイル名を入力してください(動画): ")
resultpath = "./video_" + os.path.splitext(os.path.basename(mp4path))[0]
count = 0

class video():

  def save_all_frames(self, video_path, dir_path, basename, target_player, ext='jpg'):
      convert_path = f"{basename}_{config.fps}.mp4"
      try:
        os.remove(convert_path)
      except:
        pass
      print("フレームレートを変換中...")
      ffmpeg.input(video_path).trim(start=0).filter("fps",fps=config.fps, round="up").output(convert_path).run(quiet=True)

      cap = cv2.VideoCapture(video_path)
      frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

      if not cap.isOpened():
          return

      shutil.copytree("base",dir_path,dirs_exist_ok=True)
      os.makedirs(f"{dir_path}/data/video_{basename}/functions", exist_ok=True)
      os.makedirs(f"{dir_path}/data/video_{basename}/tags/functions", exist_ok=True)
      

      print("mcfunctionに書き出し中...")
      count = 0
      with tqdm(total = frame_count) as progress:
        while True:
          ret, frame = cap.read()
          if ret:
            count += 1
            image_to_particle.main(frame,f"{dir_path}/data/video_{basename}/functions/{count}")
            progress.update(1)
          else:
              break

      
      with open(f"{dir_path}/data/minecraft/tags/functions/load.json",mode="w",encoding="utf-8") as f:
        f.write(json.dumps({"values":[f"video_{basename}:load"]}))
      with open(f"{dir_path}/data/video_{basename}/tags/functions/loop.json",mode="w",encoding="utf-8") as f:
        f.write(json.dumps({"values":[f"video_{basename}:loop"]}))
      with open(f"{dir_path}/data/video_{basename}/functions/load.mcfunction", mode="w",encoding="utf-8") as f:
        f.write(f"scoreboard objectives add video_{basename} dummy\n")
      with open(f"{dir_path}/data/video_{basename}/functions/loop.mcfunction", mode="w",encoding="utf-8") as f:
        f.write(f"scoreboard players add {target_player} video_{basename} 1\n")
        scores = []
        for r in range(1,count):
          scores.append(f"execute if score {target_player} video_{basename} matches {r} run function video_{basename}:{r}\n")
        f.writelines(scores)
      print("変換が完了しました！")
      

v = video()
v.save_all_frames(mp4path, resultpath, os.path.splitext(os.path.basename(mp4path))[0] ,config.target ,"png")

