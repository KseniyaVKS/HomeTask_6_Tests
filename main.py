import requests

def unique_names(list_names):
    all_names_list = []
    for mentor in list_names:
        name = mentor.split()
        all_names_list.append(name[0])

    unique_names = set(all_names_list)

    all_names_sorted = sorted(list(unique_names))
    res = ', '.join(all_names_sorted)

    return f'Уникальные имена преподавателей: {res}'


def top_3(list_names):
    unique_names = [x.split(" ")[0].strip() for x in list_names]

    popular = []

    for name in unique_names:
        popular.append((name, unique_names.count(name)))

    popular = list(set(popular))
    popular.sort(key=lambda x: x[1], reverse=True)
    popular_list = list(popular)
    top_3 = popular_list[0:3]

    top_str = []

    for name, count in top_3:
        top_str.append(name + ': ' + str(count))

    return f'{" раз(а), ".join(top_str)} раз(а)'


def courses_duration(courses_list):
    durations_dict = {}

    for id, course in enumerate(courses_list):
        key = course["duration"]
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)

    durations_dict = dict(sorted(durations_dict.items()))

    courses_duration_list = []
    for durations, valuem in durations_dict.items():
        for i in valuem:
            string = f'{courses_list[i]["title"]} - {durations} месяцев'
        courses_duration_list.append(string)

    return courses_duration_list


def YandexDisk_folder(token):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    params = {
        "path": 'for_coursework'
    }

    headers = {
        "Authorization": token
    }

    res = requests.put(url, headers=headers, params=params)
    if res.status_code == 409:
        requests.delete(url, headers=headers, params=params)
        res = requests.put(url, headers=headers, params=params)

    return res.status_code

