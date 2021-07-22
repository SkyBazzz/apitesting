from voluptuous import Schema, Coerce, Url, Required

get_user_scheme = Schema({
    Required('id'): Coerce(int),
    'email': str,
    'first_name': str,
    'last_name': str,
    'avatar': Url()
})
