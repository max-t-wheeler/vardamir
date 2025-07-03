def get_bigquery_table_name(config: dict) -> str:
  project_id = config.get('project_id')
  dataset_id = config.get('dataset_id')
  table_id = config.get('table_id')

  table_name = f"{project_id}.{dataset_id}.{table_id}"

  return table_name
