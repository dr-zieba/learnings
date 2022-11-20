template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
        },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
            },
        'birthplace': {
            'country': str,
            'city': str
            }
        }
}

john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
        },
    'bio': {
        'dob': {
        'year': 1939,
        'month': 11,
        'day': 27
        },
    'birthplace': {
        'country': 'United Kingdom',
        'city': 'Weston-super-Mare'
        }
    }
}

eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
        },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
            },
        'birthplace': {
             'country': 'United Kingdom'
            }
        }
    }

class SchemaError(Exception):
    pass

class SchemaKeyMismatch(SchemaError):
    pass

class SchemaTypeMismatch(SchemaError, TypeError):
    pass

def check_keys(data, template, path):
    data_keys = data.keys()
    template_keys = template.keys()

    extra_keys = data_keys - template_keys
    missing_keys = template_keys - data_keys

    if missing_keys or extra_keys:
        is_ok = False
        missing_msg = ('Missing keys: ' + ','.join({path + '.' + str(key) for key in missing_keys})) if missing_keys else ''
        extra_msg = ('Extra keys: ' + ','.join({path + '.' + str(key) for key in extra_keys})) if extra_keys else ''
        raise SchemaKeyMismatch(' '.join((missing_msg, extra_msg)))

def check_type(data, template, path):
    for k, v in template.items():
        if isinstance(v, dict):
            template_type = dict
        else:
            template_type = v
        data_value = data.get(k, object())
        if not isinstance(data_value, template_type):
            error_msg = (f'Incorect type: {path}.{k} -> expected: {template_type.__name__}, found: {type(data_value).__name__}')
            raise SchemaTypeMismatch(error_msg)

def recurse_validation(data, template, path):
    check_keys(data, template, path)
    check_type(data, template, path)

    dict_keys = {key for key, value in template.items() if isinstance(value, dict)}

    for key in dict_keys:
        sub_path = f'{path}.{str(key)}'
        sub_template = template[key]
        sub_data = data[key]
        recurse_validation(sub_data, sub_template, sub_path)

def validate(data, template):
    recurse_validation(data, template, '')


validate(eric, template)