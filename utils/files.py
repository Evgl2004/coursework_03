import json
from classes.operations import Operation


def load_json_file(path_to_file):
    """
    Считываем файл формата json с операциями, возвращаем значения в виде словаря

    :param path_to_file: путь до файла, который считываем
    :return: данные из JSON представленных в виде списка словарей
    """
    with open(path_to_file, "rt", encoding="utf-8") as file_operation:
        return json.loads(file_operation.read())


def load_operations(path_to_file):
    """
    Считываем файл формата json с операциями, возвращаем список экземпляров класса Операции

    :param path_to_file: путь до файла, который считываем
    :return: список экземпляров класса Операции
    """
    return_list = []
    for input_dict in load_json_file(path_to_file):
        return_list.append(
            Operation(input_dict["id"], input_dict["date"], input_dict["state"], input_dict["operationAmount"],
                      input_dict["description"], input_dict["from"], input_dict["to"]))

    return return_list
