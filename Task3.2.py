def data_user(name, last_name, year_of_birth, city_of_residence, email, phone):
    print(f"Пользователь {name} {last_name} {year_of_birth} года рождения, проживающий в городе {city_of_residence}, "
          f"имеет Email {email} и телефон {phone}")


user_template = {
    'name': 'Имя',
    'last_name': 'Фамилия',
    'year_of_birth': 'Год рождения',
    'city_of_residence': 'Город проживания',
    'email': 'Email',
    'phone': 'Телефон'
}
my_user = {}
for key, value in user_template.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})


def print_user(**my_user):
    pass
