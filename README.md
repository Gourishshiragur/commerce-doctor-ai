# 🧠 CommerceDoctor AI  
### Agentic Data Quality & Auto-Repair Platform (Databricks + AI)

---

## 🚀 Overview

CommerceDoctor AI is an **agentic data platform** that combines **AI (LLM)** with **Data Engineering pipelines** to detect, analyze, and fix data quality issues.

The system integrates:
- Databricks (PySpark) for scalable data processing  
- Ollama (LLM) for intelligent reasoning  
- Streamlit for interactive UI  

---

## 🔥 Key Features

- AI-powered data issue detection  
- Automatic fix suggestions  
- AI-generated PySpark code  
- Bronze → Silver → Gold pipeline  
- Audit & monitoring framework  
- Replay (failure recovery) mechanism  
- Agent-based auto-fix workflow  
- Interactive UI (Streamlit)  

---

## 🧠 Architecture


User (Streamlit UI)
↓
AI Agent (Ollama - Analysis + Code Generation)
↓
Decision Layer (Safe Execution)
↓
Databricks Pipeline (Bronze → Silver → Gold)
↓
Audit + Replay + Monitoring


---

## 🧠 AI Design (Important)

- LLM is used for:
  - Data analysis  
  - Fix suggestions  
  - Code generation  

- Execution layer:
  - Fully deterministic (PySpark)
  - Ensures reliability and safety  

---

## 🏗️ Data Pipeline

### Bronze Layer
- Raw data ingestion  

### Silver Layer
- Data cleaning  
- Null handling  
- Deduplication  
- Invalid value filtering  

### Gold Layer
- Business KPIs  
- Aggregations (Revenue, Orders)  

---

## 📊 Audit & Monitoring

Each pipeline run logs:
- pipeline_name  
- run_id  
- status (SUCCESS / FAILED)  
- records_processed  
- error_message  
- run_timestamp  

---

## 🔁 Replay & Failure Recovery

Failed runs are identified and reprocessed:

```python
failed_runs = audit_df.filter("status = 'FAILED'")

Benefits:

Avoid full pipeline reruns
Faster recovery
Production reliability
🤖 Agent Workflow

Analyze → Plan → Generate Code → Apply Fix → Log

🌐 UI Features
Upload dataset
Run AI analysis
Generate PySpark fix code
Auto-fix via AI agent
View cleaned data
KPI dashboard
▶️ How to Run
1. Start Ollama
ollama serve
2. Run Streamlit UI
python -m streamlit run ui/app.py
📦 Requirements
streamlit
pandas
requests

🧑‍💻 Tech Stack
Python
PySpark
Databricks
Delta Lake
Streamlit
Ollama (LLM)
🚀 Future Enhancements
Streaming pipeline (Kafka)
CDC ingestion
Data quality scoring
Schema evolution detection
👨‍💻 Author

Gourish Shiragur
Data Engineer (Azure • Databricks • PySpark)

LinkedIn: https://www.linkedin.com/in/gourishankar-shiragur/

GitHub: https://github.com/Gourishshiragur/commerce-doctor-ai