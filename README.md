# image-to-particle
### 画像、動画をパーティクルに変換  
<br>

## 開発環境<br>
Minecraft Java Edition 1.18.2<br>
Python 3.8.7<br>

## 動画変換の際の注意
フレームの数だけmcfunctionが生成されるので30秒以下の動画を推奨します。

## Usage
リリースからダウンロードするのが一番楽です。  
ソースから動かす場合は以下の通りです。  

**1.** [Python3](https://www.python.org/downloads/)のインストール<br><br>
**2.** 依存ライブラリのインストール  
```
pip install -r requirements.txt
```
<br>

**3.** 変換  


* 画像

```
python image_to_particle.py
```

* 動画
```
python video_to_particle.py
```
<br>

**4**. 出力されたmcfunctionをワールドに導入しfunctionを実行してください。<br>
動画の場合は生成されたフォルダをdatapacksフォルダに導入し、
```mcfunction
function #video_ファイル名:loop
```
をリピートコマンドブロック等で毎tick実行すれば再生できます。
