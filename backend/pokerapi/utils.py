import random, string
from .models import Game


def generate_name():
    global name
    is_unique = False
    while not is_unique:
        name = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(7)
        )
        try:
            Game.objects.get(name=name)
        except Game.DoesNotExist:
            is_unique = True
    return name
