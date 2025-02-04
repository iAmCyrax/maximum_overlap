from datetime import datetime, timedelta


def create_date_range(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    return dates


def split_dates(dates, group_size, start_size=None, end_size=None):
    groups = []

    if start_size:
        groups.append(dates[:start_size])
        dates = dates[start_size:]

    for i in range(0, len(dates) - (end_size or group_size), group_size):
        groups.append(dates[i:i + group_size])

    if end_size:
        groups.append(dates[-end_size:])
    else:
        groups.append(dates[-group_size:])

    return groups


def find_max_overlap(dates1, dates2, group_size, start_size=None, end_size=None):
    grouped_dates1 = split_dates(dates1, group_size, start_size, end_size)
    grouped_dates2 = split_dates(dates2, group_size, start_size, end_size)

    # n = 0
    dates_list = []
    for group in grouped_dates1:
        if group in grouped_dates2:
            dates_list.append(group)
            # n += 1

    # return n
    return dates_list


def find_optimal_grouping(dates1, dates2):
    max_overlap = []
    optimal_size = 0
    optimal_start_size = 0

    for size in [2, 3, 4]:
        for start_size in [None, 2, 3, 4]:
            overlap = find_max_overlap(dates1, dates2, size, start_size)
            # print(overlap)
            if len(overlap) > len(max_overlap):
                max_overlap = overlap
                optimal_size = size
                optimal_start_size = start_size

    return optimal_size, max_overlap, optimal_start_size


date_group1 = create_date_range(datetime(2024, 7, 1), datetime(2024, 10, 31))
date_group2 = create_date_range(datetime(2024, 7, 15), datetime(2024, 7, 30))

best_size, best_overlap, best_start_size = find_optimal_grouping(date_group1, date_group2)

print(best_size)
print(best_start_size)
print(best_overlap)
