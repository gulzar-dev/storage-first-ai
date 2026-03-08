import json
import os
import re
import argparse
import subprocess
import requests

class StorageAgent:
    def __init__(self, data_path="."):
        self.memory_path = os.path.join(data_path, "memory")
        self.knowledge_path = os.path.join(data_path, "knowledge")
        self.stats_path = os.path.join(self.memory_path, "agent_stats.json")
        
        for path in [self.memory_path, self.knowledge_path]:
            if not os.path.exists(path):
                os.makedirs(path)
        
        self.load_stats()

    def load_stats(self):
        if os.path.exists(self.stats_path):
            with open(self.stats_path, 'r') as f:
                self.stats = json.load(f)
        else:
            self.stats = {"balance": 100.0, "total_tasks": 0, "efficiency_score": 1.0}
            self.save_stats()

    def save_stats(self):
        with open(self.stats_path, 'w') as f:
            json.dump(self.stats, f, indent=4)

    def update_balance(self, amount, reason):
        self.stats["balance"] += amount
        color = "\033[92m+" if amount > 0 else "\033[91m"
        print(f"{color}{amount:.1f} Credits\033[0m | {reason} | Bal: {self.stats['balance']:.1f}")
        self.save_stats()

    def learn_new_skill(self, skill_name, logic_steps, keywords):
        self.update_balance(-2.0, "Writing New Skill to Disk")
        skill_data = {
            "name": skill_name, "logic": logic_steps, "keywords": keywords,
            "times_used": 0, "status": "active", "complexity": len(logic_steps)
        }
        with open(os.path.join(self.memory_path, f"{skill_name.replace(' ', '_').lower()}.json"), 'w') as f:
            json.dump(skill_data, f, indent=4)
        print(f"\033[94m[*] SUCCESS: AI has mastered '{skill_name}' on your hard drive.\033[0m")

    def search_memory(self, task):
        self.update_balance(-0.5, "Disk Search (Cheap)")
        skills = [f for f in os.listdir(self.memory_path) if f.endswith(".json") and f != "agent_stats.json"]
        memories = []
        for skill_file in skills:
            with open(os.path.join(self.memory_path, skill_file), 'r') as f:
                memories.append(json.load(f))
        
        # Sort by complexity: Higher complexity skills are tried first
        memories.sort(key=lambda x: x.get("complexity", 0), reverse=True)

        for memory in memories:
            if any(keyword.lower() in task.lower() for keyword in memory.get("keywords", [])):
                return memory
        return None

    def execute_task(self, task):
        memory = self.search_memory(task)
        if memory:
            print(f"[EXEC] Using Stored Skill: '{memory['name']}'")
            self.update_balance(-1.0, "Executing Stored Logic")
            local_context = {"task": task, "result": None} 
            try:
                # We define local_context for the exec environment
                exec(memory['logic'], globals(), {"task": task, "local_context": local_context})
                self.update_balance(5.0, "Task SUCCESS")
                return True
            except Exception as e:
                print(f"[!] Error: {e}")
                return False
        else:
            print("[FAIL] No matching skill found.")
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Full Capability Storage Agent")
    parser.add_argument("query", type=str, nargs="?", help="Task for the agent")
    args = parser.parse_args()
    agent = StorageAgent()
    if args.query:
        agent.execute_task(args.query)
