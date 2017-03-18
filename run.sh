# compile
jupyter nbconvert --to python python/FaceCut.ipynb
jupyter nbconvert --to python python/LearnData.ipynb
jupyter nbconvert --to python python/TensorFrow.ipynb

# run
pushd python
python FaceCut.py
python LearnData.py
python TensorFrow.py
popd ../

# view tensorboard
# tensorboard --logdir image/train