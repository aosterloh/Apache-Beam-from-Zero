import apache_beam as beam

pipeline =  beam.Pipeline()

tornadoes = (pipeline
 | beam.io.ReadFromText('data/gsod_small.csv')
 | beam.io.textio.WriteToText('extracted_tornados')   
)
pipeline.run()
