PROJECT=<PROJECTID>
BUCKET=<BUCKET>

python -m tornadoes10 --input $PROJECT:gsod.weather \
  --output $PROJECT:gsod.output \
  --output_tablename tornadocount \
  --runner DataflowRunner \
  --project $PROJECT \
  --temp_location gs://$BUCKET/staging \
