def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: ((-x[1]), -len(x[0]), x[0]))

    for x in kwargs:
        return '\n'.join([f"{key}: {value}" for key, value in kwargs])


print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))
