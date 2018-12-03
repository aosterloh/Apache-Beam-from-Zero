import apache_beam as beam
import csv

if __name__ == '__main__':
   with beam.Pipeline('DirectRunner') as pipeline:

      airports = (pipeline
         | beam.io.ReadFromText('test_small.csv')
         | beam.Map(lambda line: next(csv.reader([line])))
         | beam.Map(lambda fields: (fields[3], (fields[30])))
      	 | beam.io.textio.WriteToText('extracted_tornados')   
      )
      pipeline.run()
