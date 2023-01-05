from datetime import datetime
import time
import tibbercall

def wait_and_sleep(sleep_time):
    end_time = 0
    sleep_interval = 1
    while end_time < sleep_time:
        time.sleep(sleep_interval)
        end_time += sleep_interval


def seconds_to_midnight():
    n = datetime.now()
    return ((24-n.hour-1) * 60 * 60) + ((60-n.minute -1) * 60) + (60 -n.second)


if __name__ == '__main__':
    # execute time should be at 13:30
    # assuming time is 00:00 when execution
    # 60 * 60 = 1hour,
    # 60 * 60 * 13 = 13 hours
    # (60 * 60 * 13) + (30 * 60) = 13.5hours
    seconds_to_execute = (60 * 60 * 13) + (30 * 60)

    while True:
        data = tibbercall.get_data('today')
        tibbercall.insert_data(data)
        data = tibbercall.get_data('tomorrow')
        time_to_sleep = seconds_to_midnight() + seconds_to_execute
        if data:
            tibbercall.insert_data(data)
        else:
            wait_and_sleep(3600)
