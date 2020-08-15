
def unique_path(directory, name_pattern):

    counter = 0
    while True:

        counter += 1
        path = directory / name_pattern.format(counter)
        print(f"what comes from input is:{directory} / {name_pattern}")
        print(f"unique_path for path is :{path}")
        print(f"path type is:{type(path)}")
        if not path.exists():
            return path


def add_empty_file(path):
    print(f"Create file:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
