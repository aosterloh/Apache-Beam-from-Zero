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


## Running our first pipeline
My examples build up and are loosely based on the Apache Beam example of weather - specifically tornado - data example found here:
https://github.com/apache/beam/tree/master/examples/java/src/main/java/org/apache/beam/examples/complete

The above example reads and writes to BigQuery. You can play with the dataset here
https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&t=gsod&page=table

You can play with the dataset and try a quick query, e.g. see the month with the most tornados

```
SELECT month, count(month) as num  
FROM `<YOUR-PROJECT-ID>.gsod.tornados` 
WHERE tornado
GROUP BY month
ORDER BY num desc
```
Next let's make sure running our first Beam pipeline actually works. Just enter 
```
python tornado01.py
```
That should read the small local CSV file and output a local file like `extracted_tornados-00000-of-00001`

## Looking at the code
Let's go through the code, line by line. 

### Import statements
If we want to use apache beam, we have to import it. As we are also dealing with csv files, let's make life easy and import that library too. 
```
import apache_beam as beam
import csv
```

### Setting up the pipeline 


```
if __name__ == '__main__':
   with beam.Pipeline('DirectRunner') as pipeline:
```

```
      airports = (pipeline
         | beam.io.ReadFromText('test_small.csv')
         | beam.Map(lambda line: next(csv.reader([line])))
         | beam.Map(lambda fields: (fields[3], (fields[30])))
         | beam.io.textio.WriteToText('extracted_tornados')
      )
      pipeline.run()
```

