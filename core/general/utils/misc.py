import yaml


def yaml_coerce(value):
    # Convert to Python

    if isinstance(value, str):
        return yaml.load(f'data: {value}', Loader=yaml.SafeLoader)['data']

    return value
