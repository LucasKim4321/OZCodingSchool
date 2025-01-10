print("start animals")

# __all__ = ['mammals','birds']

from .mammals import mammals
from .birds import birds
# import mammals
# import birds

animals = {
    "mammals": mammals,
    "birds": birds
}

print(animals)
