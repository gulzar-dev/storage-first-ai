from storage_agent import StorageAgent
agent = StorageAgent()

skills = [
    {
        'name': 'Git Project Initializer',
        'logic': '''
import os, subprocess
project = task.split('for')[-1].strip() if 'for' in task else 'new_project'
os.makedirs(project, exist_ok=True)
subprocess.run(['git', 'init'], cwd=project)
with open(f'{project}/.gitignore', 'w') as f:
    f.write('node_modules/\\n__pycache__/\\n.env\\n')
print(f'AI Output: Initialized Git repository for {project}')
''',
        'keywords': ['git', 'init', 'version control', 'repo', 'repository']
    },
    {
        'name': 'API Client Builder',
        'logic': '''
print('AI Output: Generating API Client Code...')
print("""
// fetchClient.ts
export async function fetchData(endpoint: string) {
  try {
    const res = await fetch(`https://api.example.com${endpoint}`);
    if (!res.ok) throw new Error('Network response was not ok');
    return await res.json();
  } catch (error) {
    console.error('Fetch error:', error);
    throw error;
  }
}
""")
''',
        'keywords': ['api', 'client', 'fetch', 'axios', 'request']
    },
    {
        'name': 'Database Configurator',
        'logic': '''
print('AI Output: Generating SQLite / Prisma Configuration...')
print("""
// schema.prisma
datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
""")
''',
        'keywords': ['database', 'sqlite', 'prisma', 'sql', 'db config']
    },
    {
        'name': 'Test Scaffolder',
        'logic': '''
print('AI Output: Generating Jest Test Suite...')
print("""
// component.test.js
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import MyComponent from './MyComponent';

describe('MyComponent', () => {
  it('renders successfully', () => {
    render(<MyComponent />);
    expect(screen.getByText(/Storage-First AI/i)).toBeInTheDocument();
  });
});
""")
''',
        'keywords': ['test', 'jest', 'pytest', 'unit test', 'tdd']
    },
    {
        'name': 'Readme Generator',
        'logic': '''
project_name = task.split('for')[-1].strip().title() if 'for' in task else 'Project'
print(f'AI Output: Generating Professional README for {project_name}...')
print(f"""
# {project_name}

## Overview
A high-performance application built using local, storage-first AI methodologies.

## Quick Start
```bash
npm install
npm run dev
```

## Architecture
- **Frontend:** Next.js / React
- **Database:** SQLite
- **Intelligence:** Local Storage-First AI Engine
""")
''',
        'keywords': ['readme', 'docs', 'documentation', 'markdown']
    }
]

for skill in skills:
    agent.learn_new_skill(skill['name'], skill['logic'], skill['keywords'])
