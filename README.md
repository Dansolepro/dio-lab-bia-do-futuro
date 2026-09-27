# 🏥 Assistente Clínico Inteligente - CAPS

Este repositório contém a implementação de um **Agente de IA Generativa** customizado para o contexto de saúde mental pública, atuando como um assistente de suporte e triagem para o **CAPS (Centro de Atenção Psicossocial)**.

O projeto foi adaptado a partir de um desafio original da DIO, focando em um ecossistema de saúde humanizado, preditivo e seguro.

---

## 📺 Vídeo de Apresentação (Pitch)

Assista ao vídeo demonstrativo do projeto com o pitch comercial de 3 minutos e detalhes da solução:

👉 **[Assista ao Vídeo do Projeto Aqui](https://drive.google.com/file/d/1ldOryGCSQ16WjZ0-GipegFW0vuFmG1E2/view?usp=sharing)**

---

## 🎯 Objetivos do Assistente

* **Triagem Inteligente:** Analisar relatos e históricos para auxiliar na classificação de demandas e urgências.
* **Suporte à Evolução Clínica:** Facilitar o acompanhamento de prontuários, relatórios e linhas de cuidado de forma ágil.
* **Segurança e Confiabilidade:** Mitigar alucinações da IA (técnicas anti-alucinação) utilizando as diretrizes oficiais de saúde mental como base de conhecimento (RAG).

---

## 📁 Estrutura e Organização do Projeto

O repositório está organizado para separar a base de conhecimento simulada, as configurações da IA e o código funcional:

* **`data/`**: Base de dados clínicos simulados e relatórios de evolução de pacientes (Exemplo: Prontuário CAPS-9872).
* **`docs/`**: Documentação das personas do assistente, engenharia de prompts clínicos, métricas de validação e roteiro do pitch.
* **`src/`**: Código-fonte da aplicação e interface interativa desenvolvida em Python.
* **`assets/`**: Imagens, capturas de tela e diagramas de arquitetura da solução.
* **`examples/`**: Referências práticas de uso do assistente.

---

## 🛠️ Tecnologias Utilizadas

* **Python 100%**
* **IA Generativa / LLMs** (com Engenharia de Prompts voltada para Saúde)
* **Interface Gráfica:** (Streamlit / Gradio ou equivalente na pasta `src`)

---

## 🚀 Como Executar o Protótipo

1. Certifique-se de ter o Python instalado e clone este repositório.
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação contida na pasta `src/`:
   ```bash
   streamlit run src/app.py
   ```
