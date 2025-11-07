---
title: "ADR-0003: Tool Integration via Function Calling"
status: "Accepted"
date: "2024-07-22"
authors: "Jules"
tags: ["architecture", "tooling", "integration"]
supersedes: ""
superseded_by: ""
---

#### Status

Accepted

#### Context

For the multi-agent system to perform useful tasks, it needs the ability to interact with external tools and execute code. This requires a mechanism to bridge the gap between the LLM's natural language understanding and the structured, callable functions of the Python environment. The mechanism should be reliable, easy to define, and provide the LLM with enough information to correctly invoke the tools.

#### Decision

We have decided to integrate tools using `pyautogen`'s built-in function-calling mechanism. This approach involves two key steps:

1.  **Defining a Tool Schema**: A JSON schema is created to describe the tool's name, purpose, and parameters. This schema is attached to the `AssistantAgent`'s `llm_config["tools"]` attribute, allowing the LLM to understand how and when to use the tool.
2.  **Registering the Function**: The actual Python function is registered with the `UserProxyAgent` using the `register_function` method, which maps the function name from the schema to the callable Python object.

This creates a robust connection where the `AssistantAgent` can request a tool's execution in a structured format, and the `UserProxyAgent` can reliably execute the corresponding function.

#### Consequences

##### Positive

- **POS-001**: **Structured Communication**: The use of JSON schemas ensures that the communication between the planning agent and the executing agent is structured and predictable, reducing the risk of misinterpretation.
- **POS-002**: **Improved LLM Accuracy**: Providing the LLM with a clear tool schema makes it more likely to generate correct function calls with the appropriate parameters.
- **POS-003**: **Decoupling**: The tool schema is decoupled from the function's implementation, allowing us to modify the function's internal logic without having to change how the LLM calls it, as long as the interface remains the same.

##### Negative

- **NEG-001**: **Maintenance Overhead**: For every new tool, both a schema and a function registration are required, which adds a small amount of maintenance overhead.
- **NEG-002**: **Schema-Implementation Mismatch**: Any discrepancy between the JSON schema and the Python function's signature can lead to runtime errors. This requires careful synchronization between the two.
- **NEG-003**: **Limited to Function Calls**: This pattern is primarily designed for calling functions and may not be the best fit for more complex integrations that require stateful connections or streaming data.

#### Alternatives Considered

##### Parsing Natural Language

- **ALT-001**: **Description**: The `AssistantAgent` could generate natural language instructions (e.g., "run the linter on `input.md`"), and the `UserProxyAgent` would parse this text to determine which function to call.
- **ALT-002**: **Rejection Reason**: This approach is brittle and prone to errors. Relying on regex or simple string matching to parse commands is not as reliable as the structured data provided by function calling. It would also require more complex logic in the `UserProxyAgent`.

##### Custom Tool-Use Protocol

- **ALT-003**: **Description**: We could have designed our own protocol for tool use, for example, by having the LLM generate a specific JSON format in its messages that our `UserProxyAgent` would be programmed to interpret.
- **ALT-004**: **Rejection Reason**: This would be reinventing the wheel. The function-calling mechanism provided by `pyautogen` (and the underlying LLM providers) is a standardized and battle-tested solution for this exact problem.

#### Implementation Notes

- **IMP-001**: The JSON schema for the `lint_and_fix_markdown` tool is defined in `src/main.py`.
- **IMP-002**: The schema is passed to the `LinterAgent` via the `llm_config["tools"]` dictionary key.
- **IMP-003**: The `lint_and_fix_markdown` Python function is registered with the `Executor` agent using a `function_map`.

#### References

- **REF-001**: ADR-0002: Two-Agent Architecture
- **REF-002**: [AutoGen Tool Use Documentation](https://microsoft.github.io/autogen/docs/topics/tool-use)
