# Intent Resolution – LawAI

## Purpose

This document explains how LawAI interprets free-form user queries and maps them to the correct legal concepts.  
The goal is to allow users to ask questions naturally, without fixed formats, while maintaining correctness and safety.

---

## Design Goals

The intent resolution system is designed to:

- Accept natural language queries with spelling mistakes or informal phrasing
- Avoid keyword-based or rule-based matching
- Map queries to stable, predefined legal concepts
- Prevent incorrect or overly broad matches
- Fail safely when intent cannot be determined

---

## High-Level Approach

LawAI uses **semantic intent resolution**, not predefined questions.

Instead of matching exact words, the system compares the meaning of the user’s query with the meaning of each legal concept.

---

## Intent Resolution Flow

User Query  
→ Text Embedding  
→ Semantic Similarity Search  
→ Concept Selection  
→ Confidence Check  
→ Safe Match or Refusal

---

## Step-by-Step Logic

### 1. User Query Embedding

- The user’s input text is converted into a numerical embedding that represents its semantic meaning.
- This process captures intent even if grammar, spelling, or phrasing is imperfect.

**Example user queries:**
- “Kids working in hotel”
- “Small children doing jobs”
- “Minors working instead of school”

All of these produce semantically similar embeddings.

---

### 2. Concept Embeddings

- Each legal concept has a corresponding embedding generated from:
  - `concept_description`
  - `intent_scope`
- These embeddings represent the meaning of the legal situation the concept covers.

---

### 3. Similarity Matching

- The system compares the user query embedding against all concept embeddings within the relevant legal domain.
- A similarity score is calculated for each concept.

---

### 4. Concept Selection

- The concept with the highest similarity score is selected.
- The selected concept must exceed a predefined confidence threshold.

If no concept meets the threshold, the system refuses safely.

---

### 5. Ambiguity Handling

If multiple concepts have similar confidence scores:
- The system may request clarification from the user, or
- Select the broader, safer concept if applicable

Ambiguous matches never result in speculative answers.

---

## Domain Filtering

Before similarity matching:
- The system may infer a broad legal domain (e.g., labour, criminal, cyber)
- Only concepts within that domain are considered

This improves accuracy and performance.

---

## Failure and Refusal

LawAI enforces refusal when:
- No concept meets the confidence threshold
- The query is outside available legal domains
- The intent is unclear or ambiguous

In such cases, the system responds politely without guessing.

---

## Why This Design Is Safe

- No fixed questions are required
- No hardcoded keyword rules exist
- AI never invents legal meaning
- Every answer is tied to a validated legal concept

---

## Summary

LawAI’s intent resolution system allows flexible, human-friendly input while preserving strict legal correctness through semantic matching and controlled failure.
