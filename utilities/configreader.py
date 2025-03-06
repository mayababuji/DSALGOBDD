import configparser
# Create a ConfigParser object
# config = configparser.ConfigParser()
# # Read the configuration file
# config.read('config.ini')
# # Access values from the configuration file
# application_name = config.get('DEFAULT', 'application_name')
# print(application_name)
# application_url = config.get('DEFAULT', 'application_url')
# print(application_url)

def read_config(file_path, section, key):
    """
        Read a value from a configuration file.

        :param file_path: Path to the configuration file.
        :param section: Section in the configuration file.
        :param key: Key in the specified section.
        :return: Value of the key in the specified section.
        """
    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Read the configuration file
    config.read(file_path)
    # Get the value from the specified section and key
    value = config.get(section, key)
    return value

# Example usage
if __name__ == "__main__":
    file_path = 'config.ini'
    section = 'DEFAULT'
    key = 'application_url'
    value = read_config(file_path, section, key)
    print(f"Value of {key} in section {section}: {value}")