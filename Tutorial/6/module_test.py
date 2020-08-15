
# execute moduel as script
def func():
    # TODO
    pass

if __name__ == '__main__':
    import sys
    func(int(sys.argv[1]))

# dir: list the names mduels defines
import sys
dir(sys)

# import * : author need to decide which names should be inported
# int __init__.py file
__all__ = ["name1", "name2", "name3"]

# relative path
# . local path
# .. the same path from local folder
# ..module1 the module1 folder
from . import func1
from .. import module1
from ..module1 import func1