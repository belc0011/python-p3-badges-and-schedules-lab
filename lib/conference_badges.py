def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    list_of_names = []
    for name in names:
        greeting = badge_maker(name)
        list_of_names.append(greeting)
    return list_of_names

def assign_rooms(names):
    counter = 1
    new_list = []
    while counter < 9:
        for name in names:
            greeting = f"Hello, {name}! You'll be assigned to room {counter}!"
            new_list.append(greeting)
            counter +=1
    return new_list

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
