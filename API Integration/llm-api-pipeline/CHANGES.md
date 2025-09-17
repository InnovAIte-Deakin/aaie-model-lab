# LLM Evaluation Pipeline - Changes Summary

## Directory Structure Changes

### Before (Primary Version)

```
llm-eval-pipeline_1/
└── llm-eval-pipeline/
    ├── app/
    ├── requirements.txt
    ├── tests/
    └── README.md
```

### After (Current Version)

```
llm-eval-pipeline/
├── app/
├── requirements.txt
├── tests/
├── README.md
└── llm-pipeline.log
```

**Change**: Flattened directory structure by removing one nesting level.

## Code Changes

### 1. app/main.py

#### Added CORS Middleware

**Current version** includes CORS configuration that was missing in the primary version:

```python
# Added in current version
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LLM Evaluation Pipeline", version="1.1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
svc = EvaluatorService()
```

#### Added Evaluation Endpoint

**Current version** includes an additional endpoint that combines all evaluation components:

```python
# Added in current version
@app.post("/api/v1/evaluate")
async def evaluate(req: EvalRequest):
    try:
        data = await svc.evaluate(req.domain, req.prompt, req.rubric.model_dump(), req.submission)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**Primary version** only had these endpoints:

- `/api/v1/classification`
- `/api/v1/confidence`
- `/api/v1/rubric-scores`
- `/api/v1/feedback`

### 2. requirements.txt

#### Dependency Version Change

```diff
# Primary version
- numpy==2.1.1

# Current version
+ numpy>=1.21.0
```

**Change**: Made numpy version constraint more flexible (from exact pin to minimum version).

## New Files

### llm-pipeline.log

**Added in current version** - Contains 514 lines of API usage logs showing:

- Successful API calls (200 OK responses)
- Multiple 500 Internal Server Error responses
- Evidence of active testing and development
- Server startup/shutdown logs

## Unchanged Files

The following files remain identical between both versions:

- `app/config.py`
- `tests/test_smoke.py`
- All files in `app/data/` directory
- All files in `app/models/` directory
- All files in `app/prompting/` directory
- All files in `app/services/` directory
- All files in `app/utils/` directory
- `app/schemas.py`
- `app/__init__.py`

## Migration Notes

To upgrade from the primary version to the current version:

1. **Update main.py**: Add CORS middleware and `/api/v1/evaluate` endpoint
2. **Update requirements.txt**: Change numpy constraint to `>=1.21.0`
3. **Test endpoints**: Verify all endpoints work correctly, especially the new combined endpoint

The current version is backward compatible - all existing endpoints work the same way, with additional functionality added.
