# System Overview – LawAI

## Purpose

LawAI is an AI-powered legal awareness system designed to help Indian citizens understand applicable labour laws in simple, human-friendly language.  
The system focuses strictly on legal awareness and education, not legal advice or outcome prediction.

---

## Design Philosophy

LawAI is built on three core principles:

1. **Authoritative Grounding**  
   The AI is never treated as a source of legal truth. All legal correctness comes from curated, structured data derived from official sources such as India Code.

2. **Schema-Governed Knowledge**  
   Legal information is stored as validated legal concepts rather than raw law text. Every concept must conform to a master JSON schema before it can be used.

3. **Controlled AI Reasoning**  
   The AI is restricted to explaining only the legal data provided to it. If required information is missing, the system enforces refusal instead of guessing.

---

## High-Level Architecture

The system follows a controlled Retrieval-Augmented Generation (RAG) flow:

User Query  
→ Intent & Semantic Understanding  
→ Legal Concept Retrieval  
→ Grounded AI Explanation  
→ Structured, Cited Response

At no point does the AI operate without verified legal context.

---

## Core Components

### 1. User Interface
Accepts free-form legal questions written in natural language, including informal language and spelling mistakes.

### 2. Intent Analyzer
Uses semantic understanding to map user queries to the most relevant legal concept without relying on fixed questions or keywords.

### 3. Legal Knowledge Store
Contains structured legal concepts validated against a master JSON schema. Each concept references applicable Acts, sections, and official authority.

### 4. Retrieval Layer
Selects the most relevant legal concept(s) based on semantic similarity and passes only that data to the AI.

### 5. AI Explanation Layer
Generates clear explanations, rights, and next steps using only the retrieved legal data and enforced safety rules.

### 6. Safety & Boundary Enforcement
Ensures mandatory disclaimers, blocks legal advice, prevents hallucination, and enforces refusal when information is unavailable.

---

## What LawAI Is Not

- LawAI is not a lawyer or legal advisor  
- LawAI does not predict legal outcomes  
- LawAI does not replace professional legal consultation  

---

## Outcome

By combining authoritative data, schema validation, and controlled AI reasoning, LawAI provides safe, explainable, and trustworthy legal awareness for real-world use.
