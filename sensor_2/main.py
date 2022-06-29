import time
import random

while True:
  temp = round(random.uniform(10, 20), 1)
  bacteria = round(random.uniform(400, 3000), 1)
  print({"sensor_id": 2, "temperature": temp, "bacteria": bacteria})
  time.sleep(1)