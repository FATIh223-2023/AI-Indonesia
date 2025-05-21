def clean_text(text):
    # Function to clean and preprocess the input text
    text = text.lower()  # Convert to lowercase
    text = text.strip()  # Remove leading and trailing whitespace
    # Add more preprocessing steps as needed (e.g., removing punctuation, stop words)
    return text

def format_training_data(data):
    # Function to format the training data into the required structure
    formatted_data = []
    for item in data:
        question = clean_text(item['question'])
        response = clean_text(item['response'])
        formatted_data.append({'question': question, 'response': response})
    return formatted_data