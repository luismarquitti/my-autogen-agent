---
title: "ADR-0005: Local Code Execution"
status: "Accepted"
date: "2024-07-22"
authors: "Jules"
tags: ["architecture", "security", "execution"]
supersedes: ""
superseded_by: ""
---

#### Status

Accepted

#### Context

The `UserProxyAgent` is responsible for executing code and tools. A critical decision is determining the environment in which this code runs. The choice has significant implications for security, performance, and dependency management. The primary options are executing the code directly on the host machine or isolating it within a sandboxed environment like a Docker container.

#### Decision

We have configured the `UserProxyAgent` to execute code directly on the host machine by setting `"use_docker": False` in the `code_execution_config`. This means that when the `AssistantAgent` requests the execution of a tool, the corresponding Python function is run in the same process and environment as the main application script.

#### Consequences

##### Positive

- **POS-001**: **Simplicity and Performance**: This approach avoids the overhead of creating and managing Docker containers, resulting in faster execution and a simpler debugging experience.
- **POS-002**: **No Docker Dependency**: The application does not require Docker to be installed or running on the host machine, which lowers the barrier to entry for developers and simplifies deployment.
- **POS-003**: **Direct Filesystem Access**: The executed code has direct access to the local filesystem, which is necessary for tools that need to read and write files, such as the `lint_and_fix_markdown` function.

##### Negative

- **NEG-001**: **Security Risks**: Code is executed with the same permissions as the user running the script. This is a significant security risk if the code to be executed is not fully trusted, as it could access or modify files, or perform other malicious actions on the host system.
- **NEG-002**: **Environment Inconsistency**: The success of the code execution depends on the host machine having all the necessary libraries and dependencies installed. This can lead to the "it works on my machine" problem.
- **NEG-003**: **Lack of Isolation**: There is no isolation between the executed code and the main application. A crash or unhandled exception in the executed code will terminate the entire application.

#### Alternatives Considered

##### Docker-Based Execution

- **ALT-001**: **Description**: Setting `"use_docker": True` in the `code_execution_config`. This would instruct `pyautogen` to execute the code inside a sandboxed Docker container.
- **ALT-002**: **Rejection Reason**: For the current scope of the project, which involves a single, trusted tool (`pymarkdown-linter`), the added complexity of managing Docker images, volumes for file access, and the performance overhead was deemed unnecessary. If the system were to execute untrusted, LLM-generated code, this would be the preferred approach.

##### Web API Execution

- **ALT-003**: **Description**: Exposing the `lint_and_fix_markdown` functionality as a local web service and having the `UserProxyAgent` make an API call to it.
- **ALT-004**: **Rejection Reason**: This would introduce significant architectural complexity, including the need to run and manage a separate server process, handle network requests, and serialize data. It is overly complex for a tool that operates on the local filesystem.

#### Implementation Notes

- **IMP-001**: The `code_execution_config` for the `Executor` agent in `src/main.py` is explicitly set to `{"use_docker": False}`.
- **IMP-002**: All required dependencies for the executed tools (e.g., `pymarkdown-linter`) must be installed in the same Python environment as the main application.
- **IMP-003**: This decision implies that all tools integrated into the system are fully trusted and well-tested.

#### References

- **REF-001**: ADR-0002: Two-Agent Architecture
- **REF-002**: [AutoGen Code Execution Documentation](https://microsoft.github.io/autogen/docs/topics/code-executors)
