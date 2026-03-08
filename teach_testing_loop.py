from storage_agent import StorageAgent
import os

agent = StorageAgent()

# CORRECTED: Passing the agent instance correctly into the exec context
verify_logic = '''
import subprocess
import os

print(f"AI Builder: Building and Verifying {task}...")

# Step 1: Build (Simulated)
with open("test_app.py", "w") as f:
    f.write("print(x) # Intentional Error")

# Step 2: Run Test
print("AI Builder: Running automated test...")
try:
    result = subprocess.check_output("python3 test_app.py", shell=True, stderr=subprocess.STDOUT, text=True)
    print(f"AI Output: Test PASSED! Output: {result.strip()}")
except subprocess.CalledProcessError as e:
    err = e.output.strip()
    print(f"AI Builder: Test FAILED! Error detected: {err}")
    
    # Step 3: Trigger Healer automatically!
    # We use 'agent' because we will inject it into the local_context
    print("AI Builder: Triggering Autonomous Healer...")
    agent.execute_task(f"Heal error: '{err}'")
    
    # Step 4: Re-verify
    print("AI Builder: Re-running test after healing...")
    os.system("python3 test_app.py")
'''

agent.learn_new_skill("Build and Verify", verify_logic, ["build and test", "verify", "run loop"])
