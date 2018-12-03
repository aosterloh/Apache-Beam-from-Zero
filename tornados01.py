import apache_beam as beam

pipeline =  beam.Pipeline('DirectRunner')

airports = (pipeline
 | beam.io.ReadFromText('test_small.csv')
 | beam.io.textio.WriteToText('extracted_tornados')   
)
pipeline.run()
