# A mock database of available products
fake_products_db = [
    {
        "item_name": "Customer Support Auto-Responder",
        "sku": "CS-001",
        "price": 599.00,
        "stock": 500,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CS-001&backgroundColor=b6e3f4",
        "description": "Support backlogs erode customer trust and burn out your agents. Our Auto-Responder resolves Tier 1 tickets instantly using advanced NLP — understanding intent, querying your knowledge base, and closing common issues in seconds. Your human team stays focused on the escalations that actually need them, while customers get answers around the clock."
    },
    {
        "item_name": "Sales Lead Qualification Bot",
        "sku": "SL-001",
        "price": 1199.00,
        "stock": 300,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SL-001&backgroundColor=c0aede",
        "description": "Most website visitors leave without ever talking to a human — and your pipeline pays the price. This agent engages prospects 24/7, asks intelligent qualifying questions, scores leads against BANT criteria, and books meetings directly into your sales team's calendar. Stop letting warm leads go cold while your team sleeps."
    },
    {
        "item_name": "Automated Data Entry Assistant",
        "sku": "DE-001",
        "price": 349.00,
        "stock": 1000,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=DE-001&backgroundColor=ffdfbf",
        "description": "Manual data entry is one of the most expensive drains on operational efficiency — slow, error-prone, and deeply demoralizing for skilled staff. This AI extracts structured data from PDFs, emails, and images using OCR and computer vision, then syncs it directly to your CRM or ERP at 99.9% accuracy. Reclaim hundreds of hours per quarter and eliminate costly reconciliation work."
    },
    {
        "item_name": "HR Onboarding Copilot",
        "sku": "HR-001",
        "price": 749.00,
        "stock": 400,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=HR-001&backgroundColor=b6e3f4",
        "description": "A poor onboarding experience is one of the leading drivers of early attrition — and replacing a new hire costs an average of 50–200% of their salary. This copilot gives every new employee a personalized guide through paperwork, IT setup, company policies, and day-one questions, ensuring they feel supported and productive from minute one — without burdening your HR team."
    },
    {
        "item_name": "Financial Report Generator",
        "sku": "FIN-001",
        "price": 1499.00,
        "stock": 150,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=FIN-001&backgroundColor=c0aede",
        "description": "Finance teams spend days each month manually consolidating data that should take minutes — leaving leadership to make decisions on stale numbers. This generator automatically aggregates ledger data across departments to produce polished P&L statements, cash flow forecasts, and anomaly detection reports, giving your executives the real-time clarity they need to act with confidence."
    },
    {
        "item_name": "Inventory Forecasting AI",
        "sku": "INV-001",
        "price": 1999.00,
        "stock": 100,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=INV-001&backgroundColor=ffdfbf",
        "description": "Stockouts cost sales. Overstocking ties up capital. Most businesses are perpetually managing both problems at once. This AI analyzes your historical sales, seasonality, and live market signals to accurately predict demand and automate reordering — reducing stockouts, cutting warehousing overhead, and finally bringing your supply chain in sync with actual customer demand."
    },
    {
        "item_name": "Cybersecurity Threat Analyzer",
        "sku": "SEC-001",
        "price": 3500.00,
        "stock": 75,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SEC-001&backgroundColor=b6e3f4",
        "description": "The average cost of a data breach now exceeds $4 million — and most go undetected for months. This agent acts as your 24/7 SOC analyst, continuously monitoring network traffic, detecting behavioral anomalies, automatically quarantining suspicious endpoints, and producing compliance-ready incident reports. Don't wait for a breach to discover the gaps in your defenses."
    },
    {
        "item_name": "Marketing Campaign Optimizer",
        "sku": "MKT-001",
        "price": 1199.00,
        "stock": 250,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=MKT-001&backgroundColor=c0aede",
        "description": "Ad spend without optimization is just guesswork at scale. This AI continuously A/B tests your copy, adjusts bidding strategies in real-time across Google and Meta, and reallocates budget toward your highest-performing audience segments — so every dollar works harder and your team focuses on strategy instead of manual campaign management."
    },
    {
        "item_name": "Legal Document Reviewer",
        "sku": "LGL-001",
        "price": 2299.00,
        "stock": 120,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=LGL-001&backgroundColor=ffdfbf",
        "description": "Every unreviewed clause in a contract is a potential liability. Legal review at scale is expensive and slow — but skipping it is riskier. This tool scans NDAs, MSAs, and employment contracts against your company playbook, flags non-standard or high-risk language, and suggests compliant alternatives. Accelerate your legal operations without compromising on due diligence."
    },
    {
        "item_name": "Social Media Sentinel",
        "sku": "SM-001",
        "price": 649.00,
        "stock": 600,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SM-001&backgroundColor=b6e3f4",
        "description": "Brand crises don't announce themselves — they escalate before most teams even notice. This sentinel monitors all major social channels for brand mentions, detects negative sentiment spikes in real time, and automatically drafts empathetic responses for your PR team to review and deploy. Protect what you've built before a single bad thread becomes a headline."
    },
    {
        "item_name": "Code Review Assistant Pro",
        "sku": "DEV-001",
        "price": 1399.00,
        "stock": 200,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=DEV-001&backgroundColor=c0aede",
        "description": "Security vulnerabilities and technical debt are far cheaper to catch before they reach production. This assistant integrates directly into your CI/CD pipeline to flag security risks, enforce style guides, and surface performance optimizations at the pull request stage — reducing review bottlenecks, accelerating releases, and keeping your codebase healthy without slowing your engineers down."
    },
    {
        "item_name": "Enterprise Search AI",
        "sku": "ES-001",
        "price": 2799.00,
        "stock": 50,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=ES-001&backgroundColor=ffdfbf",
        "description": "The average knowledge worker wastes nearly two hours a day searching for information scattered across Slack, Drive, Jira, and Confluence. This AI unifies your company's entire knowledge base into a single, permission-aware conversational interface — so employees get accurate, contextual answers in seconds, not hours spent digging through disconnected tools."
    },
    {
        "item_name": "Meeting Summarizer Bot",
        "sku": "MTG-001",
        "price": 399.00,
        "stock": 800,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=MTG-001&backgroundColor=b6e3f4",
        "description": "Meetings generate decisions and action items that too often go undocumented, misremembered, or lost. This bot joins your Zoom, Teams, or Meet calls to provide real-time transcription, extract clear action items, and deliver formatted executive summaries to all attendees automatically. Eliminate post-meeting admin and ensure accountability on every commitment made."
    },
    {
        "item_name": "Predictive Maintenance AI",
        "sku": "PM-001",
        "price": 4200.00,
        "stock": 30,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=PM-001&backgroundColor=c0aede",
        "description": "Unplanned equipment downtime costs manufacturers an average of $260,000 per hour — and it's almost always preventable. This AI ingests IoT sensor data including vibration and temperature readings to detect the early signatures of mechanical failure, then schedules maintenance proactively. Stop reacting to breakdowns and start preventing them before they happen."
    },
    {
        "item_name": "Supply Chain Routing Optimizer",
        "sku": "SC-001",
        "price": 3699.00,
        "stock": 40,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SC-001&backgroundColor=ffdfbf",
        "description": "Logistics inefficiencies quietly compound into significant margin erosion — late deliveries, underloaded containers, and reactive rerouting are all avoidable. This optimizer uses advanced graph algorithms and live transit data to dynamically reroute fleets, maximize container utilization, and deliver precise ETAs. Recover margin on every shipment without adding headcount."
    },
    {
        "item_name": "Compliance Monitoring Agent",
        "sku": "CMP-001",
        "price": 2199.00,
        "stock": 110,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CMP-001&backgroundColor=b6e3f4",
        "description": "Regulatory frameworks like GDPR, CCPA, and HIPAA are constantly evolving — and non-compliance penalties can reach into the tens of millions. This agent continuously audits your data practices against an up-to-date global compliance database, flags potential violations before they become fines, and keeps your team ahead of the regulatory curve rather than scrambling to catch up."
    },
    {
        "item_name": "Customer Feedback Sentiment Engine",
        "sku": "CF-001",
        "price": 899.00,
        "stock": 350,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CF-001&backgroundColor=c0aede",
        "description": "Customer feedback is one of the most valuable signals your business collects — and most of it goes unread. This engine ingests thousands of App Store reviews, NPS responses, and support tickets to identify patterns, categorize feature requests, and surface the core drivers of churn. Turn qualitative noise into the strategic insights your product and CX teams actually need."
    },
    {
        "item_name": "Internal Knowledge Base Bot",
        "sku": "KB-001",
        "price": 999.00,
        "stock": 280,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=KB-001&backgroundColor=ffdfbf",
        "description": "When employees can't find answers about benefits, PTO policies, or internal processes, they interrupt HR and managers — costing your organization time it can't afford. This bot lives in your intranet and answers complex policy questions instantly by synthesizing your scattered wikis and documentation into one reliable, conversational interface available to every employee, 24/7."
    },
    {
        "item_name": "Executive Dashboard AI",
        "sku": "EXEC-001",
        "price": 4999.00,
        "stock": 25,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=EXEC-001&backgroundColor=b6e3f4",
        "description": "C-suite leaders are routinely making decisions on incomplete, delayed, or siloed data — not because the data doesn't exist, but because synthesizing it takes too long. This AI Chief of Staff consolidates signals from across your entire tech stack to deliver daily executive briefings on OKR progress, cash burn, and emerging operational bottlenecks — so leadership is always working from the full picture."
    },
    {
        "item_name": "Automated Pricing Strategy AI",
        "sku": "PRC-001",
        "price": 2499.00,
        "stock": 90,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=PRC-001&backgroundColor=c0aede",
        "description": "Static pricing strategies leave margin on the table in competitive markets and can quietly erode revenue as conditions shift. This AI monitors competitor pricing, models demand elasticity, and adjusts your catalog prices in real-time — helping you capture maximum revenue at every stage of the market cycle without requiring manual intervention from your commercial team."
    },
    {
        "item_name": "Recruitment Sourcing Agent",
        "sku": "REC-001",
        "price": 1099.00,
        "stock": 320,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=REC-001&backgroundColor=ffdfbf",
        "description": "Finding niche technical talent is one of the most time-intensive challenges in modern hiring — with top candidates typically off the market within days. This agent scours GitHub, LinkedIn, and StackOverflow for candidates with highly specific skillsets, crafts personalized outreach at scale, and runs initial async technical screening — so your team spends time only on candidates worth interviewing."
    },
    {
        "item_name": "Contract Lifecycle AI",
        "sku": "CTR-001",
        "price": 1799.00,
        "stock": 130,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CTR-001&backgroundColor=b6e3f4",
        "description": "Auto-renewing contracts, missed deadlines, and buried price escalation clauses cost businesses millions annually — often because vendor agreements live in inboxes and shared drives with no systematic oversight. This AI digitizes your legacy contracts, extracts critical metadata including renewal dates and rate changes, and proactively alerts procurement 90 days before any deadline that matters."
    },
    {
        "item_name": "RFP Response Generator",
        "sku": "RFP-001",
        "price": 2199.00,
        "stock": 85,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=RFP-001&backgroundColor=c0aede",
        "description": "Enterprise RFPs are time-consuming to respond to and easy to lose — not because you lack the capability, but because assembling a 100-page response from scratch every time is unsustainable. This generator produces accurate, tailored RFP responses in minutes by intelligently drawing on your historical security questionnaires and past winning bids, letting your team focus on strategy rather than copy-pasting."
    },
    {
        "item_name": "Video Analytics Sentinel",
        "sku": "VID-001",
        "price": 3299.00,
        "stock": 60,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=VID-001&backgroundColor=ffdfbf",
        "description": "Most organizations have extensive CCTV infrastructure that generates footage no one can realistically review. This sentinel applies deep learning to your existing camera feeds to track retail foot traffic patterns, monitor factory floor safety compliance, and alert security to unauthorized access — transforming a passive recording system into an active operational intelligence layer."
    },
    {
        "item_name": "Expense Auditing Agent",
        "sku": "EXP-001",
        "price": 749.00,
        "stock": 450,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=EXP-001&backgroundColor=b6e3f4",
        "description": "Expense fraud and policy non-compliance are more common than most finance teams realize — and manual review processes rarely catch them consistently. This agent reads submitted receipts, cross-references them against your corporate policy limits, and automatically flags duplicates and out-of-policy claims for review before they reach payroll. Protect your bottom line with systematic oversight that never gets tired or distracted."
    },
    {
        "item_name": "IT Helpdesk Resolution Bot",
        "sku": "IT-001",
        "price": 1299.00,
        "stock": 210,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=IT-001&backgroundColor=c0aede",
        "description": "IT helpdesks are overwhelmed by repetitive, low-complexity tickets that consume time your team should be spending on infrastructure and security. This bot deflects up to 60% of common requests by autonomously resetting passwords, provisioning software licenses, and troubleshooting VPN issues — all directly within Slack or Teams, without a single ticket ever needing human intervention."
    },
    {
        "item_name": "Customer Churn Prediction Agent",
        "sku": "CHP-001",
        "price": 1349.00,
        "stock": 175,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CHP-001&backgroundColor=ffdfbf",
        "description": "Most businesses only discover a customer has churned after it's already too late to act. This agent continuously analyzes behavioral signals — login frequency, feature usage, support history, and payment patterns — to identify at-risk accounts weeks before cancellation. It then triggers personalized intervention workflows for your success team, allowing them to step in with precisely the right offer at precisely the right moment."
    },
    {
        "item_name": "Accounts Receivable Collections AI",
        "sku": "AR-001",
        "price": 1099.00,
        "stock": 220,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=AR-001&backgroundColor=b6e3f4",
        "description": "Chasing overdue invoices is time-consuming, uncomfortable, and inconsistent when left to humans. This agent monitors your AR ledger, automatically sends personalized payment reminders on optimized schedules, escalates strategically based on invoice age and customer history, and flags accounts for human review only when truly necessary. Reduce your average days sales outstanding without straining client relationships."
    },
    {
        "item_name": "Competitive Intelligence Monitor",
        "sku": "CI-001",
        "price": 1699.00,
        "stock": 140,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=CI-001&backgroundColor=c0aede",
        "description": "By the time your team manually discovers a competitor's new product launch, pricing change, or strategic pivot, you've already lost response time. This agent continuously monitors competitor websites, press releases, job postings, and review platforms to surface actionable intelligence — delivered as a structured weekly briefing to your product, sales, and leadership teams so you're always one step ahead."
    },
    {
        "item_name": "Employee Productivity Analytics Agent",
        "sku": "EPA-001",
        "price": 1499.00,
        "stock": 160,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=EPA-001&backgroundColor=ffdfbf",
        "description": "Without clear visibility into how work actually gets done, managers rely on assumptions — and high-performing teams get the same treatment as struggling ones. This agent analyzes anonymized workflow data across your tools to identify bottlenecks, highlight collaboration gaps, and surface burnout risk before it becomes attrition. Give your people managers the insight they need to coach effectively and allocate resources fairly."
    },
    {
        "item_name": "Vendor Risk Assessment AI",
        "sku": "VRA-001",
        "price": 1999.00,
        "stock": 95,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=VRA-001&backgroundColor=b6e3f4",
        "description": "Third-party vendors are one of the most underestimated sources of operational, financial, and reputational risk for modern businesses. This agent continuously monitors your supplier ecosystem — tracking financial stability signals, news sentiment, cybersecurity posture, and regulatory standing — and generates tiered risk scores for your procurement team. Know which vendor relationships need attention before a crisis forces your hand."
    },
    {
        "item_name": "Sales Forecasting & Pipeline AI",
        "sku": "SF-001",
        "price": 1599.00,
        "stock": 185,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=SF-001&backgroundColor=c0aede",
        "description": "Inaccurate sales forecasts lead to poor hiring decisions, missed targets, and misallocated resources — and most CRM-based forecasts rely too heavily on rep-reported data that is inherently optimistic. This AI analyzes deal velocity, engagement signals, historical win rates, and market conditions to produce forecasts your leadership can actually plan around. Give finance and operations a revenue number they can trust."
    },
    {
        "item_name": "E-Commerce Personalization Engine",
        "sku": "ECP-001",
        "price": 2299.00,
        "stock": 115,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=ECP-001&backgroundColor=ffdfbf",
        "description": "Generic product recommendations and one-size-fits-all email campaigns consistently underperform — because your customers have individual needs your current tools aren't addressing. This engine analyzes real-time browsing behavior, purchase history, and contextual signals to serve hyper-personalized product recommendations, dynamic pricing, and targeted offers across your storefront and email channels. Increase average order value and repeat purchase rate without increasing ad spend."
    },
    {
        "item_name": "Multilingual Customer Communication Agent",
        "sku": "MLC-001",
        "price": 1149.00,
        "stock": 270,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=MLC-001&backgroundColor=b6e3f4",
        "description": "Expanding into new markets is costly enough without also hiring multilingual support staff for every region you enter. This agent communicates fluently with customers in over 50 languages across chat, email, and social — maintaining your brand voice and tone in every interaction. Deliver a consistent, high-quality customer experience globally without the overhead of region-specific support teams."
    },
    {
        "item_name": "Grant & Proposal Writing Assistant",
        "sku": "GPA-001",
        "price": 1299.00,
        "stock": 200,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=GPA-001&backgroundColor=c0aede",
        "description": "For nonprofits, research institutions, and growth-stage companies, winning grants and government contracts is a critical revenue stream — but the writing process is labor-intensive and highly technical. This assistant analyzes funding requirements, cross-references your organization's past successful applications, and generates tailored, compliance-ready proposal drafts that your team can refine and submit in a fraction of the usual time."
    },
    {
        "item_name": "Employee Scheduling & Shift Optimizer",
        "sku": "ESO-001",
        "price": 899.00,
        "stock": 310,
        "image_url": "https://api.dicebear.com/9.x/bottts/svg?seed=ESO-001&backgroundColor=ffdfbf",
        "description": "Manual shift scheduling for large or distributed teams is a constant source of errors, conflicts, and compliance risk — especially when factoring in labor laws, skill coverage requirements, and last-minute absences. This optimizer automatically generates schedules that balance employee availability, contractual constraints, and operational demand, then dynamically adjusts when the unexpected happens. Reduce scheduling time from hours to minutes and minimize costly overstaffing or coverage gaps."
    }
]