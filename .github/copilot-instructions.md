# 🤖 Copilot Instructions for my-autogen-agent

## Project Overview
This repository is a robust Python project for building AI agents using the (py)AutoGen framework. The architecture is designed for clarity, reproducibility, and extensibility, with a focus on agent-tool orchestration and practical automation workflows.

## Key Components & Structure
- **src/main.py**: Entry point. Demonstrates a two-agent system:
  - `LinterAgent` (AssistantAgent): Orchestrates Markdown linting using a tool.
  - `Executor` (UserProxyAgent): Executes registered Python functions/tools.
- **input.md**: Example Markdown file for linting/fixing.
- **.env**: Stores LLM API keys/config (never commit this!).
- **README.md**: Comprehensive onboarding, setup, and workflow documentation.

## Agent Patterns & Conventions
- Agents are defined using `autogen.AssistantAgent` and `autogen.UserProxyAgent`.
- Tools are registered as Python functions and described to the LLM via a JSON schema.
- The main workflow is initiated by `executor.initiate_chat(linter_agent, message=...)`.
- All agent configuration (models, API keys) is loaded from `.env` using `autogen.config_list_from_env()`.
- Code execution is local (`use_docker: False`), not containerized by default.

## Developer Workflows
- **Setup**: Use Python 3.10+, create a venv, install dependencies with `pip install -r requirements.txt` (or as listed in README).
- **Run Example**: Activate venv, then `python src/main.py` to see the agent workflow in action.
- **Lint/Format**: Uses `pymarkdown-linter[all]`, `black`, and `ruff` (see `.vscode/settings.json` in README for VSCode config).
- **API Keys**: Place your OpenAI or Gemini key in `.env` as per README instructions.

## Integration & Extensibility
- To add new tools, define a Python function and register it with the `Executor` agent.
- To add new agents, follow the pattern in `src/main.py` and document in `README.md`.
- LLM model and provider are controlled via the `OAI_CONFIG_LIST` env variable.

## Project-Specific Patterns
- All agent and tool schemas are explicitly described for LLM function-calling.
- Example workflows are reproducible and documented step-by-step in the README.
- Markdown linting/fixing is the canonical example, but the pattern generalizes to other tools.

## References
- See `README.md` for full onboarding, environment, and workflow details.
- See `src/main.py` for agent orchestration and tool registration patterns.
- Example `.env` and VSCode settings are provided in the README.

---

For new agents or tools, follow the explicit schema and registration patterns. For questions, consult the README or use the documented Copilot chat prompts for context-aware help.
