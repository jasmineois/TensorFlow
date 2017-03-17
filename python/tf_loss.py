""" lossを計算する関数

引数:
    logits: ロジットのtensor, float - [batch_size, NUM_CLASSES]
    labels: ラベルのtensor, int32 - [batch_size, NUM_CLASSES]

返り値:
    cross_entropy: 交差エントロピーのtensor, float

"""
def loss(logits, labels):
    # 交差エントロピーの計算
    cross_entropy = -tf.reduce_sum(labels*tf.log(logits))
    # TensorBoardで表示するよう指定
    tf.scalar_summary("cross_entropy", cross_entropy)
    return cross_entropy