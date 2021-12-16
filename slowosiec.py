import plwn
import regex as re


def get_hyponyms(input_words, final_output=[]):
    output_words = []
    for word in input_words:
        word = word.replace('_', ' ')
        lexical_units = wn.lexical_units(lemma=u'{}'.format(word))
        if any([str(elem.domain) == 'Domain.msc' for elem in lexical_units]):
            final_output = list(set(final_output + [word]))
            units = wn.synsets(lemma=u'{}'.format(word))
            for unit in units:
                if any([str(elem.domain) == 'Domain.msc' for elem in unit.lexical_units]):
                    for elem in unit.related_pairs():
                        if str(elem[0]) == 'hiperonimia':
                            for elem in re.findall('(?<=[\{ ]).+?(?=\.)', str(elem[1])):
                                elem = elem.replace('_', ' ')
                                if elem not in final_output:
                                    output_words.append(elem)
    print(final_output)
    if not output_words:
        return final_output
    return get_hyponyms(output_words, final_output)


wn = plwn.load('plwn-3.0-v5.db', 'sqlite3')

output = get_hyponyms(['budynek'])
