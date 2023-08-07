#Can only be run from Google Shell Editor or using the Google Cloud CODE plugin in VS Code
#https://cloud.google.com/code?hl=zh-cn
from google.cloud import bigquery
from google.cloud import storage
import os

client = bigquery.Client(project = 'strategic-howl-392707')
bucket_name = 'rios_patent'
project = 'patents-public-data'
dataset_id = 'patents'
table_id = 'publications_202304'

destination_uri = 'gs://{}/{}'.format(bucket_name, 'GooglePatent/Google_patent*.gz')
dataset_ref = client.dataset(dataset_id, project=project)
table_ref = dataset_ref.table(table_id)
configuration = bigquery.job.ExtractJobConfig()
#For AVRO 
#configuration.destination_format ='AVRO'
#For JSON
#configuration.destination_format ='NEWLINE_DELIMITED_JSON'
configuration.compression = 'GZIP'

extract_job = client.extract_table(
    table_ref,
    destination_uri,
    job_config=configuration,
    location='US')
extract_job.result()

# Download the file from GCS
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob('GooglePatent/Google_patent*.gz')
blob.download_to_filename('/path/to/rios_patent/GooglePatent/Google_patent*.gz')

print('Exported {}:{}.{}, and downloaded to {}'.format(project, dataset_id, table_id, '/path/to/rios_patent/GooglePatent/Google_patent*.gz'))


