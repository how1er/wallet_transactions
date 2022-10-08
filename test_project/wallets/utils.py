import random
import string


def get_random_string():
    # choose from all lowercase letter
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(8))
