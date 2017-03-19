# TensorFlow Demo

* TensorFlowのインストール
~~~
https://www.tensorflow.org/install/
~~~

* jupyterのインストール
~~~
pip install jupyter 
~~~

* opencvのインストール
~~~
brew install opencv
brew info opencv
~~~

* 初めにイメージファイルを入れるデェレクトリの生成
~~~
bash ./init.sh
~~~

* notebook → tensorboard
~~~
jupyter notebook
tensorboard --logdir image/train
~~~

* 一気にRun
~~~
bash ./run.sh
~~~