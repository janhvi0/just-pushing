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