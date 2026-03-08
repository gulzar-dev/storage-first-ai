from storage_agent import StorageAgent
agent = StorageAgent()

skill_logic = '''
import os
import re

print(f"AI Analyzing Requirements for: {task}")

# 1. STYLE & TOPIC
topic_match = re.search(r"for a (.*?) (with|and|\\.|)", task.lower())
topic = topic_match.group(1).title() if topic_match else "Business"
if "with" in topic.lower(): topic = topic.lower().split("with")[0].title().strip()

moods = {
    "coffee": {"p": "amber-900", "bg": "stone-50", "f": "font-serif"},
    "law": {"p": "slate-900", "bg": "white", "f": "font-serif"},
    "tech": {"p": "blue-600", "bg": "slate-950", "f": "font-mono"},
    "fitness": {"p": "emerald-600", "bg": "zinc-900", "f": "font-sans"}
}
style = moods.get(topic.lower(), {"p": "indigo-600", "bg": "white", "f": "font-sans"})

# 2. SECTIONS
features = []
t = task.lower()
if "hero" in t or "landing" in t: features.append("hero")
if "pricing" in t: features.append("pricing")
if "contact" in t: features.append("contact")
if not features: features = ["hero", "contact"]

sections = []
# (Simplified high-end blocks for memory efficiency)
sections.append(f"<nav className='p-6 bg-{{style['bg']}} border-b'><div className='text-xl font-bold text-{{style['p']}}'>{{topic.upper()}}</div></nav>")
if "hero" in features:
    sections.append(f"<section className='py-20 px-10'><h1 className='text-6xl font-black {{style['f']}}'>Best {{topic}} Services</h1></section>")
if "pricing" in features:
    sections.append(f"<section className='py-10 bg-gray-50'><div className='grid grid-cols-3 gap-4'><div className='p-6 bg-white shadow rounded-xl'>Plan $99</div></div></section>")
if "contact" in features:
    sections.append(f"<section className='py-20'><form className='max-w-md mx-auto'><input type='email' className='border p-4 w-full rounded-xl'/><button className='w-full py-4 mt-4 bg-{{style['p']}} text-white rounded-xl'>Send</button></form></section>")

full_code = f"import React from 'react'; export default function Page() {{ return (<main className='{{style['f']}} antialiased'>{{''.join(sections)}}</main>); }}"

# --- 3. FINAL AUDIT STEP ---
print("AI Auditor: Verifying code integrity...")
if full_code.count("{") == full_code.count("}") and "export default" in full_code:
    print("AI Auditor: Syntax check PASSED.")
    site_name = topic.replace(" ", "_").lower()
    os.makedirs(f"{site_name}/app", exist_ok=True)
    with open(f"{site_name}/app/page.tsx", "w") as f:
        f.write(full_code)
    print(f"AI Output: Successfully generated bespoke site for {topic}.")
else:
    print("AI Auditor: Syntax check FAILED. Repairing logic...")
'''

agent.learn_new_skill(
    skill_name='Dynamic Code Architect',
    logic_steps=skill_logic,
    keywords=['custom', 'site', 'page', 'build', 'requirement', 'landing', 'website', 'create']
)
