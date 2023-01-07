import itertools
import time

cycle = itertools.cycle(['-', '/', '|', '\\'])
for i in range(5):
    print("Loading", next(cycle), end="\r")
    time.sleep(.5)
print("Finished!")

cycle = itertools.cycle(['.', '..', '...', '....'])
for i in range(5):
    print("Waiting", next(cycle), f"{'':<5}", end="\r")
    time.sleep(.5)
print("Finished!")
