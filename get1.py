def get_answer(question):
 answers={"привет":"И тебе привет!", "как дела":"Лучше всех","пока":"Увидимся"}
 return answers.get(question)
user_question = input('Спроси что-нибудь:\n')
answer = get_answer(user_question.lower())
print(answer)