from locators.home_page_locators import HomePageLocators


class DataForTests:
    ORDER_DATA = [
        {
            'name': 'Иван',
            'surname': 'Иванов',
            'address': 'Улица Иванова',
            'station': 'Бульвар Рокоссовского',
            'phone': '89000000000',
            'date': '15.07.2025',
            'period': 'Трое суток'
        },
        {
            'name': 'Петр',
            'surname': 'Петров',
            'address': 'Проспект Петрова',
            'station': 'Комсомольская',
            'phone': '89111111111',
            'date': '01.08.2025',
            'period': 'Сутки'
        }
    ]
    FAQ_BLOCK_DATA = [
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_ONE,
            'expected_answer': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_ONE
        },
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_TWO,
            'expected_answer': 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_TWO
        },
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_THREE,
            'expected_answer': 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_THREE
        },
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_FOUR,
            'expected_answer': 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_FOUR
        },
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_FIVE,
            'expected_answer': 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_FIVE
        },
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_SIX,
            'expected_answer': 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_SIX
        },
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_SEVEN,
            'expected_answer': 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_SEVEN
        },
        {
            'question_locator': HomePageLocators.FAQ_QUESTION_EIGHT,
            'expected_answer': 'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
            'answer_locator': HomePageLocators.FAQ_ANSWER_EIGHT
        }
    ]
