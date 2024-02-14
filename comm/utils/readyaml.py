import yaml


def read_yaml_data(yaml_file):

    with open(yaml_file, 'r', encoding="utf-8") as fr:
        return yaml.load(fr, Loader=yaml.SafeLoader)


def write_yaml_file(yaml_file, obj):

    with open(yaml_file, 'w', encoding='utf-8') as fw:
        yaml.dump(obj, fw, Dumper=yaml.RoundTripDumper, allow_unicode=True)

