# data ディレクトリ生成
if [ ! -d data ] ; then
    mkdir data
    echo "make data dir"
else
    echo "exist data dir"
fi

# image ディレクトリ生成
if [ ! -d image ] ; then
    mkdir image
    echo "make image dir"
else
    echo "exist image dir"
fi

# サブディレクトリ生成
if [ ! -d image/cut ] ; then
    mkdir image/cut
    echo "make image cut"
else
    echo "exist image cut"
fi
if [ ! -d image/original ] ; then
    mkdir image/original
    echo "make image original"
else
    echo "exist image original"
fi
if [ ! -d image/train ] ; then
    mkdir image/train
    echo "make image train"
else
    echo "exist image train"
fi
