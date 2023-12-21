def format_json_response(json_data):
    formatted_string = ""

    # Basic information
    formatted_string += "Response ID: {}\n".format(json_data["id"])
    formatted_string += "Model Used: {}\n".format(json_data["model"])
    formatted_string += "Creation Timestamp: {}\n\n".format(json_data["created"])

    # Message details
    message = json_data["choices"][0]["message"]
    formatted_string += "Role: {}\n".format(message["role"])
    formatted_string += "Content: {}\n\n".format(message["content"].strip())

    # Usage details
    usage = json_data["usage"]
    formatted_string += "Usage Details:\n"
    formatted_string += "\tPrompt Tokens: {}\n".format(usage["prompt_tokens"])
    formatted_string += "\tCompletion Tokens: {}\n".format(usage["completion_tokens"])
    formatted_string += "\tTotal Tokens: {}\n".format(usage["total_tokens"])

    return formatted_string


def format_and_get_moderation_response(api_response):
    # Extract information from the API response
    categories = api_response.categories
    category_scores = api_response.category_scores
    flagged = api_response.flagged

    # Create a formatted string to capture the content
    formatted_content = "Categories:\n"
    formatted_content += f"Harassment: {categories.harassment}\n"
    formatted_content += f"Harassment Threatening: {categories.harassment_threatening}\n"
    formatted_content += f"Hate: {categories.hate}\n"
    formatted_content += f"Hate Threatening: {categories.hate_threatening}\n"
    formatted_content += f"Self Harm: {categories.self_harm}\n"
    formatted_content += f"Self Harm Instructions: {categories.self_harm_instructions}\n"
    formatted_content += f"Self Harm Intent: {categories.self_harm_intent}\n"
    formatted_content += f"Sexual: {categories.sexual}\n"
    formatted_content += f"Sexual Minors: {categories.sexual_minors}\n"
    formatted_content += f"Violence: {categories.violence}\n"
    formatted_content += f"Violence Graphic: {categories.violence_graphic}\n"
    
    formatted_content += "Category Scores:\n"
    formatted_content += f"Harassment Score: {category_scores.harassment}\n"
    formatted_content += f"Harassment Threatening Score: {category_scores.harassment_threatening}\n"
    formatted_content += f"Hate Score: {category_scores.hate}\n"
    formatted_content += f"Hate Threatening Score: {category_scores.hate_threatening}\n"
    formatted_content += f"Self Harm Score: {category_scores.self_harm}\n"
    formatted_content += f"Self Harm Instructions Score: {category_scores.self_harm_instructions}\n"
    formatted_content += f"Self Harm Intent Score: {category_scores.self_harm_intent}\n"
    formatted_content += f"Sexual Score: {category_scores.sexual}\n"
    formatted_content += f"Sexual Minors Score: {category_scores.sexual_minors}\n"
    formatted_content += f"Violence Score: {category_scores.violence}\n"
    formatted_content += f"Violence Graphic Score: {category_scores.violence_graphic}\n"
    
    formatted_content += f"Flagged: {flagged}\n"

    return formatted_content
