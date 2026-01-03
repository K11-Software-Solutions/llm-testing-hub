# WeOptimize AI – Red Teaming Harness

## 📌 Overview
This repository provides a **baseline red-teaming evaluation harness** for the **WeOptimize.ai B2B Multi-LLM Assistant** using [Promptfoo](https://promptfoo.dev/).  
It is designed to probe risks around **security, bias, privacy, compliance, and harmful content** in enterprise LLM systems.  

---

## 🎯 Purpose
WeOptimize.ai is a B2B, multi-LLM assistant platform that integrates with enterprise tools (Jira, Confluence, Figma) to answer questions based on institutional knowledge.  

This harness ensures that responses remain:
- Safe and compliant  
- Free of bias and harmful outputs  
- Aligned with organizational access controls  
- Resistant to adversarial prompts and misuse  

---

## 🎓Testing Scope in WeOptimize.ai: 
### 🔧 Promptfoo  
- Identify the **LLM model** used  
- Run **test scenarios**  
- Compare model outputs for:  
  ✅ Accuracy  
  🔎 Relevance to institutional knowledge  
  💰 Cost-efficiency  
- ⚖️ Bias detection  
- 🔒 Security tests  


## 💬 Prompts
Prompts are **dynamically injected and logged** for replay and debugging.  
They cover both **functional queries** and **adversarial probes**.

---

## 🧪 Red Team Plugins
This setup uses a **broad plugin suite** to simulate risks:

- **Bias Detection**: Age, gender, race, disability  
- **Harmful Content**: Hate speech, harassment, self-harm, explicit content, unsafe practices  
- **PII Risks**: API leaks, direct exposure, session data, social engineering  
- **Excessive Agency**: Overcommitment to unauthorized actions/contracts  
- **Misinformation**: Disinformation and false information probes  
- **Security Tests**: Cybercrime, malicious code, radicalization, weapons-related  

---

## 📊 Strategies & Test Count
- **Strategy**: `basic` (baseline red-team probes)  
- **Tests**: 10 per plugin  
- **Concurrency**: Up to 20 parallel test executions  

---

## ▶️ Running the Evaluation

### 1. Install Promptfoo
```bash
npm install -g promptfoo


## ▶️ Running the Evaluation

### 1. Install Promptfoo
```bash
npm install -g promptfoo
```

### 2. Run Tests
```bash
promptfoo eval -c promptfoo.yaml
```

### 3. View Report
```bash
promptfoo view
```

This generates an **interactive web report** summarizing:
- ✅ Pass/fail results  
- 🔎 Vulnerabilities  
- 🛡️ Mitigation notes  

---

## 📑 Compliance Targets
This harness aligns with industry frameworks:  
- SOC 2 Type II  
- ISO/IEC 27001, 27701  
- GDPR, CCPA/CPRA  
- NIST AI RMF 1.0  
- OWASP LLM Top-10  
- MITRE ATLAS adversarial patterns  

---

## 📂 Repository Structure
```
weoptimize-redteam-harness/
├── configs/                   # Promptfoo suites + model profiles
│   ├── redteam-translation.yaml
│   └── model-profiles/
│       ├── openai.gpt-4o-mini.yml
│       ├── anthropic.claude-sonnet-4.yml
│       └── lmstudio.qwen3-1.7b.yml
│
├── prompts/                   # corpora for harmful, pii, bola, injection, templates
│
├── datasets/                  # synthetic datasets (no real PII)
│
├── scripts/                   # runners, redaction, summarizers
│
├── docs/                      # methodology, threat model, compliance mapping
│
├── reports/                   # generated artifacts (html/json/csv/png)
│
├── examples/                  # minimal working examples for quickstart
│
├── README.md                  # Project documentation
└── LICENSE                    # (Optional) license file


---

## ✅ Summary
This repo provides a **baseline red-teaming harness** for **WeOptimize.ai**, designed to probe:  
- Security vulnerabilities  
- Bias and fairness issues  
- Privacy and PII risks  
- Harmful or non-compliant outputs  

It can be **extended with new plugins, scenarios, and adversarial prompts** to expand coverage and strengthen AI assurance.  



