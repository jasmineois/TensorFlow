## 1.Docker Toolbox のダウンロード・インストール
https://www.docker.com/products/docker-toolbox


## 2.Docker Quickstart Terminalのアイコンをクリックして起動
コンソールにてクジラさんが表示
<pre>
                        ##         .  
                  ## ## ##        ==  
               ## ## ## ## ##    ===  
           /"""""""""""""""""\___/ ===  
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~  
           \______ o           __/  
             \    \         __/  
              \____\_______/  
</pre>


## 3.TensorFlowのインストール
`docker run -it b.gcr.io/tensorflow/tensorflow:latest-devel`


## 4.共有フォルダの設定(OSのフォルダと同期)
`docker run -v /c/Users/jasmine-tensorflow:/jasmine -it b.gcr.io/tensorflow/tensorflow:latest-devel`  
`ls /jasmine`  
`python /jasmine/test.py`  


---

### イメージ一覧を得る
docker images
