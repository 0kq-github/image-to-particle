# image-to-particle
### 画像、動画をパーティクルに変換  
<br>

開発環境<br>
Minecraft Java Edition 1.18.2<br>
Python3.8.7<br>

## Usage
1. Python3のインストール  
2. 依存ライブラリのインストール  
```
pip install -r requirements.txt
```
3. 変換  
  
 画像:
```
python image_to_particle.py
```
 動画:
```
python video_to_particle.py
```
4. 出力されたmcfunctionをワールドに導入しfunctionを実行してください。　　
動画の場合は生成されたフォルダをdatapacksフォルダに導入し、
```mcfunction
function #video_ファイル名:loop
```
をリピートコマンドブロック等で毎tick実行すれば再生できます。