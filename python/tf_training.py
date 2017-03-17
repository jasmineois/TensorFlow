""" 訓練のopを定義する関数

引数:
    loss: 損失のtensor, loss()の結果
    learning_rate: 学習係数

返り値:
    train_step: 訓練のop

"""
def training(loss, learning_rate):
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)
    return train_step