import pytest
from tests.data import DataForTests
import allure


class TestFaqBlock:
    @allure.title('Проверка появления текста с ответом на вопрос при нажатии на все 8 вопросов')
    @pytest.mark.parametrize('faq_block_data', DataForTests.FAQ_BLOCK_DATA)
    def test_click_on_questions_shows_answers(self,homepage,faq_block_data):
        homepage.click_faq_question(faq_block_data['question_locator'])

        assert faq_block_data['expected_answer'] == homepage.text_answer_for_question(faq_block_data['answer_locator'])
