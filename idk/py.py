def extract_json(response_text):
    try:
        # First try to find JSON array pattern
        json_match = re.search(r'\[[\s\S]*\]', response_text)
        if json_match:
            potential_json = json_match.group(0)
            # Clean up the JSON string
            cleaned_json = re.sub(r',\s*}', '}', potential_json)
            cleaned_json = re.sub(r',\s*\]', ']', cleaned_json)
            # Parse the JSON
            return json.loads(cleaned_json)
        else:
            print("No JSON array found in response")
            return None
    except Exception as e:
        print(f"Error extracting JSON: {e}")
        print(f"Raw response: {response_text}")
        return None

def generate_content_with_retries(prompt_text, retries=3, wait_time=60):
    for attempt in range(1, retries + 1):
        try:
            response = model.generate_content(prompt_text)
            return response.text
        except Exception as e:
            print(f"Attempt {attempt}: Error - {e}")
            if attempt < retries:
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
    return None
