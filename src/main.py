# src/main.py
import logging
import os
import autogen
from pathlib import Path
from pymarkdown.api import fix_markdown_file
from dotenv import load_dotenv

# 1. Configuração Inicial
# Carrega as variáveis do arquivo .env (OAI_CONFIG_LIST)
load_dotenv()

# Configura o logging para vermos o que está acontecendo
logging.basicConfig(level=logging.INFO)

# 2. Definição da Ferramenta (Tool)
# Esta é a função Python que os agentes poderão executar.
def lint_and_fix_markdown(file_path: str) -> str:
    """
    Executa o lint e corrige automaticamente um arquivo markdown específico.
    Retorna uma string indicando sucesso ou falha.
    """
    logging.info(f"[Tool] Iniciando lint e correção para: {file_path}")

    full_path = Path(file_path).resolve()

    if not full_path.exists():
        logging.error(f"[Tool] Erro: Arquivo não encontrado em {full_path}")
        return f"Erro: Arquivo não encontrado em {file_path}"

    try:
        # A função fix_markdown_file do pymarkdown corrige o arquivo "in-place"
        fix_markdown_file(str(full_path))

        logging.info(f"[Tool] Arquivo corrigido e salvo em: {full_path}")
        return f"Sucesso: O arquivo '{file_path}' foi corrigido e salvo."

    except Exception as e:
        logging.error(f"[Tool] Erro ao corrigir o arquivo: {e}")
        return f"Erro: Não foi possível corrigir o arquivo {file_path}. Detalhe: {e}"

# 3. Função Principal (Main)
def main():
    print("Iniciando o sistema de agentes...")

    # 4. Configuração do LLM
    # Carrega a configuração do .env (OAI_CONFIG_LIST)
    config_list = autogen.config_list_from_env()

    llm_config = {
        "config_list": config_list,
        "temperature": 0.1,
    }

    # 5. Instanciando os Agentes

    # O AssistantAgent (LinterAgent)
    # Este é o agente de IA que entende o objetivo e decide usar ferramentas.
    linter_agent = autogen.AssistantAgent(
        name="LinterAgent",
        system_message="""Você é um assistente especialista em formatação de Markdown.
        Seu objetivo é corrigir arquivos .md usando a ferramenta 'lint_and_fix_markdown'.
        Não escreva o código da correção você mesmo. Apenas peça para a ferramenta ser executada no arquivo solicitado.
        Responda 'TERMINATE' quando a tarefa estiver concluída com sucesso.
        """,
        llm_config=llm_config,
    )

    # O UserProxyAgent (Executor)
    # Este agente atua como um proxy do usuário e executa o código/ferramentas.
    executor = autogen.UserProxyAgent(
        name="Executor",
        human_input_mode="NEVER",
        code_execution_config={
            # Importante: "use_docker": False significa que o código (a chamada da função)
            # será executado no ambiente local (onde o script está rodando).
            "use_docker": False,
        },
    )

    # 6. CRUCIAL: Registro da Ferramenta

    # 6a. Definição do Schema da Ferramenta (para o LLM entender)
    tool_schema = {
        "type": "function",
        "function": {
            "name": "lint_and_fix_markdown",
            "description": "Executa o lint e corrige automaticamente um arquivo markdown específico.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "O caminho do arquivo .md a ser corrigido (ex: ./input.md)",
                    }
                },
                "required": ["file_path"],
            },
        },
    }

    # 6b. "Ensinando" os agentes sobre a ferramenta

    # Damos ao LinterAgent (LLM) o schema da ferramenta
    linter_agent.llm_config["tools"] = [tool_schema]

    # Damos ao Executor (Código) a função Python real
    executor.register_function(
        function_map={
            "lint_and_fix_markdown": lint_and_fix_markdown
        }
    )

    # 7. Iniciando a Conversa
    print("Iniciando a conversa...")
    executor.initiate_chat(
        linter_agent,
        message="Por favor, corrija o lint do arquivo './input.md'.",
    )

# Executa a função principal
if __name__ == "__main__":
    main()
