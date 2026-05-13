import os
import json

SCAN_DIR = "./cdk.out"

results = {
    "status": "PASS",
    "issues": []
}

# Example scan rules
dangerous_keywords = [
    "0.0.0.0/0",
    "AWS::IAM::Policy",
    "AdministratorAccess"
]

for root, dirs, files in os.walk(SCAN_DIR):
    for file in files:

        if file.endswith(".json") or file.endswith(".template.json"):

            path = os.path.join(root, file)

            with open(path, "r") as f:
                content = f.read()

                for keyword in dangerous_keywords:

                    if keyword in content:
                        results["status"] = "FAIL"

                        results["issues"].append({
                            "file": path,
                            "issue": f"Found dangerous keyword: {keyword}"
                        })

# Save output
with open("scan_report.json", "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps(results, indent=2))

# Fail workflow if dangerous issues found
exit(0)
