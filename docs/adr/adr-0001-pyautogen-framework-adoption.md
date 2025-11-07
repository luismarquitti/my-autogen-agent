---
title: "ADR-0001: pyautogen Framework Adoption"
status: "Accepted"
date: "2024-07-22"
authors: "Jules"
tags: ["architecture", "framework"]
supersedes: ""
superseded_by: ""
---

#### Status

Accepted

#### Context

The project's primary goal is to develop a multi-agent system capable of automating complex tasks. This requires a framework that simplifies agent creation, communication, and the integration of external tools. The key requirements include support for different LLM providers, clear patterns for agent interaction, and the ability to execute code or functions in a controlled manner.

#### Decision

We have decided to adopt the `pyautogen` framework as the core technology for this project. `pyautogen` provides a high-level API for creating `AssistantAgent` and `UserProxyAgent` instances, which map well to our intended architecture of an orchestrator and an executor. The framework's native support for tool schemas (function calling) and its configuration-driven approach (via `OAI_CONFIG_LIST`) meet our immediate technical needs.

#### Consequences

##### Positive

- **POS-001**: **Accelerated Development**: `pyautogen` provides pre-built agent classes and communication patterns, significantly reducing the boilerplate code required to set up a multi-agent system.
- **POS-002**: **Built-in Tool Integration**: The framework has native support for function calling, which simplifies the process of giving agents access to external tools and functions.
- **POS-003**: **Extensibility**: The framework is extensible, allowing for the creation of custom agent types and more complex interaction patterns (e.g., `GroupChat`) as the project evolves.

##### Negative

- **NEG-001**: **Opinionated Design**: The framework's architecture is opinionated, which may constrain us to specific agent interaction patterns.
- **NEG-002**: **Rapid Evolution**: As a relatively new framework, `pyautogen` is under active development, which could introduce breaking changes in future updates.
- **NEG-003**: **Learning Curve**: The concepts of `UserProxyAgent`, `AssistantAgent`, and the registration of function maps may require a learning curve for new developers.

#### Alternatives Considered

##### LangChain

- **ALT-001**: **Description**: LangChain is a popular framework for developing applications powered by language models. It provides a more general-purpose set of tools for chaining LLM calls and integrating with various data sources.
- **ALT-002**: **Rejection Reason**: While powerful, LangChain is less specialized for multi-agent conversations. Implementing the desired two-agent conversational pattern for tool execution would require more custom orchestration code compared to `pyautogen`'s native implementation.

##### Custom Framework

- **ALT-003**: **Description**: We considered building a lightweight, custom framework from scratch to handle agent communication and tool execution.
- **ALT-004**: **Rejection Reason**: This approach would provide maximum flexibility but would also require a significant investment in development and maintenance, reinventing many of the features already available in `pyautogen`. The long-term cost and effort were deemed too high for the scope of this project.

##### Do Nothing

- **ALT-005**: **Description**: Proceeding without a dedicated framework, using only raw API calls to LLMs.
- **ALT-006**: **Rejection Reason**: This would lead to a tightly coupled, monolithic codebase that would be difficult to maintain, extend, and debug. A framework is essential for providing structure and scalability.

#### Implementation Notes

- **IMP-001**: All agents will be instantiated and configured within the `src/main.py` file.
- **IMP-002**: The project will rely on the `pyautogen` package, installed via pip, as a core dependency.
- **IMP-003**: LLM configuration will be managed via the `OAI_CONFIG_LIST` environment variable, as recommended by the `pyautogen` documentation.

#### References

- **REF-001**: [Official pyautogen GitHub Repository](https://github.com/microsoft/autogen)
