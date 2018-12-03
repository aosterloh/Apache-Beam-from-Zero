# Apache Beam for Python Dummies 
If new to Apache Beam and also new to Python, getting started can be hard. A new SDK plus non-trivial concepts of streaming in a python code that is often hard to read can be daunting. It was daunting for myself so I created this step by step guide starting at zero. It stops where other tutorials picks up. This is to get you started if other code examples left you stranded in the cold. 
## Setup
Follow the steps described here
https://beam.apache.org/get-started/quickstart-py/

Using my mac, these are the steps I followed:

```
pip install --upgrade pip
pip install --upgrade virtualenv
virtualenv tornado --python=python2.7
source tornado/bin/activate # activate your env
cd tornado
pip install apache-beam[gcp]
git clone https://github.com/aosterloh/beam4dummies.git
cd beam4dummies
```


## Our first pipeline
My examples build up and are loosely based on the Apache Beam example of weather - specifically tornado - data example found here:
https://github.com/apache/beam/tree/master/examples/java/src/main/java/org/apache/beam/examples/complete

The above example reads and writes to BigQuery. You can first look at the dataset here
https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&t=gsod&page=table

You can play with the dataset and try a quick query, e.g. see the month with the most tornados
````
SELECT month, count(month) as num  FROM `<YOUR-PROJECT-ID>.gsod.tornados` where tornado
group by month
order by num desc
```

