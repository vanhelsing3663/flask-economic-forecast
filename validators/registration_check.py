import re
from abc import ABC, abstractmethod


class CheckRegister(ABC):
    @abstractmethod
    def is_valid_lenght(self, lenght_password):
        pass


class CheckUserPassword(CheckRegister):

    def is_valid_lenght(self, lenght_password):
        "Функция проверяет , что длина пароля валидная"
        return True if len(lenght_password) >= 8 else False

    def checking_that_the_password_contains_at_least_one_digit(self, password):
        "Функция проверяет , что пароль содержит хотя бы одну цифру"
        return any(psw.isdigit() for psw in password)

    def has_uppercase(self, password):
        """Проверяет, содержит ли пароль хотя бы одну заглавную букву"""
        pattern = r'[A-Z]'
        return bool(re.search(pattern, password))



class CheckUserEmail(CheckRegister):
    def is_valid_lenght(self, lenght_email):
        "Функция проверяет , что длина пароля валидная"
        return True if len(lenght_email) >= 5 else False

    def count_dog_symbol(self, email):
        "Функция проверяет , что  email содержит символ @"
        return True if email.count("@") == 1 else False

    def email_should_not_exceed_voltage(self, email):
        "Функция проверяет , что длина email не более 256"
        return True if len(email) <= 256 else False


