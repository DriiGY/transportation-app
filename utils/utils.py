from datetime import datetime


def calc_time_diff(st_time, ed_time):  # format of times: ex. 11:46
    st_time += ":00"
    ed_time += ":00"
    start_time = datetime.strptime(st_time, "%H:%M:%S")
    end_time = datetime.strptime(ed_time, "%H:%M:%S")
    # get difference
    delta = end_time - start_time

    sec = delta.total_seconds()
    # print('difference in seconds:', sec)

    min = sec / 60
    # print('difference in minutes:', min)

    # get difference in hours
    hours = sec / (60 * 60)
    # print('difference in hours:', hours)

    return int(hours), int(int(min) - int(hours) * 60)


# test
#print(calc_time_diff("15:00", "15:31"))