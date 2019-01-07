import hashlib


def get_md5_digest(source_data):
    return hashlib.md5(source_data).digest()
