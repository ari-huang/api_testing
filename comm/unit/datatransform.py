import json

import config.variables as var

call_counter = 0


def replace_string(value: str, template_vars: {}) -> object:
    """
    Replaces template strings in value, by the values in template_vars.
    """

    for template, newValue in template_vars.items():
        value = value.replace("${}".format(template), str(newValue))

    return value


def replace_recursive(json_obj: object, template_vars: {}) -> {}:
    """
    Recursively unpacks and replaces items in a multi-dimensional dict/list/item json object.
    """
    # For each item at this level

    for key, value in json_obj.items():
        # If the value is a string, replace it

        if isinstance(value, (str, int, bool)):
            if isinstance(value, str):
                json_obj[key] = replace_string(value, template_vars)

        # If the item is a list, we need to do something for each value
        elif isinstance(value, list):
            # Enumate unpacks an index with each value
            for index, item in enumerate(value):
                # If it's a string, we can replace it

                if isinstance(item, str):
                    value[index] = replace_string(item, template_vars)
                # If it's not, we need to do more work.
                else:
                    value[index] = replace_recursive(item, template_vars)

        # If it's a dict, use this function again to unpack/replace the values
        else:
            json_obj[key] = replace_recursive(value, template_vars)

    return json_obj


def config_to_dict():
    var_dict = dict()
    for k, v in vars(var).items():
        if not k.startswith("_"):
            var_dict[k] = v
    return var_dict


def init_variable(casedata):
    var_dict = config_to_dict()
    json = replace_recursive(casedata, var_dict)
    return json
