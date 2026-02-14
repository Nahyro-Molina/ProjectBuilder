from TestClass import Project

# standard Library
from pathlib import Path
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
# ============================
#Objective: Construct a structured environment


def main():
    """ Runner """
    # Call other functions from here
    program()

def program():
    """???"""

    # ============= argument config ============================================
    project_name = f"{Path.cwd().name}"
    project_cli_usage_options = "%(prog)s usage options"
    project_cli_description = "Small Project building command line tool for building project"
    project_cli_epilog = "Start Project faster and with structure!!"
    project_cli_config = ArgumentParser(  prog=project_name,
                                formatter_class = ArgumentDefaultsHelpFormatter,
                                usage=project_cli_usage_options,
                                description=project_cli_description,
                                epilog=project_cli_epilog,
                                allow_abbrev=False
                                )
    project_cli_config.suggest_on_error = True

    # ============= argument definitions =======================================
    project_path_argument_help = "location of new project"
    project_cli_config.add_argument("project_path", default=".", help=project_path_argument_help)
    project_cli_config.add_argument("project_name", help="Name of the project to build")
    project_cli_config.add_argument("project_template", help="Name of the template to use")
    project_cli_config.print_help()

    # ============= argument parsed ============================================
    project_cli_args = project_cli_config.parse_args()
    project_path = project_cli_args.project_path
    project_name = project_cli_args.project_name
    project_template = project_cli_args.project_template
    test = Project(project_path, project_name, project_template)

if __name__ == "__main__":
    main()

