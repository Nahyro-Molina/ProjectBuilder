# Standard libraries
from pathlib import Path

# third-party libraries

# User-defined libraries
"""
    No clue what this will consist of YET! But here is a brainstormed version of what I have in mind:
        - Wondering if there should be classes based off the project for example:
            - Should I have a class for "programming" project? IDK
        - For now I will have a generic class that will reference the project structure 
"""
class TestClass:
    def __init__(self, project_name, project_type):
        self._project_name = project_name
        self._project_type = project_type
        self._generate()

    def _generate(self):
        if not self.project_name:
            ValueError("DESIGN ERROR: PROJECT NAME NOT DEFINED, SHOULD NOT BE ABLE TO RUN!!")
        project = Path(project)
        ProjectConfig()
        
