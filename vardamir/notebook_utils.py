import yaml

def get_notebook_config(file_path: str) -> None:
    config = None

    with open(file_path) as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)

    return config
