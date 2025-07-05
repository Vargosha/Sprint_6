class TestFaqBlock:
    def test_click_on_question_one_shows_answer(self,homepage):
        # Проверка что при нажатии на Первый вопрос открывается ответ на Первый вопрос
        expected_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

        homepage.click_faq_question_one()

        assert expected_answer == homepage.text_answer_for_question_one()

    def test_click_on_question_two_shows_answer(self,homepage):
        # Проверка что при нажатии на Второй вопрос открывается ответ на Второй вопрос
        expected_answer = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

        homepage.click_faq_question_two()

        assert expected_answer == homepage.text_answer_for_question_two()

    def test_click_on_question_three_shows_answer(self,homepage):
        # Проверка что при нажатии на Третий вопрос открывается ответ на Третий вопрос
        expected_answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

        homepage.click_faq_question_three()

        assert expected_answer == homepage.text_answer_for_question_three()

    def test_click_on_question_four_shows_answer(self,homepage):
        # Проверка что при нажатии на Четвертый вопрос открывается ответ на Четвертый вопрос
        expected_answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

        homepage.click_faq_question_four()

        assert expected_answer == homepage.text_answer_for_question_four()

    def test_click_on_question_five_shows_answer(self,homepage):
        # Проверка что при нажатии на Пятый вопрос открывается ответ на Пятый вопрос
        expected_answer = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

        homepage.click_faq_question_five()

        assert expected_answer == homepage.text_answer_for_question_five()

    def test_click_on_question_six_shows_answer(self,homepage):
        # Проверка что при нажатии на Шестой вопрос открывается ответ на Шестой вопрос
        expected_answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

        homepage.click_faq_question_six()

        assert expected_answer == homepage.text_answer_for_question_six()

    def test_click_on_question_seven_shows_answer(self,homepage):
        # Проверка что при нажатии на Седьмой вопрос открывается ответ на Седьмой вопрос
        expected_answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

        homepage.click_faq_question_seven()

        assert expected_answer == homepage.text_answer_for_question_seven()

    def test_click_on_question_eight_shows_answer(self,homepage):
        # Проверка что при нажатии на Восьмой вопрос открывается ответ на Восьмой вопрос
        expected_answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

        homepage.click_faq_question_eight()

        assert expected_answer == homepage.text_answer_for_question_eight()
