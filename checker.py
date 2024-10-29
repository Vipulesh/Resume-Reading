# main.py
from agents.resume_reader_agent import ResumeReaderAgent
from agents.extractor_agent import ExtractorAgent
from agents.validator_agent import ValidatorAgent
import ast
from langsmith import traceable

def main(file_path):
    # Step 1: Read Resume
    reader_agent = ResumeReaderAgent(file_path)
    resume_text = reader_agent.read_resume()

    # Step 2: Extract Entities
    extractor_agent = ExtractorAgent()
    extracted_data = extractor_agent.extract_entities(resume_text)
    print("Extracted Data:", extracted_data)

    # Step 3: Validate Entities
    validator_agent = ValidatorAgent(extracted_data)
    validation_results = validator_agent.validate_entities()
    print("Validation Results:", validation_results)

    # Human Feedback Loop (Placeholder)
    # Integrate feedback collection here as needed
    for key, valid in validation_results.items():
        if not valid:
            print(f"Warning: '{key}' data may need correction.")
            # In a real implementation, prompt user for correction or confirm the flag.

if __name__ == "__main__":
    file_path = "211010258_Vipulesh.pdf"  # Replace with the actual file path
    main(file_path)
