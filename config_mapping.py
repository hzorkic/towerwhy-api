# tower_configuration.py

def determine_lighting_configuration(description):
    config_mapping = {
        "lit orange": "orange",
        "lights up orange": "orange",
        "darkened tower": "dark",
        "dark": "dark",
        "white tower": "white",
        "white lighting": "white",
        "special lighting": "special",
        "special": "special",
        "burnt orange": "orange",
        "orange": "orange"
    }

    # Check description against config_mapping
    for keyword, config in config_mapping.items():
        if keyword in description.lower():
            return config
    
    # If no match found, return "unknown"
    return "unknown"