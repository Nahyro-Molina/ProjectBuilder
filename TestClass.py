# Standard libraries
from pathlib import Path

# third-party libraries
import yaml

# User-defined libraries

PB_CONFIG_FILE = ".pb/config.yml"
"""
    No clue what this will consist of YET! But here is a brainstormed version of what I have in mind:
        - Wondering if there should be classes based off the project for example:
            - Should I have a class for "programming" project? IDK
        - For now I will have a generic class that will reference the project structure 
"""
class Project:
    def __init__(self, project_path, project_name, project_template):
        self._project_path = project_path
        self._project_name = project_name
        self._project_template = project_template
        # TODO: self._project_folders = ProjectFolders()
        self._generate()

    @property
    def project_path(self):
        return self._project_path

    @property
    def project_name(self):
        return self._project_name

    @property
    def project_template(self):
        return self._project_template
    
    # ============== TODO ================
    #@property
    #def project_folders(self):
    #    return self._project_folders
    # ====================================

    def _generate(self):
        if not self.project_name:
            ValueError("DESIGN ERROR: PROJECT NAME NOT DEFINED, SHOULD NOT BE ABLE TO RUN!!")
        project = Path(f"{self.project_path}/{self.project_name}")
        self._projectConfig(project, self.project_template)

    def _projectConfig(self, project: Path, project_template: str):
        with open(PB_CONFIG_FILE, "r") as pb_config_file:
            config_data = dict(yaml.safe_load(pb_config_file))
        print(config_data["Designs"][project_template]["folders"])
        for folder_dict in config_data["Designs"][project_template]["folders"]:
            for folder_name, folder_items in folder_dict.items():
                project_folder = project / folder_name
                print(project_folder)
                # TODO: self.project_folders.add(project_folder, folder_items)
                project_folder.mkdir(parents=True, exist_ok=True)
        
        
