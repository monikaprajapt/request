import json

def encode_complex(object):
    if isinstance(object, complex):
        return [object.real, object.imag]

complex_obj = json.dumps(2 + 3j,default=encode_complex)
print(complex_obj) 
