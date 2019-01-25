from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import csv
import logging
import sys
import time
from datetime import datetime

import apache_beam as beam
from apache_beam.metrics.metric import Metrics
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import StandardOptions

def run(argv=None):
  parser = argparse.ArgumentParser()

  parser.add_argument('--input',
  required=True,
  default='gs://<your bucket>/weather/gsod_medium.csv', #no need to change, as taken from arguments in run03.sh
  help=('input bucket of test weather data'))

  parser.add_argument(
  '--output',
  required=True,
  default='gs://<your bucket>/output/', #no need to change, as taken from arguments in run03.sh
  help= ('Where to write result to'))

  known_args, pipeline_args = parser.parse_known_args(argv)

  options = PipelineOptions(pipeline_args)
  options.view_as(SetupOptions).save_main_session = True

  with beam.Pipeline(options=options) as pipeline:

     tornadoes = (pipeline 
        | 'Read csv from gsc' >> beam.io.ReadFromText(known_args.input, skip_header_lines=1)
        | 'csv' >> beam.Map(lambda line: next(csv.reader([line])))
        | 'filter out 2 columns' >> beam.Map(lambda fields: (fields[3], fields[30]))
        | 'Write result to GCS' >> beam.io.textio.WriteToText(known_args.output)
        )

  pipeline.run() 


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)	
  run()