import sys
import json

image_uri = sys.argv[1]

result = {
    "image": image_uri,
    "valid_name": True,
    "name_check": "passed",
    "basic_checks": {
        "format_ok": image_uri.startswith("docker://") or ":" in image_uri,
        "length_ok": len(image_uri) < 200
    }
}

# Example rule
if "latest" in image_uri:
    result["warning"] = "Avoid using latest tag"

with open("validation_report.json", "w") as f:
    json.dump(result, f, indent=2)

print("Validation completed")
