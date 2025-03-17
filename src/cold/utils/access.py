import os

###########
## PATHS ##
###########

print(os.path.dirname(os.path.abspath(__file__)))


def get_path_to_utils():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def get_path_to_cold():
    path = os.path.dirname(get_path_to_utils())
    return path

def get_path_to_ontology():
    path = os.path.join(get_path_to_cold(), "ontology")
    return path

def get_path_to_models_ontology():
    path = os.path.join(get_path_to_cold(), "models", "ontology")
    return path


def get_path_to_ontology_files():
    path = os.path.join(get_path_to_models_ontology(), "files")
    return path


def get_path_to_ontology_files_formatted():
    path = os.path.join(get_path_to_ontology_files(), "formatted")
    return path


def get_path_to_ontology_files_originals():
    path = os.path.join(get_path_to_ontology_files(), "originals")
    return path
