**AAIE API Framework Comparison -- FastAPI vs Flask vs DRF vs Express**

**1) Executive Summary**

**Recommendation:** Adopt **FastAPI** as the primary backend framework
for AAIE's model‑serving APIs (AI detection + rubric‑aligned feedback).
FastAPI offers the best blend of developer velocity (auto‑generated
OpenAPI docs and Pydantic validation), excellent async performance on
ASGI (Uvicorn/Starlette), straightforward model‑serving ergonomics in
Python, and a gentle learning curve for our team.

**When to consider alternatives:**

-   **Django REST Framework (DRF):** If we later build a richer data
    platform around a relational DB with complex permissions, admin
    workflows, and multi‑tenant back‑office ops, DRF becomes appealing.

-   **Flask:** Good for very small, hand‑rolled microservices or where
    extremely minimal footprint is required and we control extensions
    ourselves.

-   **Express.js:** If Product mandates a Node‑only stack for certain
    UI‑adjacent services (e.g., webhooks, upload proxy, edge functions).
    For LLM serving, keep Python services in FastAPI and interop via
    HTTP/Queue.

**2) Evaluation Criteria**

1.  **Developer velocity** (DX): type hints → validation, auto docs,
    hot‑reload, dependency injection.

2.  **Performance & Concurrency:** async, WebSockets/streaming, CPU/GPU
    utilization patterns, ability to shard and scale horizontally.

3.  **Integration & Ecosystem:** auth, CORS, ORMs, background tasks,
    task queues, caching, rate limiting, observability.

4.  **Learning curve & community:** quality of docs, examples, stack
    overflow answers, release cadence.

5.  **Deployment & Ops:** containerization, process model (workers),
    serverless viability, reverse proxy (Nginx), CI/CD, health checks,
    readiness, blue/green.

6.  **Security:** auth schemes, JWT/OAuth, input validation,
    schema‑first error responses.

7.  **Maintainability:** code clarity, typing, modularity, versioning,
    breaking‑change policy.

**4) Shortlist Overview (At‑a‑Glance)**

  ------------------------------------------------------------------------------------------------------------
  **Dimension**     **FastAPI**             **Flask**          **Django REST       **Express.js**
                                                               Framework**         
  ----------------- ----------------------- ------------------ ------------------- ---------------------------
  Core runtime      Python, **ASGI**        Python, WSGI       Python, Django      Node.js (V8)
                    (Starlette)             (async optional)   (WSGI/ASGI)         

  Validation &      **First‑class** with                                           
  typing            **Pydantic**                                                   

  Minimal;          Django serializers &                                           
  extensions        validators (robust)                                            
  (Marshmallow,                                                                    
  pydantic‑flask)                                                                  

  Libraries                                                                        
  (zod/joi/ts)                                                                     

  Auto OpenAPI docs **Built‑in              Not built‑in (use  Browsable API &     Not built‑in
                    (Swagger+ReDoc)**       Flask‑RESTX, etc.) schema tools        (swagger‑ui‑express,
                                                                                   OpenAPI generators)

  Async & streaming **Excellent** (ASGI,    Limited/advanced   Good with Django 4+ **Excellent** (native event
                    WebSockets, Server‑Sent                    ASGI, but heavier   loop); streaming easy
                    Events)                                                        

  Performance       **High** (Uvicorn       Moderate           Moderate (heavier   High
  (typical)         workers)                                   stack)              

  ORM & admin       Optional                Optional           **Best‑in‑class**   Optional
                    (SQLModel/SQLAlchemy)                      (Django ORM +       (Prisma/TypeORM/Mongoose)
                                                               Admin)              

  Learning curve    **Gentle** (Pythonic +  Gentle             Steeper (Django     Gentle → moderate (JS+TS
                    types)                  (microframework)   conventions)        choices)

  Ecosystem         High, rapidly growing   **Very high**,     **Very high**,      **Very high**, massive
  maturity                                  many extensions    enterprise‑ready    ecosystem

  Suitability for   **Excellent**           Good for very      Overkill if not     Good, but cross‑language
  model APIs                                small services     using Django stack  friction with Python models
  ------------------------------------------------------------------------------------------------------------

**5) Deep Dive**

**5.1 FastAPI (Python, ASGI)**

-   **Strengths**

    -   **Pydantic models** drive request/response validation, type‑safe
        contracts, and **automatic OpenAPI docs** (Swagger UI & ReDoc)
        with zero extra tooling.

    -   Built on **Starlette** → native **async**, WebSockets,
        background tasks; deploy with **Uvicorn** or **Gunicorn+Uvicorn
        workers**.

    -   Excellent ergonomics for ML/LLM services: easy dependency
        injection for loading models, middlewares for
        auth/observability, clean testing with httpx/pytest.

    -   Ecosystem: SQLModel/SQLAlchemy, Redis clients, Celery/RQ/Arq for
        queues, FastAPI Users/JWT utils, rate‑limiting/middleware
        packages.

