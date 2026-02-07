import pathlib
#Objective: Construct a structured environment


def main():
    """ Runner """
    # Call other functions from here
    program()

def program():
    """???"""
    # We need to create the folders
    pathlib.Path("libraries").mkdir()
    pathlib.Path("scripts").mkdir()
    pathlib.Path("build").mkdir()
    pathlib.Path("tests").mkdir()
    pathlib.Path("wiki").mkdir()
    pathlib.Path("apis").mkdir()
    pathlib.Path("docs").mkdir()
    pathlib.Path("bin").mkdir()
    pathlib.Path("src").mkdir()

    # I have the folders now what?


if __name__ == "__main__":
    main()

