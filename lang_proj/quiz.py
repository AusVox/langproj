from . import terms_work
from lang_proj.views_functions import get_terms_by_id
from random import choices


class Quiz:
    def __init__(self):
        random_terms = choices(get_terms_by_id(1), k=5)  #TODO: вынести количество вопросов в .env

        self.qna = []
        cnt = 0
        for rt in random_terms:
            qna_item = []
            cnt += 1
            qna_item.append(cnt)
            qna_item = qna_item + rt[1:]
            self.qna.append(qna_item)

            self.user_answers = []
            self.qna_iter = iter(self.qna)  # Объект-итератор для вопросов-ответов

    def next_qna(self):
        """Возвращает очередной вопрос"""
        return next(self.qna_iter)

    def record_user_answer(self, a):
        """Добавляет ответ пользователя в переменную экземпляра (список ответов)"""
        self.user_answers.append(a)

    def get_user_answers(self):
        """Возвращает список ответов пользователя"""
        return self.user_answers

    def check_quiz(self):
        """Проверяет ответы и возвращает список эмодзи"""
        correct_answers = [str(qna_item[2]).split('/') for qna_item in self.qna]
        answers_true_false = [i in j for i, j in zip(self.user_answers, correct_answers)]
        answers_emoji = [str(atf).replace('False', '❌').replace('True', '✅') for atf in answers_true_false]
        return answers_emoji
