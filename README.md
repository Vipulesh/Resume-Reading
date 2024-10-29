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

## Resume Processing Workflow Code Overview

This code snippet defines a structured workflow for processing resumes, extracting data, and validating entities. Key components include `langgraph` and `langchain` for state-based control flow, custom agents for specific tasks, and secure environment variable management.

### Libraries and Imports

- **`TypedDict`, `Literal`**: Provides type-checking and literal types for improved type safety.
- **`random`, `json`, `os`, `getpass`**: Handles randomness, JSON parsing, file system access, and secure user input.
- **`IPython.display`**: Used for displaying the resulting graph.
- **`langgraph`, `langchain`**: Used for workflow control and interactions with language models.
- **Custom agents**: `ResumeReaderAgent`, `ExtractorAgent`, `ValidatorAgent` are custom classes for specific tasks within resume processing.
- **Environment management**: `.env` loading via `dotenv` secures API keys.

### Environment Variables and Setup

Environment variables are loaded from a `.env` file:
- `LANGSMITH_API_KEY`: Secures the connection to `Langchain` API.
- `GROQ_API_KEY`: Secures access to the `Groq` API for language model interactions.

These are set up for tracing, endpoint management, and integration with the `ChatGroq` language model.

### Key Functions

- **`get_resume_text(file_path: str) -> str`**: Reads and returns text from a resume file using `ResumeReaderAgent`.
- **`extract_entities(resume_text: str) -> str`**: Extracts structured information from the resume text using `ExtractorAgent`.
- **`validate_entities(extracted_data: str) -> str`**: Validates extracted data using `ValidatorAgent` to ensure accuracy.

### Workflow Definition with `StateGraph`

1. **Nodes**:
   - **`assistant`**: Uses the LLM with bound tools to process instructions.
   - **`tools`**: Contains the defined functions and conditionally routes based on tool calls.

2. **Edges and Conditional Routing**:
   - Workflow starts at `START`, moves to `assistant`, and uses `tools_condition` to check if further processing in `tools` is needed.
   - The graph routes back to `assistant` or ends based on conditions.

3. **Displaying the Workflow**:
   - `display()` is used to visualize the compiled workflow graph with the Mermaid graphing library.

### Running the Workflow

The process is initiated by providing a file path to a resume PDF and an instruction message. The `react_graph` processes the messages, calling appropriate agents and tools in sequence, and returns validated, structured information from the resume.


## Environment Variables

- `GEMINI_API_KEY`: API key for the Gemini model.
- `LANGSMITH_API_KEY`: API key for Langsmith.
- `GROQ_API_KEY`: API key for Groq.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
