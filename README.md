# Apache Beam for Python Dummies 
If new to Apache Beam and also new to Python, getting started can be hard. A new SDK plus non-trivial concepts of streaming in a python code that is often hard to read can be daunting. It was daunting for myself so I created this step by step guide starting at zero. It stops where other tutorials picks up. This is to get you started if other code examples left you stranded in the cold. 
## Setup
Follow the steps described here
https://beam.apache.org/get-started/quickstart-py/

Using my mac, these are the steps I followed:
'''
pip install --upgrade pip
pip install --upgrade virtualenv
virtualenv tornado --python=python2.7
source tornado/bin/activate # activate your env
pip install apache-beam[gcp]

'''


## Our first pipeline
My examples build up and are loosely based on the Apache Beam example of weather - specifically tornado - data found here:
https://github.com/apache/beam/tree/master/examples/java/src/main/java/org/apache/beam/examples/complete