-   **Trade‑offs**

    -   Async best practices required (avoid CPU‑bound work on event
        loop; use thread/process pools or task queues for blocking ops).

    -   Keep an eye on Pydantic major changes; pin versions and generate
        contract tests.

-   **Good fit for AAIE**

    -   Python‑native with strong typing; minimal glue around
        PyTorch/HuggingFace.

    -   Clear, shareable API contracts for the Product team; easy
        Postman and SDK generation.

**5.2 Flask (Python, WSGI; async optional)**

-   **Strengths**

    -   Minimal surface area; flexible; huge number of extensions; easy
        to learn.

    -   Great for tiny utilities, webhooks, or when we want to hand‑roll
        everything.

-   **Trade‑offs**

    -   No built‑in schema validation or OpenAPI; must add and maintain
        extensions.

    -   Async support exists but is not the core path; streaming and
        concurrency patterns are more manual.

-   **Fit**

    -   Acceptable for a very small AAIE sidecar, but FastAPI yields
        more value per line for model‑serving.

**5.3 Django REST Framework (Python, Django)**

-   **Strengths**

    -   Best‑in‑class admin, auth, permissions, ORM, browsable API, and
        batteries‑included.

    -   Excellent for complex, multi‑tenant data apps (grading portals,
        educator roles, audit trails).

-   **Trade‑offs**

    -   Heavier; steeper learning curve; more ceremony to ship small
        inference services.

-   **Fit**

    -   Consider if/when AAIE evolves into a full educator data platform
        with complex relational features and we want Django's admin +
        auth.

**5.4 Express.js (Node.js)**

-   **Strengths**

    -   Ubiquitous, tiny core, lots of middleware; very good for
        proxies, upload endpoints, and edge/SSR adjacency.

    -   JS/TS developer familiarity; great streaming support.

-   **Trade‑offs**

    -   No built‑in validation or OpenAPI; must add zod/joi + swagger
        tooling; more manual guardrails.

    -   Cross‑language boundary with Python models (IPC/HTTP) adds
        latency/ops.

-   **Fit**

    -   Keep for UI‑adjacent infrastructure if Product strongly prefers
        Node in a slice. Keep LLM inference in Python FastAPI.

**6) Deployment & Scalability**

**Recommended baseline for AAIE model APIs:**

-   **Process model:** Gunicorn (process manager) + **Uvicorn workers**
    (ASGI), \--workers=N \--threads=M tuned by CPU/GPU profile.

-   **Network:** Nginx (reverse proxy, TLS), optional CDN for caching
    static assets.

-   **Containers:** Docker images with multi‑stage builds (slim Python,
    pinned wheels), health/readiness endpoints.

-   **Serverless option (later):** Cloud Run/Azure Container Apps if
    cold‑start + GPU constraints acceptable.

-   **Observability:** Structured logs (JSON), request IDs, Prometheus
    (or OpenTelemetry) metrics, error reporting (Sentry), latency
    budgets per route.

-   **Performance notes:**

    -   Offload blocking CPU/GPU steps to worker pools or async queues;
        stream partial results for UX (SSE/WebSockets) as needed.

**7) Security & Compliance**

-   **Auth:** Start with signed JWT (short TTL) for internal MVP; rotate
    keys; later add OAuth2/OIDC via gateway.

-   **CORS:** Restricted origins; preflight caching.

-   **Validation:** Schemas for every request/response; fail‑closed with
    clear error envelopes.

-   **Rate limiting:** Middleware + gateway limits; protect expensive
    inference endpoints.

-   **Secrets:** .env for local, runtime env vars in prod; never bake
    secrets into images.

-   **Auditability:** Structured logs with who/what/when; optional
    request/response truncation for PII.

**8) Ease of Integration & Learning Curve**

-   **FastAPI**: Pythonic, type‑driven, minimal boilerplate. Frontend
    gets live Swagger UI to explore and test. Postman collection export
    straight from OpenAPI.

-   **Flask**: Minimal but DIY; documentation is good but patterns vary
    across extensions.

-   **DRF**: Well‑documented, but requires Django mental model.

-   **Express**: Plenty of examples, but validation/docs/security are
    manual unless we standardize a stack (e.g., TypeScript + zod +
    tRPC/OpenAPI).

**9) Community & Release Cadence (qualitative)**

-   FastAPI, Flask, DRF, and Express all have large communities and
    steady updates. For AAIE's purposes, the key differentiator is
    **ASGI‑first** performance and **auto‑docs** that boost team
    velocity, both of which favor FastAPI for model APIs.

