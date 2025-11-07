---
title: "ADR-0004: Environment Configuration with .env"
status: "Accepted"
date: "2024-07-22"
authors: "Jules"
tags: ["architecture", "configuration", "security"]
supersedes: ""
superseded_by: ""
---

#### Status

Accepted

#### Context

The application requires the use of sensitive information, such as API keys for LLM providers. Hardcoding these secrets directly into the source code is a significant security risk and makes it difficult to manage different configurations for development, testing, and production environments. We need a secure and flexible way to manage these configuration variables.

#### Decision

We have decided to use a `.env` file to store environment variables, including the `OAI_CONFIG_LIST` which contains the API keys. The `python-dotenv` library is used to load these variables into the application's environment at runtime. The `.env` file is included in the `.gitignore` file to prevent it from being committed to version control.

#### Consequences

##### Positive

- **POS-001**: **Improved Security**: Keeping secrets out of the codebase prevents them from being exposed in the version control history.
- **POS-002**: **Configuration Flexibility**: Developers can easily create their own `.env` file with different API keys or model configurations without modifying the source code.
- **POS-003**: **Ease of Use**: The `python-dotenv` library provides a simple and straightforward way to load environment variables, requiring minimal boilerplate code.

##### Negative

- **NEG-001**: **Runtime Dependency**: The application's configuration is not self-contained and depends on the presence of a correctly formatted `.env` file at runtime.
- **NEG-002**: **Risk of Misconfiguration**: An incorrectly formatted `.env` file can lead to runtime errors that may not be immediately obvious.
- **NEG-003**: **Manual Setup**: Each developer needs to manually create and populate their own `.env` file, which can be a small barrier to entry for new contributors.

#### Alternatives Considered

##### Hardcoded Configuration

- **ALT-001**: **Description**: Placing the API keys and other configuration directly in the `src/main.py` file.
- **ALT-002**: **Rejection Reason**: This is a major security vulnerability and is considered bad practice. It would also make it impossible to change configurations without editing the code.

##### System-Level Environment Variables

- **ALT-003**: **Description**: Requiring developers to set system-level environment variables (e.g., using `export` in their shell profile).
- **ALT-004**: **Rejection Reason**: This approach is less portable and can be cumbersome to manage, especially when working on multiple projects with conflicting environment variable names. A project-specific `.env` file provides better isolation.

##### Dedicated Configuration Management Service

- **ALT-005**: **Description**: Using a service like HashiCorp Vault or AWS Secrets Manager to manage secrets.
- **ALT-006**: **Rejection Reason**: These services are powerful but introduce significant operational overhead and are overly complex for the current needs of this project.

#### Implementation Notes

- **IMP-001**: The `python-dotenv` library is listed as a project dependency.
- **IMP-002**: The `load_dotenv()` function is called at the beginning of `src/main.py` to load the environment variables.
- **IMP-003**: The `.env` file is explicitly listed in the `.gitignore` file.

#### References

- **REF-001**: [python-dotenv PyPI page](https://pypi.org/project/python-dotenv/)
- **REF-002**: [The Twelve-Factor App: Config](https://12factor.net/config)
