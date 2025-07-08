class OrderPageLocators:
    # Шаг 1
    NAME_INPUT_FIELD = ["xpath", ".//input[@placeholder='* Имя']"] # Поле ввода Имени
    SURNAME_INPUT_FIELD = ["xpath", ".//input[@placeholder='* Фамилия']"] # Поле ввода Фамилии
    ADRESS_INPUT_FIELD = ["xpath", ".//input[@placeholder='* Адрес: куда привезти заказ']"] # Поле ввода Адреса
    METRO_STATION_SELECT_FIELD = ["xpath", ".//div[@class='select-search']"] # Поле выбора Станции метро
    METRO_STATION_ROKOSSOVSKY_BOULEVARD = ["xpath", ".//li[@data-index='0']"] # Кнопка выбора станции метро Бульвар Рокоссовского
    METRO_STATION_KOMSOMOLSKAYA = ["xpath", ".//li[@data-index='5']"] # Кнопка выбора станции метро Комсомольская
    PHONE_NUMBER_INPUT_FIELD = ["xpath", ".//input[@placeholder='* Телефон: на него позвонит курьер']"] # Поле ввода Номера телефона
    NEXT_BUTTON = ["xpath", ".//button[text()='Далее']"] # Кнопка Далее
    # Шаг 2
    DELIVERY_DATE_INPUT_FIELD = ["xpath", ".//input[@placeholder='* Когда привезти самокат']"] # Поле ввода Даты доставки
    RENTAL_PERIOD_SELECT_FIELD = ["xpath", ".//div[@class='Dropdown-root']"] # Поле выбора Срока аренды
    RENTAL_PERIOD_ONE_DAY_BUTTON = ["xpath", ".//div[text()='сутки']"] # Кнопка выбора срока аренды Сутки
    RENTAL_PERIOD_THREE_DAYS_BUTTON = ["xpath", ".//div[text()='трое суток']"] # Кнопка выбора срока аренды Трое суток
    ORDER_BUTTON = ["xpath", ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"] # Кнопка Заказать
    # Шаг 3
    CONFIRM_BUTTON = ["xpath", ".//button[text()='Да']"] # Кнопка Да
    # Шаг 4
    SHOW_STATUS_ORDER_BUTTON = ["xpath", ".//button[text()='Посмотреть статус']"] # Кнопка Посмотреть статус
    HEADER_DISCLAIMER = ["xpath", ".//div[@class='Header_Disclaimer__3VEni']"] # Дисклеймер Учебный тренажер в шапке
