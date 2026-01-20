import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_concepts(schema_path: Path, data_path: Path):
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)

    data = load_json(data_path)

    if "concepts" not in data:
        raise ValueError("Data file must contain a top-level 'concepts' array")

    errors_found = False

    for idx, concept in enumerate(data["concepts"], start=1):
        errors = list(validator.iter_errors(concept))
        if errors:
            errors_found = True
            print(f"\n❌ Validation errors in concept #{idx} "
                  f"(concept_id={concept.get('concept_id')}):")
            for error in errors:
                print(f"  - {error.message}")

    if errors_found:
        print("\n❌ Validation failed. Fix errors before ingestion.")
        sys.exit(1)

    print("✅ Validation successful. All concepts are schema-compliant.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate.py <schema.json> <data.json>")
        sys.exit(1)

    schema_file = Path(sys.argv[1])
    data_file = Path(sys.argv[2])

    if not schema_file.exists():
        print(f"Schema file not found: {schema_file}")
        sys.exit(1)

    if not data_file.exists():
        print(f"Data file not found: {data_file}")
        sys.exit(1)

    validate_concepts(schema_file, data_file)
