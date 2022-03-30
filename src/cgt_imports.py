import importlib
import sys
from pathlib import Path

"""
This makes sure all modules are reloaded from new files, when the addon is removed and a new version is installed in the same session,
or when Blender's 'Reload Scripts' operator is run manually.
"""

SUB_DIRS = ['src/import_models', 'src/interface', 'src/management', 'src/setup', 'src.utils']
INIT_MODULES = [
    '.src.interface.Properties',
    '.src.interface.Operators',
    '.src.interface.Panels',
    '.src.interface.Registration'
]

FILE = Path(__file__)
PACKAGE_PATH = FILE.parent.parent
PACKAGE_NAME = PACKAGE_PATH.name


def import_module(module):
    print(f"importing {PACKAGE_NAME}{module}...")
    importlib.import_module(f"{PACKAGE_NAME}{module}")


def reload_module(module):
    print(f"reloading {PACKAGE_NAME}{module}...")
    importlib.reload(sys.modules[f"{PACKAGE_NAME}{module}"])


def get_reload_list(sub_dirs):
    reload_list = []

    for sub_dir in sub_dirs:
        files = [p for p in sub_dir.rglob("*.py") if p.stem != '__init__']
        for file in files:
            parents = get_parents(file, [])
            imp_path = ""
            for parent in reversed(parents):
                imp_path += f".{parent}"
            imp_path += f".{file.stem}"
            reload_list.append(imp_path)
    return reload_list


def get_parents(file: Path, parents: list):
    if file.parent.name != PACKAGE_NAME:
        parents.append(file.parent.name)
        get_parents(file.parent, parents)
    return parents


def manage_imports(reload: bool = False):
    for module in INIT_MODULES:
        print("module to import:", module)
        import_module(module)

    sub_dirs = [PACKAGE_PATH / sub_dir for sub_dir in SUB_DIRS]
    reload_list = get_reload_list(sub_dirs)

    for module in reload_list:
        if reload is True:
            import_module(module)
            reload_module(module)
        else:
            import_module(module)
    print(f"Reloaded {PACKAGE_NAME} successfully")


if __name__ == '__main__':
    addons_folder = str(PACKAGE_PATH)
    sys.path.append(addons_folder)

    # reload modules besides bpy
    sub_dirs = [PACKAGE_PATH / sub_dir for sub_dir in SUB_DIRS[1:]]
    print(sub_dirs)
    reload_list = get_reload_list(sub_dirs)
    print(reload_list)
    for module in reload_list:
        print(f"importing {module}...")
        import_module(module)
