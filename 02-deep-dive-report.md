# Phase 3 & 5: Deep-Dive & Evaluation Report

**Group Name:** [Your Group Name]
**Members:**
1. Nguyen Nam Anh (Student ID: [Add Your ID]) 
2. [Teammate 2 Name] (Student ID: [ID])
3. [Teammate 3 Name] (Student ID: [ID])

---

## 1. Selected Problem
**Intelligent Transshipment & Dispatching Tool (Xanh SM / VinBus)**

## 2. Problem Statement (6-Field Framework)
1.  **Actor:** Fleet Dispatcher (Điều phối viên).
2.  **Current Workflow:** Dispatchers receive transshipment requests, manually cross-reference available vehicles on the tracking dashboard, estimate travel times, and assign drivers.
3.  **Bottleneck:** The cognitive load of matching dynamic requests with real-time vehicle locations. It takes an average of 8 minutes to process a complex dispatching batch, leading to system bottlenecks during rush hour.
4.  **Business Impact:** High vehicle idle time, increased fuel waste, and lower customer satisfaction due to delayed response times.
5.  **Success Metric:** Reduce dispatch matching time by 75% (from 8 minutes to 2 minutes) while maintaining or improving route efficiency.
6.  **Operational Boundary:** The AI cannot autonomously dispatch vehicles. All AI-generated dispatch recommendations must be reviewed and approved by the human Dispatcher (Human-in-the-loop).

## 3. Future-State Flow & AI Fit
*   **Workflow:** 
    1. Transshipment request enters system.
    2. AI Agent extracts location, urgency, and passenger/cargo count.
    3. AI queries system for vehicle coordinates and generates 3 optimized dispatch options.
    4. **Human-in-the-loop:** Dispatcher reviews the options on the UI and clicks "Approve" on the best one.
    5. System automatically notifies the assigned driver.
*   **AI Category:** Agentic Loop (Reasoning through available data and APIs) with an LLM Feature for natural language extraction.
*   **Fallback Plan:** If the AI API times out or returns a confidence score below 80%, the system defaults to the legacy dashboard, requiring the dispatcher to assign the route manually.

## 4. Evaluation (Phase 5)
*   **Technical Feasibility:** High. LLMs are excellent at extracting structured JSON from natural language requests, which can easily be fed into a standard routing algorithm.
*   **Cost Estimation:** Very Low. Using Gemini 2.5 Flash costs fractions of a cent per prompt. Processing 1,000 tickets a day would cost less than $1/day in API fees.
*   **Final Decision:** **GO**. The problem is well-scoped, the bottleneck is clear, the human-in-the-loop ensures safety, and the ROI (Return on Investment) regarding time saved is massive.