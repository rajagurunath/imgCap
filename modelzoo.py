# -*- coding: utf-8 -*-
"""modelzoo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tensorflow/lucid/blob/master/notebooks/modelzoo.ipynb

# Lucid Modelzoo

If you want to study techniques for visualizing and understanding neural networks, it's important to be able to try your experiments on multiple models.

 [Lucid](https://github.com/tensorflow/lucid) is a library for visualizing neurla networks.
 As of lucid v0.3, we provide a consistent API for interacting with 27 different vision models.

## General Setup
"""

# Expanded modelzoo is only available as of lucid v0.3
!pip install --quiet lucid==0.3

import numpy as np
import tensorflow as tf

from lucid.misc.io import show, load
import lucid.optvis.objectives as objectives
import lucid.optvis.param as param
import lucid.optvis.render as render
import lucid.optvis.transform as transform

"""## Import Modelzoo"""

# Lucid's modelzoo can be accessed as classes in vision_models
import lucid.modelzoo.vision_models as models

# ... or throguh a more systematic factory API
import lucid.modelzoo.nets_factory as nets

"""## List Models

As of lucid v0.3
"""

print ""
print "Model".ljust(27), " ", "Dataset"
print ""
for name, Model in nets.models_map.iteritems():
  print name.ljust(27), " ", Model.dataset

models.InceptionV4_slim.layers

"""## List Model Layers"""

models.VGG16_caffe.layers

"""## Show Model Graph"""

model = models.VGG16_caffe()
model.load_graphdef()

model.show_graph()

"""## Visualize Neuron

See the [lucid tutorial](https://colab.research.google.com/github/tensorflow/lucid/blob/master/notebooks/tutorial.ipynb) to learn more.

We pick `InceptionV4/InceptionV4/Mixed_6b/concat` from above, and chose to focus on unit 0.
"""

model = models.VGG16_caffe()
model.load_graphdef()

_ = render.render_vis(model, "conv1_1/conv1_1:0")

"""## Caricature

See the [inversion and caricature notebook](https://colab.research.google.com/github/tensorflow/lucid/blob/master/notebooks/misc/feature_inversion_caricatures.ipynb) to learn more.
"""

from lucid.recipes.caricature import feature_inversion

img = load("https://storage.googleapis.com/lucid-static/building-blocks/examples/dog_cat.png")

model = models.VGG16_caffe()
model.load_graphdef()

result = feature_inversion(img, model, "conv1_1/conv1_1", n_steps=512, cossim_pow=0.0)
show(result)