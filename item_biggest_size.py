#biggest size in dictionary
def bsidict(dict):
    # for i in range():
    # for key, value in dict.items():
    #     print(f'a chave "{key}" , seu tamanho é {value}')
    biggest_value = 0
    
    for value in dict.values():
        if len(value) > biggest_value:
            biggest_value = len(value)
    return biggest_value
