import json
import google.generativeai as genai
import re
import time

# Configure the Gemini API
genai.configure(api_key="AIzaSyD-5J4tX-A8xclZEggNedMUoaYk8SMeSuw")
model = genai.GenerativeModel("gemini-1.5-flash")

prompts_file = r"G:\Bootcoding\aptitude_que_generator\Prompt_json\test.json"

# Load prompts from JSON file
with open(prompts_file, "r") as file:
    prompts = json.load(file)

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

# Main process
formatted_results = []
with open(prompts_file, "r") as file:
    prompts = json.load(file)

for prompt in prompts:
    topic = prompt["topic"]
    sub_topic = prompt["sub_topic"]
    question_prompt = prompt["question_prompt"]

    print(f"Generating content for: {topic} - {sub_topic}")
    raw_response = generate_content_with_retries(question_prompt)
    
    if raw_response:
        questions = extract_json(raw_response)
        if questions:
            for question in questions:
                # Check for both possible field name formats
                formatted_question = {
                    "title": question.get("title", ""),
                    "option_1": question.get("option1") or question.get("option_1", ""),
                    "option_2": question.get("option2") or question.get("option_2", ""),
                    "option_3": question.get("option3") or question.get("option_3", ""),
                    "option_4": question.get("option4") or question.get("option_4", ""),
                    "correct_answer": question.get("correct_option") or question.get("correct_answer", ""),
                    "topic": topic,
                    "sub_topic": sub_topic,
                    "difficulty_level": question.get("difficulty_level", "medium")
                }
                
                # Only add if all required fields have values
                if all(formatted_question[key] for key in ["title", "option_1", "option_2", "option_3", "option_4", "correct_answer"]):
                    formatted_results.append(formatted_question)
                else:
                    print(f"Skipping incomplete question: {question}")

# Save results
output_file = r"G:\Bootcoding\aptitude_que_generator\JSON_FILES\test_Que.json"
with open(output_file, "w") as file:
    json.dump(formatted_results, file, indent=4)

print(f"Questions have been saved to {output_file}")