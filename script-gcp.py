from google.auth import compute_engine
from google.cloud import bigquery

credentials = compute_engine.Credentials(
    service_account_email='SERVICE_ACCOUNT_EMAIL')
query = '''
SELECT
  name,
  count
FROM
  `babynames.names_2014`
WHERE
  gender = 'M'
ORDER BY
  count DESC
LIMIT
  5
'''
client = bigquery.Client(
    project='PROJECT_ID',
    credentials=credentials)
print(client.query(query).to_dataframe())
