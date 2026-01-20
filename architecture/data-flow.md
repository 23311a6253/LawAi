# Data Flow – LawAI

## Overview

This document describes how data flows through the LawAI system from the moment a user submits a query to the final response.  
The design ensures correctness, safety, and traceability at every stage.

---

## High-Level Flow

User Query  
→ Input Processing  
→ Intent Resolution  
→ Legal Concept Retrieval  
→ AI Explanation  
→ Response Assembly  

Each stage has clearly defined responsibilities and safety controls.

---

## Step-by-Step Data Flow

### 1. User Input

- The user submits a free-form legal question.
- Input may contain spelling mistakes, informal language, or mixed phrasing.
- No predefined questions or dropdowns are required.

**Example:**  
“Kids are working in a hotel near my house”

---

### 2. Input Processing

- The raw input is normalized (basic cleanup if required).
- No legal interpretation happens at this stage.
- The input is passed as-is to the intent resolution layer.

---

### 3. Intent Resolution

- Semantic understanding is used to identify the closest matching legal concept.
- Matching is based on meaning, not keywords.
- The system maps the query to a stable `concept_id`.

**Example mapping:**  
User input → `child_labour_prohibition`

If no suitable concept is found, the system triggers a safe refusal.

---

### 4. Legal Concept Retrieval

- The system loads the relevant legal concept from the knowledge store.
- All legal concepts are pre-validated using the master JSON schema.
- Only the retrieved concept data is passed forward.

At this stage:
- No external law sources are queried
- No raw law text is introduced
- No assumptions are made

---

### 5. AI Explanation Layer

- The AI receives:
  - The user’s original question
  - The retrieved legal concept data
- The AI is strictly instructed to:
  - Use only the provided legal data
  - Cite the applicable Act and authority
  - Follow all safety boundaries
  - Refuse if information is missing

The AI acts as an **explainer**, not a decision-maker.

---

### 6. Response Assembly

The final response is structured into:
- Simple explanation
- Applicable law and authority
- User rights
- Recommended next steps
- Mandatory disclaimer

This structure ensures clarity and trust.

---

## Error Handling and Refusal

LawAI enforces refusal in the following cases:
- No matching legal concept is found
- The user requests legal advice or outcome prediction
- Required legal information is missing from verified data

In such cases, the system responds safely instead of guessing.

---

## Key Design Guarantees

- AI never invents laws or sections
- All legal references are verifiable
- Every response is traceable to a validated concept
- Safety rules are enforced programmatically

---

## Summary

This controlled data flow ensures that LawAI delivers accurate, explainable, and responsible legal awareness while preventing hallucination and misuse.
