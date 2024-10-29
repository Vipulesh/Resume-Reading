# validator_agent.py
import re
import ast

class ValidatorAgent:
    def __init__(self, extracted_data):
        self.data = ast.literal_eval(extracted_data[7:len(extracted_data)-3])

    def validate_entities(self):
        validation_results = {
            "name": self._validate_name(self.data.get("personal_info", {}).get("name")),
            "email": self._validate_email(self.data.get("personal_info",{}).get("email")),
            "phone": self._validate_phone(self.data.get("personal_info",{}).get("phone_no")),
            "education": self._validate_education(self.data.get("education")),
            "work_experience": self._validate_experience(self.data.get("work_experience")),
            "skills": self._validate_skills(self.data.get("skills"))
        }
        return validation_results

    def _validate_name(self, name):
        return bool(name)  # Simple check; could be more complex

    def _validate_email(self, email):
        return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)) if email else False

    def _validate_phone(self, phone):
        return bool(re.match(r'^\+?\d[\d -]{8,}\d$', phone)) if phone else False

    def _validate_education(self, education):
        return bool(education) and len(education) > 0

    def _validate_experience(self, experience):
        return bool(experience) and len(experience) > 0

    def _validate_skills(self, skills):
        return bool(skills) and len(skills) > 0

def run_agent(extracted_data):
    validator_agent = ValidatorAgent(extracted_data)
    validation_results = validator_agent.validate_entities()
    return validation_results