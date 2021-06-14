import hashlib

def generate_sha256(message):
    result = hashlib.sha256()
    result.update(str(message).encode('utf-8'))
    return result.hexdigest()

def func_args_processor(func):
    
    def input_args(*args, **kwargs):
        for v in kwargs:
            kwargs[v] = args_precessing(kwargs[v])
        # args = [args_precessing(e) for e in args]
        return func(*args, **kwargs)
    
    return input_args

def args_precessing(value):
    if type(value) == "dict":
        return str(value.values()[0])
    if type(value) == "list":
        return [str(x) for x in value]
    return str(value)