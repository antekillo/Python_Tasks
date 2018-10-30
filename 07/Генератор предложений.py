import random
name = ['Олег', 'Паша', 'Захар']
verb = ['Дети', 'мальчики', 'молодцы']

def nm(name):
    num_word = len(name)
    num_picked = random.randint(0, num_word-1)
    name_picked = name[num_picked]
    return name_picked

def vrb(verb):
    num_word = len(verb)
    num_picked = random.randint(0, num_word-1)
    verb_picked = verb[num_picked]
    return verb_picked

print(nm(name), vrb(verb))
