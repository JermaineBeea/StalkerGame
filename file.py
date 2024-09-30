import time

kill_time = 10

def time_event(period):
  start_time = time.perf_counter()
  while True:
    end_time = time.perf_counter()
    time_passed = end_time - start_time
    if time_passed > period: return True

