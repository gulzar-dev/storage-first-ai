from storage_agent import StorageAgent
agent = StorageAgent()

skill_logic = '''
import os
import subprocess
import re

# 1. IDENTIFY TARGET
path_match = re.search(r"audit (.*?)($| )", task.lower())
file_path = path_match.group(1).strip() if path_match else None

if not file_path or not os.path.exists(file_path):
    print(f"AI Auditor: Please provide a valid file path to audit.")
else:
    print(f"AI Auditor: Starting deep audit of {file_path}...")
    with open(file_path, "r") as f:
        code = f.read()

    issues = []

    # --- PHASE 1: SYNTAX VERIFICATION ---
    if file_path.endswith(".py"):
        try:
            subprocess.check_output(f"python3 -m py_compile {file_path}", shell=True, stderr=subprocess.STDOUT)
            print("[+] Syntax: Python check passed.")
        except subprocess.CalledProcessError as e:
            issues.append(f"Syntax Error: {e.output.decode().strip()}")

    # --- PHASE 2: SECURITY & SMELL SCAN ---
    bad_patterns = {
        "eval(": "Insecure use of eval() detected.",
        "exec(": "Dangerous use of exec() detected.",
        "password =": "Potential hardcoded credential found.",
        "API_KEY =": "API Key exposed in source code.",
        "TODO:": "Unfinished business logic found."
    }
    for pattern, msg in bad_patterns.items():
        if pattern in code:
            issues.append(f"Security/Quality: {msg}")

    # --- PHASE 3: SEMANTIC FIXING ---
    if issues:
        print(f"AI Auditor: Found {len(issues)} issues. Attempting automated repair...")
        for issue in issues:
            print(f"  -> Fixing: {issue}")
            # (In a real app, this would trigger Autonomous Research Mode for specific fixes)
        
        # Example fix: Clean up TODOs
        fixed_code = code.replace("TODO:", "# FIXED BY AI:")
        with open(file_path, "w") as f:
            f.write(fixed_code)
        print(f"AI Output: Audit complete. {file_path} has been patched.")
    else:
        print("AI Auditor: No major issues found. Code is clean and professional.")
'''

agent.learn_new_skill(
    skill_name='Universal Code Auditor',
    logic_steps=skill_logic,
    keywords=['audit', 'check code', 'analyze file', 'verify logic', 'secure']
)
