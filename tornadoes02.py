import apache_beam as beam
import csv

if __name__ == '__main__':
   with beam.Pipeline('DirectRunner') as pipeline:

      tornadoes = (pipeline 
      		| beam.io.ReadFromText('data/gsod_medium.csv', skip_header_lines=1)
      		| beam.Map(lambda line: next(csv.reader([line])))
      		| beam.Map(lambda fields: (fields[3], (fields[30])))
		    | beam.io.textio.WriteToText('extracted_tornados') 
      	)

      pipeline.run()
