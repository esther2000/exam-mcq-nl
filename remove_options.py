import json
import random


def modify_json(data):
    options = item['options']
    correct_answer = options[item['answer']]
    
    while len(options) > 4:
        # Remove a random option that is not the correct answer
        options_to_remove = [opt for opt in options if opt != correct_answer]
        option_to_remove = random.choice(options_to_remove)
        options.remove(option_to_remove)
    
    # Update the answer index
    item['answer'] = options.index(correct_answer) + 1

    return data


new_json = []
with open("train.json", "r") as f:
    data = json.load(f)
    for item in data:
        data = modify_json(item)
        new_json.append(data)
    with open("questions_modified.json", "w") as f_out:
        json.dump(new_json, f_out)

