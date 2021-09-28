def correct_answers_number(profile_data_query):
    answers_number = len(profile_data_query)
    correct_answers_len = len(list(filter(lambda x: x.is_correct_answer, profile_data_query)))
    return answers_number, correct_answers_len
