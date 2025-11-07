---
title: "ADR-0002: Two-Agent Architecture"
status: "Accepted"
date: "2024-07-22"
authors: "Jules"
tags: ["architecture", "agent-design"]
supersedes: ""
superseded_by: ""
---

#### Status

Accepted

#### Context

To effectively automate tasks, the system needs a clear separation of concerns between high-level planning and low-level execution. The planning component should be responsible for interpreting user requests and breaking them down into actionable steps, while the execution component should handle the implementation of those steps, including running code and interacting with tools. This separation is crucial for modularity, debuggability, and security.

#### Decision

We have implemented a two-agent architecture consisting of an `AssistantAgent` (`LinterAgent`) and a `UserProxyAgent` (`Executor`).

-   The **`AssistantAgent`** acts as the "brains" of the operation. It is connected to an LLM and is responsible for understanding the user's intent, planning the steps to achieve the goal, and deciding which tools to use.
-   The **`UserProxyAgent`** acts as the "hands" of the operation. It does not connect to an LLM but is configured to execute code and functions on behalf of the `AssistantAgent`.

This pattern creates a clear conversational workflow where the `AssistantAgent` requests an action and the `UserProxyAgent` executes it and reports back the result.

#### Consequences

##### Positive

- **POS-001**: **Clear Separation of Concerns**: The architecture clearly separates the LLM-driven planning from the code execution, making the system easier to understand, debug, and maintain.
- **POS-002**: **Enhanced Security**: By isolating code execution within the `UserProxyAgent`, we can implement security measures (such as running code in a Docker container, although not currently enabled) without affecting the `AssistantAgent`'s planning capabilities.
- **POS-003**: **Modularity**: This pattern allows us to swap out the LLM configuration of the `AssistantAgent` or the execution environment of the `UserProxyAgent` with minimal impact on the other agent.

##### Negative

- **NEG-001**: **Communication Overhead**: Every action requires a conversational turn between the two agents, which can introduce latency compared to a single-agent or monolithic design.
- **NEG-002**: **Increased Complexity for Simple Tasks**: For very simple tasks that don't require external tools, the two-agent setup can be more complex than necessary.
- **NEG-003**: **Potential for Misalignment**: If the tool schemas provided to the `AssistantAgent` do not perfectly match the functions registered with the `UserProxyAgent`, it can lead to runtime errors.

#### Alternatives Considered

##### Single-Agent Architecture

- **ALT-001**: **Description**: A single `AssistantAgent` that has the ability to both plan and execute code.
- **ALT-002**: **Rejection Reason**: This approach would tightly couple the LLM's planning logic with the code execution environment, making it harder to secure and maintain. It also violates the principle of least privilege, as the LLM-connected agent would have direct access to the execution environment.

##### Multi-Agent Group Chat

- **ALT-003**: **Description**: A more complex architecture involving a `GroupChat` with multiple specialized agents (e.g., a planner, a coder, a validator).
- **ALT-004**: **Rejection Reason**: While powerful for complex, multi-step tasks, a `GroupChat` is overly complex for the current project scope, which is focused on a single, well-defined tool execution task. The two-agent architecture provides a simpler and more direct solution.

#### Implementation Notes

- **IMP-001**: The `LinterAgent` is instantiated from `autogen.AssistantAgent` and is provided with the LLM configuration and tool schemas.
- **IMP-002**: The `Executor` is instantiated from `autogen.UserProxyAgent` with `human_input_mode` set to `"NEVER"` and is responsible for registering and executing the actual Python functions.
- **IMP-003**: The interaction is initiated by the `UserProxyAgent` calling the `initiate_chat` method.

#### References

- **REF-001**: ADR-0001: pyautogen Framework Adoption
- **REF-002**: [AutoGen Agents Documentation](https://microsoft.github.io/autogen/docs/core-concepts/agents)
