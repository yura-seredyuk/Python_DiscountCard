"""1. Написати клас "Карточка на знижку" (git add), який містить наступну інформацію: 

Номер карточки 
Розмір знижки (знижка передбачається накопичуваною; на початковому етапі вона рівна 1%. За кожні 1000 грн. покупки, сума знижки збільшується на 1%.) 
Приховане допоміжне поле для збереження вартості накупленого товару 
Дата видачі карточки в форматі "12/02/1200") 
Забезпечити можливість: 
Купляти товар з використанням карточки на знижку; 
Виводити інформацію про поточну величину знижки; 
Виводити інформацію про те, на яку суму ще необхідно докупити товару, щоб величина знижки збільшилась."""


if __name__ == "__main__":
    DiscountCard

import random
import datetime


class DiscountCard:
    """__discount -- max value is 50%, min value is 1% be default
       __sum -- the sum of accumulation is calculated as the amount of funds actually paid for goods
    """

    def __init__(self):
        self.__number = random.randint(10000000, 99999999)
        self.__sum = 0
        self.__discount = 1
        self.__date = datetime.datetime.now().strftime("%d/%m/%Y")

    def buy_article(self, cost: float):
        """Buy goods using a discount card"""
        if cost > 0:
            pay = cost - (cost * self.__discount / 100)
            print(
                f'Your discount is UAH {cost * self.__discount / 100}. You need to pay {pay} UAH.')
            confirm = input("Do you want to continue?: y/n --> ")
            if confirm.lower() == 'y':
                self.__sum += pay
                self.__discount = round(
                    self.__sum // 1000 + 1) if round(self.__sum // 1000 + 1) <= 50 else 50
                print("Congratulations! Operation is correct.\n")
            elif confirm.lower() == 'n':
                print("Bye!\n")
            else:
                print("Error! Wrong command. Try again!\n")
        else:
            print("Uncorrect cost! Please try again.\n")

    def discount_info(self):
        """Display information about the current amount of the discount"""
        print(
            f'Card number:{self.__number}. Your discount is {self.__discount}%.\n')

    def discount_inc_info(self):
        """Display information on how much you still need to buy additional goods to increase the size of the discount"""
        next_lev = self.__discount * 1000 - self.__sum
        if next_lev == 0:
            next_lev = 1000
        print(
            f'Card number:{self.__number}. For the next level you need to buy more goods for {next_lev} UAH.\n')

    @property
    def number(self):
        return self.__number

    @property
    def sum(self):
        return self.__sum

    @property
    def discount(self):
        return self.__discount

    @property
    def date(self):
        return self.__date
