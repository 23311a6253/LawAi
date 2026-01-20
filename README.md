# LawAI

LawAI is a schema-driven, AI-powered legal awareness system designed to help Indian citizens understand applicable laws in simple, human-friendly language using verified, authoritative legal data.

This project focuses on **legal awareness and education**, not legal advice.

---

## Problem Statement

Legal information in India is complex, fragmented, and written primarily for legal professionals.  
Most citizens struggle to understand which laws apply to real-life issues such as unpaid wages, child labour, or exploitation of contract workers.

General-purpose AI chatbots are unsafe in legal contexts because they may:
- Hallucinate laws or sections
- Provide incorrect legal advice
- Fail to cite authoritative sources
- Create false confidence for users

---

## Solution Overview

LawAI addresses these problems by combining structured legal data with controlled AI reasoning.

Key principles:
- Legal knowledge is stored as **validated legal concepts**, not raw text
- AI is used only to **explain**, never to decide or invent
- Every response is grounded in **official Indian law sources**
- Safety, refusal, and disclaimers are enforced by design

---

## System Architecture

LawAI follows a controlled Retrieval-Augmented Generation (RAG) architecture:

User Query  
→ Intent Resolution  
→ Legal Concept Retrieval  
→ Grounded AI Explanation  
→ Structured, Cited Response  

The AI is never treated as a source of legal truth.  
All legal correctness comes from curated data.

---

## Legal Data Design

Legal knowledge is stored as structured **Legal Concepts**, each representing a real-world legal situation.

Each concept includes:
- Clear description of the legal issue
- Applicable Acts and authority (India Code)
- Citizen rights
- Recommended awareness steps
- Explicit AI safety boundaries

All concepts are validated using a **master JSON schema** before ingestion, ensuring consistency and correctness.

---

## Safety and Responsible AI

LawAI is designed for a high-risk domain and enforces strict safety rules:

- Legal awareness only (no legal advice)
- Mandatory citation of Acts and authority
- Mandatory legal disclaimer in every response
- Safe refusal when information is unavailable or out of scope
- No prediction of legal outcomes

Hallucination prevention is achieved through **architecture**, not trust in the AI model.

---

## Technology Stack

- **Python** – Backend implementation
- **FastAPI** – API layer
- **JSON Schema** – Legal data validation
- **Vector-based semantic retrieval** – Intent resolution
- **Large Language Model** – Controlled explanation layer
- **India Code** – Authoritative legal reference source

---

## Example Use Case

**User Query:**  
“Kids are working in a hotel near my house”

**LawAI Response:**  
- Explains child labour prohibition in simple language  
- Mentions the *Child Labour (Prohibition and Regulation) Amendment Act, 2016*  
- Cites *India Code – Government of India* as the authority  
- Lists citizen rights and reporting options  
- Includes a legal awareness disclaimer  

---

## Evaluation and Testing

LawAI includes documented test cases covering:
- Valid legal awareness queries
- Ambiguous inputs
- Out-of-scope questions
- Unsafe requests (legal advice, outcome prediction)

This ensures predictable and safe system behavior.

---

## Current Scope and Limitations

- Currently implemented for selected **Labour Law** concepts
- Does not replace professional legal consultation
- No legal advice or case-specific guidance is provided

---

## Future Work

- Expand to additional legal domains (Criminal, Cyber, Consumer Law)
- Add multilingual and voice-first interfaces
- Implement automated law update pipelines
- Integrate full AI inference with strict controls

---

## Disclaimer

LawAI is an educational legal awareness system.  
It does not provide legal advice and should not be used as a substitute for consulting qualified legal professionals.

---

## License

This project is released under the MIT License.
