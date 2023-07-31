def recent_transactions(input_operations_list, number_operation):
    """
    Возвращает последние операции в указанном количестве с сортировкой.
    Сверху списка находятся самые последние операции (по дате).

    :param input_operations_list: Список с экземплярами класса "Операции"
    :param number_operation: количество возвращаемых экземпляров
    :return: возвращает список с отсортированным экземплярами класса "Операции" по дате операции, по убыванию.
    """
    return sorted(input_operations_list, key=lambda x: x.date_operation)[0:number_operation]


def withdraw_operations(input_operations_list, number_operation):
    """
    Выводит информацию об операции в заданном формате

    :param input_operations_list: Список с экземплярами класса "Операции"
    :param number_operation: количество возвращаемых экземпляров
    :return:
    """
    operations_list = recent_transactions(input_operations_list, number_operation)
    for operation in operations_list:
        if operation.is_executed:
            print(operation.date_operation_text + " " + operation.description)
            print(operation.from_account_secret + " -> " + operation.to_account_secret)
            print(operation.operation_amount["amount"] + " " + operation.operation_amount["currency"]["name"] + "\n")

