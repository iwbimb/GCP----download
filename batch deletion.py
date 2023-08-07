#batch deletion
from google.cloud import storage

# Replace <your_project_id> with your project ID
client = storage.Client(project='<strategic-howl-392707>')
#bucket name
bucket = client.bucket('rios_patent')

# List all the blobs in the bucket
for i in range(0, 11016):
    blob_name = 'Google_patent{:012d}'.format(i)
    blob = bucket.blob(blob_name)
    blob.delete()
    print('Blob {} deleted.'.format(blob_name))