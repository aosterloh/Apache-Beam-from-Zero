PROJECT=data-academy-2018
BUCKET=alex-testdata
python -m tornadoes03 --input gs://$BUCKET/weather/gsod_medium.csv \
  --output gs://$BUCKET/output/ \
  --runner DataflowRunner \
  --project $PROJECT \
  --region europe-west1 \
  --temp_location gs://$BUCKET/output 
