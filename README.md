# MNIST

The MNIST database contains thousands of images of handwritten characters.

## Links

- [MNIST](http://yann.lecun.com/exdb/mnist/)
- [Tensorflow MNIST](https://www.tensorflow.org/tutorials/layers)

## Usage

```bash
python -m virtualenv .venv

./.venv/Scripts/activate.ps1

pip install -r requirements.txt

python cnn_mnist.py
```

## Visualizing with tensorboard
> Served on http://localhost:6006

```bash
tensorboard --logdir ./tmp/mnist_convnet_model
```