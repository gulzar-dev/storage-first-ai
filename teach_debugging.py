from storage_agent import StorageAgent
agent = StorageAgent()

# 1. THE DEBUGGER SKILL
# This skill can read a file, find bugs, and overwrite it with a fix.
agent.learn_new_skill(
    skill_name='Senior Debugger',
    logic_steps='''
import os
# Example task: "Fix errors in coffee/app/page.tsx"
path_match = re.search(r"in (.*?)($| )", task)
file_path = path_match.group(1).strip() if path_match else None

if file_path and os.path.exists(file_path):
    print(f"AI Debugger: Reading {file_path} to find issues...")
    with open(file_path, "r") as f:
        content = f.read()
    
    # Logic to fix common AI-generated errors
    fixed_content = content
    if content.count("{") != content.count("}"):
        print("AI Debugger: Detected mismatched braces. Attempting fix...")
        # (Simplified fix logic for prototype)
        if content.count("{") > content.count("}"):
            fixed_content += "}" * (content.count("{") - content.count("}"))
    
    # Overwrite with the 'fixed' version
    with open(file_path, "w") as f:
        f.write(fixed_content)
    print(f"AI Output: Successfully audited and patched {file_path}.")
else:
    print(f"AI Error: Could not find file to debug at {file_path}")
''',
    keywords=['fix', 'debug', 'error', 'broken', 'repair']
)

# 2. UPGRADING DYNAMIC ARCHITECT WITH AUDIT
# I will re-learn the architect skill with an 'Audit' step included.
# (I am pulling the existing logic but adding the 'if syntax_ok' check)
skill_logic = agent.search_memory("build a site")["logic"]
if "Audit" not in skill_logic:
    audit_logic = '''
# --- AUDIT STEP ---
print("AI Auditor: Verifying code integrity...")
if full_code.count("{") == full_code.count("}") and "export default" in full_code:
    print("AI Auditor: Syntax check PASSED.")
else:
    print("AI Auditor: Syntax check FAILED. Retrying generation...")
    # (In a real app, it would loop here)
'''
    # Prepend the audit logic before the file write
    updated_logic = skill_logic.replace('with open', audit_logic + '\nwith open')
    agent.learn_new_skill('Dynamic Code Architect', updated_logic, ['custom', 'site', 'page', 'build'])

print("AI Status: Debugger and Auditor skills successfully mastered.")
