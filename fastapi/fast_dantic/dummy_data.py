# A mock database of available products
fake_products_db = [
    {
        "item_name": "Customer Support Auto-Responder",
        "sku": "CS-001",
        "price": 499.00,
        "stock": 500,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CS-001&backgroundColor=b6e3f4",
        "description": "Instantly handle Tier 1 support tickets with our advanced NLP model. Understands intent, accesses knowledge bases, and resolves common issues in seconds, freeing your human agents for complex escalations."
    },
    {
        "item_name": "Sales Lead Qualification Bot",
        "sku": "SL-001",
        "price": 899.00,
        "stock": 300,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SL-001&backgroundColor=c0aede",
        "description": "Automate your top-of-funnel outreach. This agent engages website visitors 24/7, asks qualifying questions, scores leads based on BANT criteria, and books meetings directly into your sales team's calendar."
    },
    {
        "item_name": "Automated Data Entry Assistant",
        "sku": "DE-001",
        "price": 299.00,
        "stock": 1000,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=DE-001&backgroundColor=ffdfbf",
        "description": "Eliminate manual copy-pasting. This AI seamlessly extracts structured data from PDFs, emails, and images using OCR and computer vision, automatically syncing it to your CRM or ERP system with 99.9% accuracy."
    },
    {
        "item_name": "HR Onboarding Copilot",
        "sku": "HR-001",
        "price": 650.00,
        "stock": 400,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=HR-001&backgroundColor=b6e3f4",
        "description": "Provide new hires with a personalized concierge. Guides them through paperwork, explains company policies, helps set up IT accounts, and answers common day-one questions perfectly."
    },
    {
        "item_name": "Financial Report Generator",
        "sku": "FIN-001",
        "price": 1200.00,
        "stock": 150,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=FIN-001&backgroundColor=c0aede",
        "description": "Transform raw ledger data into executive-ready insights. Automatically aggregates financial data across departments to generate beautiful P&L statements, cash flow forecasts, and anomaly detection reports."
    },
    {
        "item_name": "Inventory Forecasting AI",
        "sku": "INV-001",
        "price": 1500.00,
        "stock": 100,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=INV-001&backgroundColor=ffdfbf",
        "description": "Optimize your supply chain with predictive models. Analyzes historical sales, seasonality, and market trends to predict demand and automate re-ordering, reducing stockouts and warehousing costs."
    },
    {
        "item_name": "Cybersecurity Threat Analyzer",
        "sku": "SEC-001",
        "price": 2500.00,
        "stock": 75,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SEC-001&backgroundColor=b6e3f4",
        "description": "Your 24/7 SOC analyst. Continuously monitors network traffic, detects anomalies using behavioral analytics, automatically quarantines suspicious endpoints, and generates compliance-ready incident reports."
    },
    {
        "item_name": "Marketing Campaign Optimizer",
        "sku": "MKT-001",
        "price": 950.00,
        "stock": 250,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=MKT-001&backgroundColor=c0aede",
        "description": "Maximize your ad spend ROI. This AI A/B tests ad copy, adjusts bidding strategies in real-time across Google and Meta, and allocates budget to the highest-performing demographic segments."
    },
    {
        "item_name": "Legal Document Reviewer",
        "sku": "LGL-001",
        "price": 1800.00,
        "stock": 120,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=LGL-001&backgroundColor=ffdfbf",
        "description": "Accelerate your legal operations. Scans NDAs, MSAs, and employment contracts for non-standard clauses, highlights potential risks based on your company playbook, and suggests compliant alternative language."
    },
    {
        "item_name": "Social Media Sentinel",
        "sku": "SM-001",
        "price": 550.00,
        "stock": 600,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SM-001&backgroundColor=b6e3f4",
        "description": "Protect your brand reputation proactively. Monitors social channels for brand mentions, triggers alerts for negative sentiment spikes, and can automatically draft empathetic responses for your PR team."
    },
    {
        "item_name": "Code Review Assistant Pro",
        "sku": "DEV-001",
        "price": 1100.00,
        "stock": 200,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=DEV-001&backgroundColor=c0aede",
        "description": "Supercharge your engineering velocity. Runs locally in your CI/CD pipeline to catch security vulnerabilities, enforce style guides, and suggest performance optimizations before code ever reaches production."
    },
    {
        "item_name": "Enterprise Search AI",
        "sku": "ES-001",
        "price": 2200.00,
        "stock": 50,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=ES-001&backgroundColor=ffdfbf",
        "description": "Unify your company's knowledge. Connects to Slack, Google Drive, Jira, and Confluence to provide a single, permission-aware conversational interface for employees to find any internal document or answer."
    },
    {
        "item_name": "Meeting Summarizer Bot",
        "sku": "MTG-001",
        "price": 350.00,
        "stock": 800,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=MTG-001&backgroundColor=b6e3f4",
        "description": "Never take meeting notes again. Joins Zoom, Teams, or Meet calls to provide real-time transcription, extract action items, and email beautifully formatted executive summaries to all attendees."
    },
    {
        "item_name": "Predictive Maintenance AI",
        "sku": "PM-001",
        "price": 3000.00,
        "stock": 30,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=PM-001&backgroundColor=c0aede",
        "description": "Avoid costly downtime on the factory floor. Ingests IoT sensor data (vibration, temperature) to detect early signs of equipment failure and schedules maintenance before catastrophic breakdowns occur."
    },
    {
        "item_name": "Supply Chain Routing Optimizer",
        "sku": "SC-001",
        "price": 2800.00,
        "stock": 40,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SC-001&backgroundColor=ffdfbf",
        "description": "Slash your logistics costs. Uses advanced graph algorithms and real-time transit data to dynamically re-route fleets, optimize container loading, and predict exact ETAs."
    },
    {
        "item_name": "Compliance Monitoring Agent",
        "sku": "CMP-001",
        "price": 1600.00,
        "stock": 110,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CMP-001&backgroundColor=b6e3f4",
        "description": "Stay ahead of regulatory changes. Continuously audits your customer data practices against an updated database of global frameworks (GDPR, CCPA, HIPAA) and flags potential compliance violations."
    },
    {
        "item_name": "Customer Feedback Sentiment Engine",
        "sku": "CF-001",
        "price": 750.00,
        "stock": 350,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CF-001&backgroundColor=c0aede",
        "description": "Turn qualitative feedback into quantitative logic. Ingests thousands of App Store reviews, NPS surveys, and support tickets to categorize feature requests and identify core drivers of churn."
    },
    {
        "item_name": "Internal Knowledge Base Bot",
        "sku": "KB-001",
        "price": 850.00,
        "stock": 280,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=KB-001&backgroundColor=ffdfbf",
        "description": "The ultimate self-serve portal. Sits in your company intranet and answers complex employee questions about benefits, PTO policies, and internal workflows by synthesizing thousands of scattered wikis."
    },
    {
        "item_name": "Executive Dashboard AI",
        "sku": "EXEC-001",
        "price": 3500.00,
        "stock": 25,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=EXEC-001&backgroundColor=b6e3f4",
        "description": "Your AI Chief of Staff. Synthesizes data from across your entire tech stack to give C-suite leaders daily briefings on OKR progress, cash burn, and hidden operational bottlenecks."
    },
    {
        "item_name": "Automated Pricing Strategy AI",
        "sku": "PRC-001",
        "price": 1950.00,
        "stock": 90,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=PRC-001&backgroundColor=c0aede",
        "description": "Maximize margins with dynamic pricing. Scrapes competitor websites and analyzes elasticity of demand to automatically adjust your catalog prices in real-time, driving revenue growth."
    },
    {
        "item_name": "Recruitment Sourcing Agent",
        "sku": "REC-001",
        "price": 800.00,
        "stock": 320,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=REC-001&backgroundColor=ffdfbf",
        "description": "Find the legendary 10x engineer. Automatically searches GitHub, LinkedIn, and StackOverflow for niche skillsets, drafts highly personalized outreach emails, and conducts initial async technical screening."
    },
    {
        "item_name": "Contract Lifecycle AI",
        "sku": "CTR-001",
        "price": 1450.00,
        "stock": 130,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CTR-001&backgroundColor=b6e3f4",
        "description": "Never miss a renewal date again. Digitizes all legacy vendor contracts, extracts key meta-data (dates, auto-renewal clauses, price bumps), and alerts procurement teams 90 days before critical deadlines."
    },
    {
        "item_name": "RFP Response Generator",
        "sku": "RFP-001",
        "price": 1750.00,
        "stock": 85,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=RFP-001&backgroundColor=c0aede",
        "description": "Win more enterprise deals, faster. Generates highly accurate 100-page RFP responses in minutes by intelligently querying your company's historical security questionnaires and past successful bids."
    },
    {
        "item_name": "Video Analytics Sentinel",
        "sku": "VID-001",
        "price": 2700.00,
        "stock": 60,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=VID-001&backgroundColor=ffdfbf",
        "description": "Transform CCTV into actionable data. Uses deep learning to track retail foot traffic, monitor factory floor safety compliance without facial recognition, and alert security to unauthorized intrusions."
    },
    {
        "item_name": "Expense Auditing Agent",
        "sku": "EXP-001",
        "price": 600.00,
        "stock": 450,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=EXP-001&backgroundColor=b6e3f4",
        "description": "Stop expense fraud instantly. Reads submitted receipts, cross-references against corporate policy limits, flags duplicates and out-of-policy spending for manual review before sending to payroll."
    },
    {
        "item_name": "IT Helpdesk Resolution Bot",
        "sku": "IT-001",
        "price": 1050.00,
        "stock": 210,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=IT-001&backgroundColor=c0aede",
        "description": "Deflect 60% of common IT tickets. This agent can automatically reset passwords, provision software licenses via SSO integrations, and troubleshoot VPN connections directly within your team's Slack or Teams channels."
    }
]
