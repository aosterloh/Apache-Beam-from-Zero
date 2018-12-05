python -m tornadoes10 --input data-academy-2018:gsod.weather \
  --output data-academy-2018:gsod.output \
  --output_tablename exercise0 \
  --runner DataflowRunner \
  --project data-academy-2018 \
  --temp_location gs://alex-staging/staging \
