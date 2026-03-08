from storage_agent import StorageAgent
agent = StorageAgent()

skill_logic = '''
import os
import re

print(f"AI Analyzing Mood and UI/UX for: {task}")

# 1. TOPIC & MOOD ANALYSIS
topic_match = re.search(r"for a (.*?) (with|and|\\.|)", task.lower())
topic = topic_match.group(1).title() if topic_match else "Business"
if "with" in topic.lower(): topic = topic.lower().split("with")[0].title().strip()

# --- STYLE INTELLIGENCE ENGINE ---
moods = {
    "coffee": {"primary": "amber-900", "accent": "orange-200", "bg": "stone-50", "font": "font-serif"},
    "fitness": {"primary": "emerald-600", "accent": "lime-400", "bg": "zinc-900", "font": "font-sans"},
    "law": {"primary": "slate-900", "accent": "blue-800", "bg": "white", "font": "font-serif"},
    "tech": {"primary": "blue-600", "accent": "cyan-400", "bg": "slate-950", "font": "font-mono"},
    "freelance": {"primary": "purple-600", "accent": "pink-400", "bg": "white", "font": "font-sans"},
    "nightclub": {"primary": "fuchsia-600", "accent": "violet-900", "bg": "black", "font": "font-sans"}
}

# Default mood if no match
style = moods.get(topic.lower(), {"primary": "indigo-600", "accent": "indigo-400", "bg": "white", "font": "font-sans"})
p = style["primary"]
a = style["accent"]
bg = style["bg"]
f = style["font"]

print(f"AI Selected Palette: {p} on {bg} background using {f} typography.")

# 2. IDENTIFY SECTIONS
features = []
t = task.lower()
if "hero" in t or "landing" in t: features.append("hero")
if "about" in t: features.append("about")
if "pricing" in t: features.append("pricing")
if "contact" in t: features.append("contact")
if not features: features = ["hero", "contact"]

# 3. DYNAMIC UI CONSTRUCTION
sections = []

# Nav
sections.append(f"""
<nav className='flex justify-between items-center py-6 px-10 bg-{bg} border-b border-gray-100 sticky top-0 z-50'>
    <div className='text-2xl font-black tracking-tighter text-{p}'>{topic.upper()}</div>
    <div className='space-x-8 font-medium text-gray-500'>
        <a href='#' className='hover:text-{p} transition'>Process</a>
        <a href='#' className='hover:text-{p} transition'>Expertise</a>
    </div>
    <button className='bg-{p} text-white px-6 py-2 rounded-lg font-bold shadow-lg shadow-{p}/20'>Consult Now</button>
</nav>
""")

if "hero" in features:
    text_color = "white" if "900" in bg or "950" in bg or "black" in bg else "gray-900"
    sections.append(f"""
<section className='bg-{bg} text-{text_color} py-32 px-10'>
    <div className='max-w-5xl mx-auto'>
        <h1 className='text-7xl font-black mb-8 leading-tight {f}'>Elevate your <span className='text-{p}'>{topic}</span> experience.</h1>
        <p className='text-2xl opacity-70 mb-12 max-w-2xl'>Bespoke solutions crafted with precision logic and modern aesthetics.</p>
        <div className='flex gap-4'>
            <button className='bg-{p} text-white px-10 py-5 rounded-2xl font-bold text-xl hover:brightness-110 transition shadow-2xl shadow-{p}/40'>Get Started</button>
            <button className='border-2 border-gray-200 px-10 py-5 rounded-2xl font-bold text-xl hover:bg-gray-50 transition'>View Portfolio</button>
        </div>
    </div>
</section>
""")

if "pricing" in features:
    sections.append(f"""
<section className='py-24 bg-gray-50 px-10'>
    <div className='max-w-6xl mx-auto'>
        <h2 className='text-4xl font-black text-center mb-16 {f}'>Investment Plans</h2>
        <div className='grid grid-cols-1 md:grid-cols-3 gap-8'>
            {[f'<div className="p-8 bg-white rounded-3xl border border-gray-100 shadow-xl hover:border-{p} transition"><h3 className="font-bold text-xl mb-4">Plan {i}</h3><div className="text-4xl font-black mb-6">$ {i}99</div><button className="w-full py-3 bg-{p} text-white rounded-xl font-bold">Select</button></div>' for i in range(1,4)]}
        </div>
    </div>
</section>
""")

if "contact" in features:
    sections.append(f"""
<section className='py-24 px-10 bg-{bg}'>
    <div className='max-w-3xl mx-auto border-t border-gray-100 pt-24'>
        <h2 className='text-5xl font-black mb-8 {f}'>Let's connect.</h2>
        <form className='grid gap-6'>
            <input type='text' placeholder='Full Name' className='bg-gray-100 p-6 rounded-2xl outline-none focus:ring-4 focus:ring-{p}/10 border-none' />
            <input type='email' placeholder='Email' className='bg-gray-100 p-6 rounded-2xl outline-none focus:ring-4 focus:ring-{p}/10 border-none' />
            <textarea placeholder='Message' rows='4' className='bg-gray-100 p-6 rounded-2xl outline-none focus:ring-4 focus:ring-{p}/10 border-none'></textarea>
            <button className='bg-{p} text-white py-6 rounded-2xl font-bold text-2xl shadow-xl shadow-{p}/30 hover:scale-[1.02] transition-transform'>Submit Application</button>
        </form>
    </div>
</section>
""")

full_code = f"import React from 'react'; export default function CustomPage() {{ return (<main className='{f} antialiased selection:bg-{p} selection:text-white'>{''.join(sections)}</main>); }}"

site_name = topic.replace(" ", "_").lower()
os.makedirs(f"{site_name}/app", exist_ok=True)
with open(f"{site_name}/app/page.tsx", "w") as f:
    f.write(full_code)

print(f"AI Output: Successfully generated a bespoke {topic} site with a {f} layout.")
'''

agent.learn_new_skill(
    skill_name='Dynamic Code Architect',
    logic_steps=skill_logic,
    keywords=['custom', 'site', 'page', 'build', 'requirement', 'landing', 'website', 'create a', 'create']
)
