# Бот, который помогает следить за здоровьем
WATER_PER_KG = 30
WATER_PER_L = 1000
LINE_LENGTH = 95

print('Привет! Я твой личный помощник по здоровью.')
print('Моя задача - помогать тебе поддерживать свое здоровье '
      'и чувствовать себя прекрасно каждый день.')
print('-' * LINE_LENGTH)

# Шаг 1: Спрашиваем имя
print('Для начала давай познакомимся!')
user_name = input('Как тебя зовут? ')
clean_name = user_name.strip()

# Шаг 2: Спрашиваем возраст
while True:
    try:
        user_age = int(input('Сколько тебе лет? '))
        if user_age > 0:
            break
        else:
            print('Ошибка: возраст должен быть положительным числом!'
                  'Попробуйте ещё раз.')
    except ValueError:
        print('Ошибка: пожалуйста, введите корректное число.')
# Определяем окончание в зависимости от возраста
if 11 <= user_age <= 14:
    ending = 'лет'
else:
    last_digit = user_age % 10
    if last_digit == 1:
        ending = 'год'
    elif 2 <= last_digit <= 4:
        ending = 'года'
    else:
        ending = 'лет'

# Шаг 3: Узнаём индекс массы
print('Чтобы я мог давать тебе точные и полезные рекомендации, '
      'мне нужно больше узнать о тебе.')


def request_user_weight():  # Запрашиваем вес
    """Запрашиваем вес"""
    while True:
        try:
            user_input = input('Введите вес (кг): ').replace(',', '.')
            user_weight = float(user_input)
            if user_weight <= 0:
                print('Ошибка: вес должен быть положительным числом!'
                      'Попробуйте ещё раз.')
            else:
                return user_weight
        except ValueError:
            print('Ошибка: пожалуйста, введите корректное число'
                  '(например, 75.5 или 80).')


def request_user_height():  # Запрашиваем рост
    """Запрашиваем рост"""
    while True:
        try:
            user_input = input('Какой у тебя рост? Укажи в метрах'
                               '(например 1.75): ').replace(',', '.')
            user_height = float(user_input)
            if user_height <= 0:
                print('Ошибка: рост должен быть положительным числом!'
                      'Попробуйте ещё раз.')
            else:
                return user_height
        except ValueError:
            print('Ошибка: пожалуйста, введите корректное число')


user_weight = request_user_weight()
user_height = request_user_height()


def calculate_bmi(user_weight, user_height):  # Расчет ИМТ
    """Рассчитывает индекс массы тела (ИМТ) по весу и росту.

    Args:
        user_weight (float): вес в килограммах.
        user_height (float): рост в метрах.

    Returns:
        float: значение ИМТ.
    """
    return round(user_weight / (user_height ** 2), 1)


# По найденному ИМТ, получаем категорию и совет от ВОЗ
def get_bmi_category(bmi):
    """По найденному ИМТ, получаем категорию и совет от ВОЗ"""
    if bmi < 16:
        return (
            'Выраженный дефицит массы тела (истощение)',
            'Обязательная консультация с врачом'
        )
    elif 16 <= bmi <= 18.4:
        return 'Дефицит массы тела', 'Проведение обследования'
    elif 18.5 <= bmi <= 24.9:
        return 'Ваш вес в пределах нормы!', 'Продолжайте в том же духе!'
    elif 25 <= bmi <= 29.9:
        return 'Предожирение', 'Пересмотреть режим питания и рацион'
    elif 30 <= bmi <= 34.9:
        return (
            'Ожирение 1 степени',
            'Проведение обследования для составления плана снижения веса'
        )
    elif 35 <= bmi <= 39.9:
        return (
            'Ожирение 2 степени',
            'Проведение обследования для составления плана снижения веса'
        )
    else:
        return (
            'Ожирение 3 степени',
            'Проведение обследования для составления плана снижения веса'
        )


# Шаг 4: Узнаём норму воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / WATER_PER_L  # Перевод в литры

# Шаг 5: Выводим итоговый расчет
print('-' * LINE_LENGTH)
print(f'Отчет для пользователя: {clean_name} ({user_age} {ending})')

bmi = calculate_bmi(user_weight, user_height)
category, recommendation = get_bmi_category(bmi)

print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Категория: {category}')
print(f'Рекомендация: {recommendation}')

print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('Расчет сформирован. Будьте здоровы!')
