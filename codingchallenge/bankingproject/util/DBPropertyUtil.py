import configparser


class DBPropertyUtil:

    @staticmethod
    def get_connection_string(file_name: str):
        config = configparser.ConfigParser()

        try:
            config.read(file_name)
            # Ensure the 'DATABASE' section exists in the config file
            if 'DATABASE' not in config.sections():
                raise KeyError("Section 'DATABASE' not found in the config file")
            return config['DATABASE']['connection_string']

        except KeyError as e:
            print(f"Error: {e}")
            return None
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

if __name__ == "__main__":
    file_name = "db.properties"
    connection_string = DBPropertyUtil.get_connection_string(file_name)
    print(f"Connection string retrieved: {connection_string}")