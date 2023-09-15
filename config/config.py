import json

# Load configuration settings from config.json
def load_config():
    try:
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        return config_data
    except FileNotFoundError:
        print("Error: config.json not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in config.json.")
        return {}

# Sample usage
if __name__ == "__main__":
    config = load_config()

    # Access configuration settings
    api_key = config.get("api_key", "default_api_key")
    debug_mode = config.get("debug_mode", False)
    max_response_length = config.get("max_response_length", 200)
    language = config.get("language", "en")
    interview_topics = config.get("interview_topics", [])
    confidence_threshold = config.get("confidence_threshold", 0.5)

    # Use the configuration settings as needed in your project
    print("API Key:", api_key)
    print("Debug Mode:", debug_mode)
    print("Max Response Length:", max_response_length)
    print("Language:", language)
    print("Interview Topics:", interview_topics)
    print("Confidence Threshold:", confidence_threshold)
