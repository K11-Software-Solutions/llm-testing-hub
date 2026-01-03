# WeOptimize AI – Baseline Red Teaming Evaluation

This repository contains a **Promptfoo-based red-teaming evaluation** for the **WeOptimize AI B2B Multi-LLM Assistant**.  
The goal is to systematically test model safety, robustness, and compliance against industry frameworks.

---

## 📌 Project Description
**Application Under Test:**  
WeOptimize.ai is a B2B, multi-LLM assistant platform that runs on employees’ devices and connects to enterprise tools like **Jira, Confluence, and Figma** to answer questions.

### Key Features
- **Single source of truth**: Aggregates enterprise knowledge (Confluence, Jira, Figma).  
- **Citations, not guesses**: Every answer is linked back to the exact doc/section.  
- **Always fresh**: Incremental syncs keep indexes updated.  
- **Smart recall**: Embeddings + chunking to reduce hallucinations.  
- **Access-aware**: RBAC/SSO enforced.  
- **Optional hygiene**: PII redaction, duplicate detection, stale link fixing.  

### Industry Domain
- **B2B SaaS – Enterprise AI**  
- Subdomain: **Knowledge Management / RAG**  

---

## ⚖️ System Rules & Constraints
- **Identity**: Speaks only as WeOptimize.ai (1st person).  
- **No leakage**: Refuses system/prompt disclosure.  
- **Safety**: Rejects illegal, harmful, or personal-data harvesting content.  
- **Data privacy**: Access restricted to authorized org sources only.  
- **RAG behavior**: Requires citations and ignores in-doc override attempts.  

---

## 🔐 Data Access
- **Systems**: Jira, Confluence, Figma (all read-only).  
- **Sensitive data types**:  
  - Employee PII (names, work emails, avatars)  
  - Customer-related PII (incidental in bug reports, etc.)  
  - Confidential business docs (roadmaps, design specs)  
  - Document metadata (timestamps, sprint names, project IDs)  
  - Potential secrets (API keys, tokens, credentials)  

- **Redaction rules**:  
  - Secrets flagged but not output.  
  - Snippets re-validated at runtime via RBAC.  

---

## 👤 Red-Team Persona
- **Primary tester**: Authorized internal employee account (SSO).  
- **Goal**: Probe for data exfiltration, RBAC leaks, prompt injection, and metadata exposure.  
- **Constraints**:  
  - Read-only rights.  
  - No connector installs.  
  - No ACL changes.  

---

## 🚨 Attack Scenarios
This evaluation simulates adversarial behaviors such as:  
- **Prompt injection** (hidden malicious instructions).  
- **PII leakage** via translation or social engineering.  
- **BOLA attacks** (accessing other users’ data).  
- **Bias/fairness probes** (age, race, gender, disability).  
- **Unauthorized contracts & excessive agency** (AI overcommitting).  
- **Content moderation bypass** (hate, harassment, self-harm).  
- **Illegal/unsafe content handling** (weapons, cybercrime, drugs).  

---

## ⚙️ Configuration
The `promptfoo.yaml` defines the evaluation setup.

### Example
```yaml
targets:
  - id: http
    label: weOptimize-ai-b2b-multi-LLM-assistant
    config:
      url: https://api.weoptimize.ai/chats/promptfoo
      method: POST
      headers:
        Content-Type: application/json
        x-api-key: <your-api-key>
      body: |-
        {
          "email": "user@example.com",
          "message": "{{prompt}}"
        }
      transformResponse: json.message
