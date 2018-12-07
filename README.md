# Apache Beam for Python Dummies 
If new to Apache Beam and also new to Python, getting started can be hard. A new SDK plus non-trivial concepts of streaming can be daunting at first. It was daunting for myself so I created this step by step guide starting at (almost) zero. It stops where other tutorials pick up. This is to get you started if other code examples left you stranded in the cold. We start with processing local files and running beam locally to running Beam on Dataflow on GB of weather data. I will start with batch processing and then move to streaming examples. 

If Beam is new to you, I urge you to stop here and first read through the Apache Beam Programming Guide:
https://beam.apache.org/documentation/programming-guide/


## Setup
With a MAC, follow the steps described below, otherwise have a look here:
https://beam.apache.org/get-started/quickstart-py/

**Unix/Mac setup:**
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

## New to Python?
If so, have a look at attached Jupyter notebook. Just install jupyter using 
```
pip install jupyter
```

Then start Jupyter using
```
jupyter notebook
```

and open the downloaded notebook called `Python Basics for Apache Beam`


## Running our first pipeline (tornado01.py)
My examples build up and are loosely based on the Apache Beam example of weather - specifically tornado - data example found here:
https://github.com/apache/beam/tree/master/examples/java/src/main/java/org/apache/beam/examples/complete

The above example reads and writes to BigQuery. You can play with the dataset here
https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&t=gsod&page=table

You can play with the dataset and try a quick query, e.g. see the month with the most tornadoes

```
#standardSQL
SELECT month, count(month) as num  
FROM `bigquery-samples.weather_geo.gsod` 
WHERE tornado
GROUP BY month
ORDER BY num desc
```
Next let's make sure running our first Beam pipeline actually works. Just enter 
```
python tornado01.py
```
That should read the small local CSV file and output a local file like `extracted_tornadoes-00000-of-00001`. Spoiler, the pipelines does nothing except read data and write it back to file. We will look at other transforms later. 

## Looking at the code
Let's go through the code, line by line. As mentioned above, there are no shortcuts, the Apache Beam Programming Guide is great introduction read before you continue: 
https://beam.apache.org/documentation/programming-guide/

Here is the full code from example 1 (tornadoes01.py)
```
import apache_beam as beam

pipeline =  beam.Pipeline()

tornadoes = (pipeline
 | beam.io.ReadFromText('test_small.csv')
 | beam.io.textio.WriteToText('extracted_tornadoes')   
)
pipeline.run()
```


### Import statements
If we want to use apache beam, we have to import it. 
```
import apache_beam as beam
```

### Creating the pipeline 
For every pipeline we run with beam, we have to create a pipeline object. The `'DirectRunner'` option is not necessary, as it is default, but we are basically running this pipeline locally, so not using Cloud Dataflow as a runtime environment (but we will soon). 

```
pipeline =  beam.Pipeline('DirectRunner')
```

### Read and Write
First we are creating a pipeline and passing data through it. Data is passed from transform to transform as a unmutable PCollection. The first and last transform are usually for reading data from an external source (bounded or unbounded, more on this later) and writing to an external source. 

![Transforms](https://beam.apache.org/images/design-your-pipeline-linear.png)

**Image taken from Apache Beam Programming Guide, in example 1 we just read from source and write to sink**

`ReadFromText` corresponds to the `Input` transform above, will read a file - local in our case - but can also be a file on Google Cloud Storage.  This line is creating a PCollection from our small test csv file, where each element is one line of the file. 

`WriteToText` corresponds to the `Output` above and is used to write the current PCollection to a data sink, in our case again to a local file. This could be a sink on GCS or BigQuery, which we will go through later. 

```
tornadoes = (pipeline
 | beam.io.ReadFromText('test_small.csv')
 | beam.io.textio.WriteToText('extracted_tornados')   
)
```

### Running the pipeline
While the steps before defined our DAG, in order to execute the pipeline, we actually have to run it. So will call `run()` on our pipeline object. 

```
pipeline.run()
```

## Expanding the Pipeline (tornados02.py)

## Looking at the code 
Here is the full code of our 2nd example: 
```
import apache_beam as beam
import csv

if __name__ == '__main__':
   with beam.Pipeline('DirectRunner') as pipeline:

      tornadoes = (pipeline 
      		| beam.io.ReadFromText('test_small.csv', skip_header_lines=1)
      		| beam.Map(lambda line: next(csv.reader([line])))
      		| beam.Map(lambda fields: (fields[3], (fields[30])))
		| beam.io.textio.WriteToText('extracted_tornados') 
      	)

      pipeline.run()
```
We are importing csv lib which makes dealing with reading csv files easier. Also we now execute our code within our `main` module which is helpful when you later have several files to deal with. 

Now we create a pipeline again, but within a `with` statement, which is just a nicer way of dealing with e.g. file streams as cleanup is taken care of, with less lines of code, just get used to it. 

## More transforms
We are reading the same file as above, skipping the header row this time and using a lambda function twice to add 2 more transforms. 

```
tornadoes = (pipeline 
 | beam.io.ReadFromText('test_small.csv', skip_header_lines=1)
 | beam.Map(lambda line: next(csv.reader([line])))
 | beam.Map(lambda fields: (fields[3], (fields[30])))
 | beam.io.textio.WriteToText('extracted_tornados') )
 ```
Pythons lambda functions allow you to specify an anonymous function in one line of code that will only be used once. You could call a function defined outside the transforms or get used to the lambda syntax. Check youtube for understanding lambda functions in Python if this is new to you. 

The following line takes our comma separated line and turns it into csv format. 
```
beam.Map(lambda line: next(csv.reader([line])))
```
And then we just drop all the columns and only pass along the `month` and a boolean value `tornado` stating if there was a tornado or not. 

Run the pipeline to see what it does. 
```
python tornados02.py
```

Alternatively you can repace the small csv file from line 8 with `test_medium.csv` which processes about 25MB locally. Check the output file `less extract*` which should be around 150K lines. 

## Expanding the Pipeline (tornados03.py)
WIP

## Expanding the Pipeline (tornados04.py)
WIP

## Expanding the Pipeline (tornados05.py)
WIP

## Expanding the Pipeline (tornados06.py)
WIP

## Expanding the Pipeline (tornados07.py)
WIP

## Expanding the Pipeline (tornados08.py)
WIP

## Expanding the Pipeline (tornados09.py)
WIP

## Expanding the Pipeline (tornados10.py)
WIP
