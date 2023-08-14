import json


def print_json(json_object: object, indent: int = 1) -> None:
    print(json.dumps(json_object, indent=indent))
