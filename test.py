import builtins

for name in dir(builtins):
    if isinstance(getattr(builtins, name), type):
        print(name)