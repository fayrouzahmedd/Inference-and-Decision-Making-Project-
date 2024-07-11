def translate_to_logic(sentence):
    # Define a dictionary of English to logic translations
    translations = {
        'and': '&',
        'or': '|',
        'not': '~',
        'if': '->',
        'then': '->',
        'iff': '<->',
        'if and only if': '<->',
        'implies': '->',
        'is equivalent to': '<->',
        'equals': '<->'
    }

    # Replace English words with logic symbols
    for word, symbol in translations.items():
        sentence = sentence.replace(word, symbol)

    # Add parentheses for clarity
    sentence = sentence.replace('(', '( ')
    sentence = sentence.replace(')', ' )')

    return sentence


def apply_rule_of_inference(rule, premises):
    # Define a dictionary of rules of inference
    rules_of_inference = {
        'modus ponens': '({0} -> {1}), {0} |- {1}',
        'modus tollens': '({0} -> {1}), ~{1} |- ~{0}',
        'disjunctive syllogism': '{0} | {1}, ~{0} |- {1}',
        'constructive dilemma': '({0} -> {1}), ({2} -> {3}), {0} | {2} |- {1} | {3}',
        'hypothetical syllogism': '({0} -> {1}), ({1} -> {2}) |- {0} -> {2}'
    }
# Check if the rule is valid
    if rule not in rules_of_inference:
        return 'Invalid rule of inference'

    # Extract the variables from the rule
    variables = rules_of_inference[rule].format(*premises).split(' |- ')[0].split(', ')

    # Construct the conclusion of the inference
    conclusion = rules_of_inference[rule].format(*premises).split(' |- ')[1]

    # Check if the premises match the variables in the rule
    if set(variables) != set(premises):
        return 'Invalid premises'

    return conclusion


# Example usage
english_sentence = "If it is raining and the sun is shining, then the grass is wet."
propositional_logic = translate_to_logic(english_sentence)
print(propositional_logic)

premises = ['P & R -> Q', 'P & R']
rule = 'modus ponens'
conclusion = apply_rule_of_inference(rule, premises)
print(conclusion)