# Phase 1: Opportunity Scan (SCAN)

| No. | Problem / Business Operation | Member Company | Lens Type | Short Description of Bottleneck |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Transshipment & Dispatching Coordination | Xanh SM / VinBus | Time-consuming / Repetitive | Dispatchers manually calculate routes and match available vehicles to transshipment requests, causing delays during peak hours. |
| 2 | Maintenance Ticket Routing | Vinhomes | Time-consuming | Customer service staff read hundreds of free-text repair requests daily to categorize and assign technicians. |
| 3 | Technical Manual Retrieval | VinFast | AI-upgrade | Technicians spend excessive time searching through thousands of pages of manuals when diagnosing new EV error codes. |
| 4 | Patient Symptom Triage | Vinmec | Stakeholder Pain | Patients experience long wait times during initial reception because symptom categorization and department routing are done manually. |
| 5 | Room Service Scheduling | Vinpearl | Repetitive | Housekeeping requests are manually logged and assigned over walkie-talkies, leading to miscommunications and lost tasks. |

---

# Phase 2: Quick-Assess (3 Problem Cards)

### Card 1: Intelligent Transshipment & Dispatching Tool
*   **Company:** Xanh SM / VinBus
*   **Actor/Operator:** Fleet Dispatcher (Điều phối viên)
*   **Current Workflow:** Request received $\rightarrow$ Dispatcher checks vehicle availability on map $\rightarrow$ Manually calculates optimal route $\rightarrow$ Assigns driver via system/radio $\rightarrow$ Updates log.
*   **Bottleneck:** Manually matching routes and available vehicles takes 5-10 minutes per batch, leading to idle vehicles and delayed pick-ups.
*   **AI Intervention:** An LLM-based agent processes natural language requests, evaluates current vehicle coordinates, and instantly suggests the top 3 optimized dispatch matches.
*   **Success Metric:** Reduce dispatch calculation and assignment time from 10 minutes to under 2 minutes per batch.
*   **Initial Architecture:** LLM Feature (Data extraction & matching) combined with Rule-based routing algorithms.

### Card 2: EV Technical Assistant
*   **Company:** VinFast
*   **Actor/Operator:** Service Center Technician
*   **Current Workflow:** Technician reads diagnostic error code $\rightarrow$ Opens PDF manuals $\rightarrow$ Uses Ctrl+F to find the error $\rightarrow$ Reads through diagnostic steps $\rightarrow$ Applies fix.
*   **Bottleneck:** Searching and synthesizing information across multiple PDF versions for complex, cascading errors takes 15-20 minutes.
*   **AI Intervention:** A RAG (Retrieval-Augmented Generation) chatbot trained on VinFast manuals that instantly retrieves step-by-step repair guides based on error codes.
*   **Success Metric:** Reduce time spent searching documentation by 80% (from 15 minutes to 3 minutes).
*   **Initial Architecture:** LLM Feature (RAG System).

### Card 3: Maintenance Ticket Routing
*   **Company:** Vinhomes
*   **Actor/Operator:** Customer Service Representative
*   **Current Workflow:** Resident submits text request via app $\rightarrow$ CS reads request $\rightarrow$ Determines category (Electrical, Plumbing, etc.) $\rightarrow$ Forwards to specific technician team.
*   **Bottleneck:** Reading and categorizing unstructured text requests takes 3-5 minutes per ticket and is prone to human error.
*   **AI Intervention:** Text classification AI that automatically extracts the issue type, urgency, and location, then routes it to the correct department.
*   **Success Metric:** Achieve 95% automated routing accuracy and reduce manual processing time to 0.
*   **Initial Architecture:** Rule-based fallback + LLM Classification Feature.
