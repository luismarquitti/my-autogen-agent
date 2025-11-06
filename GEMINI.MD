# 🚀 Usando Modelos Gemini com (py)AutoGen

O (py)AutoGen suporta nativamente a API do Google Gemini através da configuração `OAI_CONFIG_LIST`.

## Configuração (via `.env`)

1. **Obtenha sua Chave de API:** Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey) e gere uma chave de API.

2. **Atualize seu `.env`:**

   Este é o formato exato que o `pyautogen` espera. Use o modelo `flash` para testes e baixo custo.

   ```ini
   # .env
   OAI_CONFIG_LIST='[
     {
       "model": "gemini-1.5-flash-latest",
       "api_key": "SUA_CHAVE_API_DO_GOOGLE_AI_STUDIO_AQUI",
       "api_type": "google"
     }
   ]'
   ```

   * **`model`**: O nome do modelo.
   * **`api_key`**: Sua chave do AI Studio.
   * **`api_type`: "google"**: Essencial. Isso instrui o `pyautogen` a usar o cliente Python `google-generativeai` por baixo dos panos.

## Uso no Código

O seu script `src/main.py` já está pronto para isso. A linha:

```python
config_list = autogen.config_list_from_env()
```

Irá carregar automaticamente essa configuração do Gemini, e o `AssistantAgent` a utilizará sem qualquer alteração adicional no código.
