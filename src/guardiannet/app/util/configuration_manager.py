import json
from os.path import exists as file_exists


class ConfigurationManager:
    @staticmethod
    def initializeConfiguration():
        configurations = {
            "setting": {
                "iface": "eth0",
                "batchSize": 32,
            },
            "comboBox": {
                "cmbBatchSize": ["4", "8", "16", "32", "64", "128"]
            }
        }

        try:
            with open('config/config.json', 'w') as jsonfile:
                json.dump(configurations, jsonfile, indent=4)
        except FileNotFoundError as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")
            return False
        finally:
            jsonfile.close()

        return True

    @staticmethod
    def doesConfigurationExist():
        return file_exists("config/config.json")

    @staticmethod
    def loadConfiguration() -> dict:
        try:
            with open("config/config.json", "r") as jsonfile:
                configurations = json.load(jsonfile)
        except FileNotFoundError as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")
        finally:
            jsonfile.close()

        return configurations

    @staticmethod
    def updateConfiguration(configurations):
        try:
            with open('config/config.json', 'w') as jsonfile:
                json.dump(configurations, jsonfile, indent=4)
        except FileNotFoundError as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")
            return False
        finally:
            jsonfile.close()

        return True
