from omnicam import OmnicamAPI
from datetime import datetime
import random
import time


api = OmnicamAPI("", "http://localhost:8000")

while True:
    # Get current time
    now = str(datetime.now())
    # print api.add_activity(1, now, now, random.randint(1, 101), random.randint(1, 101))

    print api.add_utility_track(1, random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(1, 101),
                                random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), now)

    time.sleep(random.randint(2, 6))
