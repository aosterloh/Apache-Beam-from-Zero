PROJECT=<PROJECTID>
BUCKET=<BUCKETNAME, e.g. tornado-eu>

python -m tornadoes03 --input gs://$BUCKET/weather/gsod_medium.csv \
  --output gs://$BUCKET/output/ \
  --runner DataflowRunner \
  --project $PROJECT \
  --region europe-west1 \
  --temp_location gs://$BUCKET/temp_location \
  --setup_file ./setup.py
