from string import punctuation
from django import template

register = template.Library()

trigger_words_list = ['lorem', 'ipsum']


def gen_trigger_words_list(words_list: list) -> list:
    result_list = []
    for i in words_list:
        for ch in punctuation:
            result_list.append(f'{i}{ch}')
            result_list.append(f'{ch}{i}')
        result_list.append(i)
    return result_list


@register.filter()
def censor(text: str) -> str:
    bad_words = gen_trigger_words_list(trigger_words_list)
    input_text_as_list = text.split()
    censored_text = []
    censored_word = None

    for i in input_text_as_list:
        if i.lower() in bad_words:
            for ch in i:
                if ch in punctuation:
                    censored_word = i[0] + '*' * (len(i) - 2) + ch
                else:
                    censored_word = i[0] + '*' * (len(i) - 1)
            censored_text.append(censored_word)
        else:
            censored_text.append(i)
    return ' '.join(censored_text)
