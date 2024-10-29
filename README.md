# Resume Processing and Validation System

This project is designed to read resumes in PDF or DOCX format, extract structured information, and validate the extracted entities. The system leverages various agents to perform these tasks and integrates with external APIs for enhanced functionality.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Agents](#agents)
- [Environment Variables](#environment-variables)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-repo/resume-processing.git
    cd resume-processing
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following variables:
    ```env
    GEMINI_API_KEY=your_gemini_api_key
    LANGSMITH_API_KEY=your_langsmith_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Specify the resume file path**:
    Modify the `file_path` variable in `main.py` to point to the resume file you want to process.

## Agents

### ResumeReaderAgent

Located in [`agents/resume_reader_agent.py`](agents/resume_reader_agent.py), this agent reads resumes in PDF or DOCX format and extracts the text.

### ExtractorAgent

Located in [`agents/extractor_agent.py`](agents/extractor_agent.py), this agent extracts structured information from the resume text using the Gemini model.

### ValidatorAgent

Located in [`agents/validator_agent.py`](agents/validator_agent.py), this agent validates the extracted entities to ensure their correctness.

## Environment Variables

- `GEMINI_API_KEY`: API key for the Gemini model.
- `LANGSMITH_API_KEY`: API key for Langsmith.
- `GROQ_API_KEY`: API key for Groq.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
