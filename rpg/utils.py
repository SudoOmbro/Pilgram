def load_json_into_object(input_json: dict, target: object):
    for element in input_json:
        target.__dict__[element] = input_json[element]
