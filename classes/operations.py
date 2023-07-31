

class Operation:
    def __init__(self, id_operation=0, date_operation="", state="", operation_amount="", description="",
                 from_account="Счет 00000000000000000000",
                 to_account="Счет 00000000000000000000"):

        self.id_operation = id_operation
        self.date_operation = date_operation
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_account = from_account
        self.to_account = to_account
        self.from_account_secret = self.convert_secret_from_account()
        self.to_account_secret = self.convert_secret_to_account()
        self.date_operation_text = self.convert_date_operation()
        self.is_executed = self.check_is_executed()

    def __str__(self):
        return f'Operation = "{self.id_operation}" | date_operation="{self.date_operation}"'

    def __repr__(self):
        return f'Operation (id_operation="{self.id_operation}", date_operation="{self.date_operation}",' \
               f' state="{self.state}), operation_amount="{self.operation_amount}", description="{self.description}", ' \
               f' from_account="{self.from_account}", from_account="{self.from_account}"' \
               f' from_account_secret="{self.from_account_secret}", to_account_secret="{self.to_account_secret}"'

    def convert_secret_from_account(self):
        """
        - Номер карты замаскирован и не отображается целиком в формате: XXXX XX** **** XXXX
        (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
        :return: Возвращает скрытый номер карты
        """
        return self.from_account[:self.from_account.find(' ')] + " " + self.from_account[-16:-12] + " " \
                                   + self.from_account[-11:-10] + "** **** " + self.from_account[-4:]

    def convert_secret_to_account(self):
        """
        - Номер счета замаскирован и не отображается целиком в формате: **XXXX (видны только последние 4 цифры номера счета).
        :return: Возвращает скрытый номер счета
        """
        return self.from_account[:self.from_account.find(' ')] + " **" + self.to_account[-4:]

    def convert_date_operation(self):
        """
        Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
        :return: Возвращает дату в заданном формате.
        """
        return self.date_operation[8:10] + "." + self.date_operation[5:7] + "." + self.date_operation[0:4]

    def check_is_executed(self):
        """
        Проверяет успешная ли операция.
        :return: Возвращает Истину, если операция Успешная.
        """
        if self.state == "EXECUTED":
            return True
        else:
            return False

