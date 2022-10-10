import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
INI_CONFIGS_PATH = os.path.join(ROOT_DIR, "ini_configs")
DATA_FILES_PATH = os.path.join(ROOT_DIR, "data")
ALLURE_RESULTS_PATH = os.path.join(ROOT_DIR, "allure-results")
DRIVERS_PATH = os.path.join(ROOT_DIR, "Drivers")

if not os.path.exists(ALLURE_RESULTS_PATH):
    os.mkdir(ALLURE_RESULTS_PATH)
