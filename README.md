# 🏥 Assistente Clínico Inteligente - CAPS

Este repositório contém a implementação de um **Agente de IA Generativa** customizado para o contexto de saúde mental pública, atuando como um assistente de suporte e triagem para o **CAPS (Centro de Atenção Psicossocial)**.

O projeto foi adaptado a partir do desafio original da DIO para focar em um ecossistema de saúde humanizado, preditivo e seguro.

---

## 🎯 Objetivos do Assistente

* **Triagem Inteligente:** Analisar relatos e históricos para auxiliar na classificação de demandas.
* **Suporte à Evolução Clínica:** Facilitar o acompanhamento de prontuários e linhas de cuidado de forma ágil.
* **Segurança e Confiabilidade:** Mitigar alucinações da IA utilizando as diretrizes oficiais de saúde mental como base de conhecimento.

---

## 📁 Organização do Projeto

* **`data/`**: Base de dados clínicos simulados e relatórios de evolução de pacientes (ex: CAPS-9872).
* **`docs/`**: Documentação das personas, engenharia de prompts clínicos e métricas de validação.
* **`src/`**: Código-fonte da aplicação e interface interativa desenvolvida em Python.

---

## 🚀 Como Executar

1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute a aplicação (interface Streamlit/Gradio):
   ```bash
   streamlit run src/app.py
   ```
