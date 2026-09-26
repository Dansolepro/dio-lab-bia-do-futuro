import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
# O Ollama por padrão roda na porta 11434. Usamos o endpoint /api/chat para melhor suporte a papéis (system/user)
OLLAMA_URL = "http://localhost:11434/api/chat"
MODELO = "gpt-oss"  # Altere para o modelo que você baixou no seu Ollama (ex: llama3, mistral, gemma2)

# ============ CARREGAR DADOS ============
# 1. Carrega as diretrizes institucionais do CAPS (Catálogo de oficinas e regras)
with open('./data/diretrizes_caps_pts.json', 'r', encoding='utf-8') as f:
    diretrizes_caps = json.load(f)

# 2. Carrega o documento atual anexado do paciente (Texto Puro)
with open('./data/documento_paciente_exemplo.txt', 'r', encoding='utf-8') as f:
    documento_paciente = f.read()

# 3. Carrega o histórico de evolução de consultas anteriores (Tabela)
historico = pd.read_csv('./data/historico_consultas.csv', encoding='utf-8')

# ============ MONTAR CONTEXTO DO PACIENTE ============
# Estrutura os dados dinâmicos do caso atual e o histórico para enviar à LLM
contexto_clinico = f"""
[DOCUMENTO ANEXADO DO CASO ATUAL]
{documento_paciente}

[HISTÓRICO DE EVOLUÇÕES E CONSULTAS ANTERIORES NO CAPS]
{historico.to_string(index=False)}

[DIRETRIZES DA INSTITUIÇÃO E OFICINAS DISPONÍVEIS]
{json.dumps(diretrizes_caps, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT CLÍNICO ============
SYSTEM_PROMPT = """Você é um Assistente Clínico especializado no ecossistema de saúde mental pública do SUS, especificamente focado em Centros de Atenção Psicossocial (Caps). Seu objetivo principal é analisar documentos clínicos (relatórios, evoluções e prontuários) e propor uma minuta estruturada de Projeto Terapêutico Singular (PTS), integrando o histórico do paciente às diretrizes institucionais fornecidas.

DIRETRIZES DE COMPORTAMENTO:
1. Atue como um consultor técnico multiprofissional (médico, psicológico e social). Seu tom deve ser técnico-clínico, empático, ético e puramente objetivo.
2. Nunca tome decisões de forma autônoma. Lembre o profissional de que suas respostas são propostas que exigem validação da equipe do Caps.
3. Não crie diagnósticos (CIDs) novos; utilize apenas os que já foram descritos pelos profissionais nos documentos fornecidos.

REGRAS ESTRITAS DE SEGURANÇA E ANTI-ALUCINAÇÃO:
1. Baseie-se exclusivamente nos arquivos fornecidos (JSON de Diretrizes, CSV de Histórico e Documento Anexado). Nunca invente informações clínicas.
2. É terminantemente proibido prescrever medicamentos, sugerir alterações de dosagem ou indicar tratamentos farmacológicos por conta própria. Se o documento do médico já trouxer uma conduta de medicação, você deve apenas replicá-la textualmente na seção correspondente para fins de centralização.
3. Se identificar sinais graves de alerta (como ideação suicida ativa, automutilação ou agressividade severa), você deve classificar o plano no Regime Intensivo e adicionar uma nota de urgência em destaque no topo da resposta.
4. Se faltarem informações essenciais (ex: rede de apoio, histórico familiar ou rotina), aponte essa lacuna explicitamente e recomende que a equipe colha esses dados.
5. Identifique a intenção do usuário: Se ele fizer uma pergunta direta sobre um dado específico (ex: "Quantas faltas?", "Qual a medicação?"), responda de forma curta, direta e objetiva, ignorando a estrutura de 5 etapas.

DIRETRIZ DE FORMATAÇÃO DA RESPOSTA:
- Para solicitações de "criar PTS", "mudar plano", "estruturar tratamento" ou "analisar caso completo": Siga RIGOROSAMENTE as 5 etapas abaixo (Aviso, Síntese, Regime, Oficinas, Medicamentos e Lacunas).
- Para dúvidas pontuais e perguntas simples: Responda diretamente em apenas 1 ou 2 parágrafos, mantendo sempre o aviso de segurança humana se envolver conduta clínica.

ESTRUTURA OBRIGATÓRIA DA RESPOSTA (Minuta de PTS):
Sua resposta final deve seguir rigorosamente a estrutura abaixo:
### [AVISO OBRIGATÓRIO DE REVISÃO CLÍNICA HUMANA]
### 1. Síntese do Caso Atual
### 2. Regime de Atendimento Recomendado (Justificado com base nas Diretrizes)
### 3. Plano de Atividades Socioterapêuticas (Oficinas recomendadas e o porquê)
### 4. Acompanhamento Clínico e Medicamentoso (Replicar estritamente o que o médico determinou)
### 5. Lacunas de Informação / Próximos Passos recomendados para a equipe"""

# ============ CHAMAR OLLAMA (API DE CHAT) ============
def gerar_minuta_pts(comando_usuario):
    payload = {
        "model": MODELO,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"CONTEXTO DO PACIENTE:\n{contexto_clinico}\n\nCOMANDO DO PROFISSIONAL:\n{comando_usuario}"}
        ],
        "stream": False
    }
    
    try:
        r = requests.post(OLLAMA_URL, json=payload)
        r.raise_for_status()
        return r.json()['message']['content']
    except Exception as e:
        return f"Erro ao conectar com o Ollama local: {e}. Certifique-se de que o Ollama está rodando (`ollama run {MODELO}`) e a porta 11434 está acessível."

# ============ INTERFACE STREAMLIT ============
# Movido para o topo idealmente, mas configurado corretamente aqui:
st.set_page_config(page_title="Assistente CAPS - PTS", layout="centered")

st.title("🏥 Assistente Clínico CAPS")
st.subheader("Suporte à Elaboração de Projeto Terapêutico Singular (PTS)")

st.info("💡 Os dados de diretrizes, histórico e o relatório atual foram carregados com sucesso a partir da pasta `/data` de forma 100% local.")

# 1. Inicializa o histórico de mensagens na sessão para evitar erros de renderização
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# 2. Mostra as mensagens anteriores que já estão salvas
for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

# 3. Captura o novo comando do usuário
if pergunta := st.chat_input("Ex: 'Estruture o plano de tratamento inicial' ou 'Gere o PTS com base no arquivo'"):
    
    # Adiciona e exibe a mensagem do usuário imediatamente
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    st.chat_message("user").write(pergunta)
    
    # Gera a resposta com o spinner controlado
    with st.spinner("Analisando prontuários e gerando minuta de PTS localmente..."):
        resposta_agente = gerar_minuta_pts(pergunta)
        
    # Adiciona e exibe a resposta do assistente
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_agente})
    st.chat_message("assistant").write(resposta_agente)

