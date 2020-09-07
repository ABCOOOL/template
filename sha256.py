import hashlib


def sha256(target):
    after_sha256 = hashlib.sha256(target.encode()).hexdigest()
    return after_sha256