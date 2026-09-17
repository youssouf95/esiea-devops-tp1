from validate_timeout import validate_timeout

assert validate_timeout(30) is True
assert validate_timeout(60) is True
assert validate_timeout(0) is False
assert validate_timeout(-5) is False

print("OK")
