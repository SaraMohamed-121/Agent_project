# Agent_project

**StoryTeller** is a high-performance AI Agentic system built using **LangGraph** to orchestrate creative workflows. The system autonomously manages a multi-node pipeline: it analyzes a user's initial idea, generates a comprehensive creative narrative, and produces a corresponding high-fidelity visual asset.

## Project Structure

The project follows a modular design for scalability:

* **`Streamlit_app.py`**: The main interface for user interaction and workflow visualization.
* **`graph_builder.py`**: Defines the LangGraph architecture and node connections.
* **`orchestrator.py`**: The "brain" of the agent that analyzes requirements and prepares prompts.
* **`story_writer.py`**: Specialized node focused on narrative drafting and creative writing.
* **`tools.py`**: Contains the `generate_image` tool for external API integrations.
* **`state.py`**: Defines the `StoryState` schema used to pass data between nodes.

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SaraMohamed-121/Agent_project.git
cd Agent_project
```

### 2. Set Up Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv agent_env
agent_env\Scripts\activate

```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory and add your API credentials:
```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
streamlit run Streamlit_app.py
```

---


