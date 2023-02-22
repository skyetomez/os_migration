"""
Quick python script to generate a tree structure of a file system
Needs to be applied to Windows and Ubuntu

"""

import os  # not operating system speciic


try:
    from tree import DirectoryTree

except ModuleNotFoundError as e:
    import sys

    # ----- pull repo locally ------ #
    clone = "git clone https://github.com/peb-peb/tree.git"
    os.system(clone)
    cwd = os.getcwd()

    # ------- get module path ------ #
    tree_lib = os.path.join(cwd, "tree")
    sys.path.append(tree_lib)

    from tree import DirectoryTree

# ---- get host and hostname and meta data ----


# top directory
def _init() -> str:
    print("paste starting directory:", flush=True)
    root_dir = str(input()).strip()

    if not os.path.isabs(root_dir):
        root_dir = os.path.abspath(root_dir)

    if os.path.exists(root_dir):
        print(f"{os.path.basename(root_dir)} found in {os.path.dirname(root_dir)}")
        return root_dir

    else:
        raise NotADirectoryError


def _save() -> str:
    save_path = os.getcwd()
    print(f"files will be saved in f{save_path}. type the save file name:\n")
    filename = str(input()).strip()
    fpath = os.path.join(save_path, filename)
    return fpath


def main() -> None:
    tree = DirectoryTree(root_dir=_init(), output_file=_save())
    tree.generate()
    return None


if __name__ == "__main__":
    main()
