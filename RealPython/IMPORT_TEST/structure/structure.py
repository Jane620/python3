import pathlib
import sys

import files

def main():
    try:
        # get the file absolute path ,like
        root = pathlib.Path(sys.argv[1]).resolve()
        print(f"root1 is : {root}")
        print(f"root2 is : {pathlib.Path.cwd()}")
    except IndexError:
        print("Need one argument: the root of the original file tree")
        raise SystemExit()

    new_root = files.unique_path(pathlib.Path.cwd(), "{:03d}")
    for path in root.rglob("*"):
        print(f"single path is :{path}")
        if path.is_file() and new_root not in path.parents:
            rel_path = path.relative_to(root)
            files.add_empty_file(new_root / rel_path)


if __name__ == '__main__':
    main()