**10) Decision & Justification**

**Choose FastAPI** for the **Model API layer** (detection, feedback,
explainability) because it:

1.  Keeps model code, dependencies, and runtime in **Python** (lowest
    friction for ML team).

2.  Provides **type‑safe contracts and auto‑generated OpenAPI**,
    accelerating Product integration and testing.

3.  Runs on **ASGI** with excellent concurrency and streaming support.

4.  Scales cleanly via **Uvicorn workers + Gunicorn**, containers, and
    standard proxies.

**Contingency choices**

-   If AAIE evolves a heavy CRUD/admin platform → consider DRF for those
    specific services.

-   For UI‑adjacent Node work → Express with a clearly documented
    boundary to Python FastAPI services.

**11) Proposed Endpoint Contract (MVP) --- aligned to AAIE T2 (Kasfi
Ahamed v1.0)**

This section mirrors the AAIE -- API Specification (v1.0, T2 2025)
drafted by Kasfi Ahamed and organizes the MVP endpoints with consistent
request/response contracts, RBAC, and error envelopes. It also preserves
the future-scope items as non‑breaking extensions.

**11.1 Authentication & RBAC (Product Engineering)**

**Auth model:** JWT Bearer tokens; roles = student \| teacher \| admin.
All teacher/admin‑only routes require corresponding role.

-   **POST /api/auth/register (admin‑only in MVP)**

    -   Create teacher/admin accounts with a role.

    -   Request { email, password, role }

    -   Response 201 Created { user_id, role }

-   **POST /api/auth/login**

    -   Authenticate and return access token + role.

    -   Request { email, password }

    -   Response 200 OK { token, role, expires_in }

-   **GET /api/auth/me**

    -   Return current user profile and role (for RBAC in UI).

    -   Response 200 OK { user_id, email, role }

**Shared error codes:** 401 Unauthorized, 403 Forbidden, 409 Conflict
(duplicate), 422 Unprocessable Entity (validation).

**11.2 LLM Team APIs (MVP)**

**Core evaluation APIs called directly (dev tools) or orchestrated via
submission endpoints.**

-   **POST /llm/classify**

    -   Purpose: Decide Human / AI / Hybrid from { prompt_text?,
        student_submission, chat_log? }.

> **POST /llm/rubric-score**

-   Purpose: Score Structure, Clarity, Relevance, AcademicWriting using
    > T2 rubric; return labels Excellent\|Good\|Fair\|Poor.

> **POST /llm/generate-feedback**

-   **Purpose:** Produce **student‑facing, actionable feedback** tied to
    > the prompt.

**11.3 Assignments & Submissions (Teacher/Admin only unless noted)**

-   **POST /api/assignments** --- create assignment

    -   **Request** { title, prompt_id?, due_at?, params? }

    -   **Response** 201 Created { assignmentId }

-   **GET /api/assignments** --- list assignments

    -   **Response** 200 OK \[{ assignmentId, title, \...}\]

-   **PUT /api/assignments/{assignmentId}** --- update

-   **DELETE /api/assignments/{assignmentId}** --- remove

-   **POST /api/assignments/{assignmentId}/submit** --- upload +
    **evaluate** submission (orchestrates LLM calls)

    -   **Behavior:** Triggers /llm/classify, /llm/rubric-score,
        /llm/generate-feedback.

    -   **Request** { student_id?, text \| file_ref, prompt_text?,
        chat_log? }

    -   **Response** 202 Accepted (async) or 200 OK (sync)

{

\"submissionId\": \"uuid\",

\"evaluation\": {

\"classification\": {\"label\": \"Human\|AI\|Hybrid\", \"confidence\":
0.0},

\"rubric\": {\"Structure\": \"Good\", \"Clarity\": \"Fair\",
\"Relevance\": \"Good\", \"AcademicWriting\": \"Good\"},

\"feedback\": \"string\"

},

\"version\": \"v1\"

}

-   **POST /api/submissions/{submissionId}/resubmit** --- new version;
    re‑runs same LLM evaluation pipeline.

-   **GET /api/submissions/{submissionId}** --- full package (original,
    rubric, classification, feedback, history).

-   **PATCH /api/submissions/{submissionId}/status** --- reviewed \|
    needs_follow_up \| archived.

-   **GET /api/submissions/{submissionId}/download** --- compiled
    evaluation report (PDF/zip).

-   **DELETE /api/submissions/{submissionId}** --- permanent removal.

**Status codes:** 200, 201, 202, 400, 401, 403, 404, 409, 422, 429, 500.

**11.4 Files**

-   **POST /api/files** --- upload supporting docs → { fileId }

-   **GET /api/files/{fileId}** --- view metadata/preview

-   **GET /api/files/{fileId}/download** --- download original

