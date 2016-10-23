## 1.Docker Toolbox のダウンロード

## 2.Docker Toolbox のインストール

## 3.Docker Quickstart Terminalのアイコンをクリックして起動

## 4.TensorFlowのインストール
docker run -it b.gcr.io/tensorflow/tensorflow:latest-devel

## 5.共有フォルダの設定(OSのフォルダと同期)
<code>

docker run -v /c/Users/jasmine-tensorflow:/jasmine -it b.gcr.io/tensorflow/tensorflow:latest-devel  
ls /jasmine  
python /jasmine/test.py

</code>


docker run -v /c/Users/jasmine-tensorflow:/jasmine-tensorflow -it b.gcr.io/tensorflow/tensorflow:latest-devel

---

### イメージ一覧を得る
docker images
