import json


def read_json_data(json_file):
    with open(json_file, "r", encoding="utf-8") as fr:
        return json.load(fr, strict=False)


def write_json_file(json_file, obj):
    with open(json_file, "w", encoding='utf-8') as fw:
        json.dump(obj, fw, ensure_ascii=False, indent=4)