-   **DELETE /api/files/{fileId}** --- remove

**11.5 User Management (Admin)**

-   **GET /api/users** --- list users with roles & status

-   **PUT /api/users/{userId}** --- update role; deactivate/reactivate

-   **DELETE /api/users/{userId}** --- remove

**11.6 Shared Conventions (Quick Reference)**

-   **Chat log format:** \[{\"role\":\"user\|ai\", \"text\":\"\...\"}\].

-   **Prompt IDs:** stable IDs (e.g., \"P001\") included with
    submissions for evaluation/similarity.

-   **Versioning:** resubmits keep same submissionId; increment version.

-   **Visibility:**

    -   **Student:** feedback + public rubric only.

    -   **Teacher/Admin:** + classification, AI score (future),
        similarity %, highlights, versions.

-   **Feature flags:** enable future features via future_scoring=true
    without breaking T2.

-   **Security/Privacy:** prefer **redaction** before LLM; enforce RBAC
    on teacher‑only fields.

**11.8 Future Scope (Non‑Breaking Additions)**

(Defined but feature‑flagged; see Section 3 in AAIE spec.)

-   **POST /llm/ai-score** → numeric 0--100 likelihood for policy
    thresholds.

-   **POST /llm/prompt-similarity** → % overlap vs prompt + chat log;
    default policy: ≥40% triggers flag.

-   **POST /llm/highlight-spans** → character‑level spans for AI or
    prompt overlap.

-   **POST /llm/evaluate-all** → one‑shot bundle (classification, AI
    score, similarity, rubric scores, feedback).

-   **POST /llm/redact** → remove PII from submissions/chat logs before
    storage or LLM processing.

**13) Risks & Mitigations**

  -----------------------------------------------------------------------
  Risk                       Mitigation
  -------------------------- --------------------------------------------
  Blocking CPU/GPU work      Use worker pools / task queue for heavy ops;
  stalls event loop          short timeouts + retries

  Schema drift between teams Single source of truth = OpenAPI; contract
                             tests in CI; semantic versioning

  Cost spikes under load     Rate limiting, caching, autoscaling; stream
                             partial results

  Security gaps (auth/PII)   JWT + scopes, CORS pinning, structured
                             redaction, secrets mgmt

  Version pinning &          Lockfiles; renovate bot; compatibility tests
  dependency churn           
  -----------------------------------------------------------------------

**14) Deployment Cheat‑Sheet (FastAPI)**

-   **Local:** uvicorn app.main:app \--reload

-   **Prod (single node):** gunicorn -k uvicorn.workers.UvicornWorker
    app.main:app -w 2 -t 60 behind Nginx (TLS, gzip, timeouts).

-   **Containers:** Multi‑stage Dockerfile; non‑root user; healthcheck
    /healthz; pinned deps.

-   **Observability:** Request ID middleware; JSON logs; OpenTelemetry
    exporter; Sentry.

**15) Conclusion & Final Recommendation**

**Conclusion (based on the evaluation results and our team's
strengths):**

-   The AAIE stack is **Python‑first** with a heavy **LLM/ML** workload.
    We need typed request/response contracts, **automatic OpenAPI
    docs**, and **ASGI‑grade concurrency** with low glue around
    PyTorch/HF.

-   Among FastAPI, Flask, DRF, and Express, **FastAPI** offers the best
    balance of **developer velocity**, **operational performance**, and
    **frictionless integration** with our current pipelines. It
    minimizes boilerplate (Pydantic models → validation + docs),
    supports streaming (Uvicorn/Starlette), and fits our MVP timeline.

**Final Recommendation:**

-   **Adopt FastAPI as the primary framework** for AAIE's **T2 MVP and
    near‑term roadmap** (model inference, rubric scoring, feedback,
    similarity, highlights).

-   **Keep DRF** as a future option **only if** Product expands into a
    rich, relational **admin/data platform** (complex roles, audit
    trails, back‑office ops) where Django's ORM/Admin shine.

-   **Use Express.js selectively** for **UI‑adjacent Node services**
    (e.g., proxies, uploads, webhooks) where staying in the JS runtime
    is advantageous---but keep LLM inference in Python.

-   **Reserve Flask** for **very small utilities** or internal tools
    where minimalism outweighs built‑ins.

**Why this matches *our* working style and the team's capability:**

-   We've been driving Python‑based LLM prototyping and will benefit
    from **type‑safe endpoints**, quick **interactive docs**, and **easy
    testability** (httpx/pytest). FastAPI let us iterate quickly while
    preserving contract quality for Product.

  -- -- -------------------------------------------- -- -- -- -- ------- --
                                                                         

                                                                         

                                                                         
  -- -- -------------------------------------------- -- -- -- -- ------- --
