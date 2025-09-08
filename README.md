# model-lab
Central repository for the Model Training Team, focused on building, training, and evaluating AI/ML models. Includes model development scripts, training experiments, evaluation results, and related documentation.

## New: LLM Rubric Scoring API

We've implemented a **POST endpoint `/llm/rubric-score`** that evaluates student submissions using rubric categories. The API provides automated scoring across four key dimensions: Structure, Clarity, Relevance, and Academic Writing.

### Project Structure
```
├── Evaluation/                    # Human evaluation rubrics and guidelines
│   ├── AI Detection/             # AI detection evaluation criteria
│   ├── Feedback Generation/      # Feedback generation evaluation criteria
│   └── README.md                 # Evaluation framework documentation
├── api/                          # LLM Rubric Scoring API
│   ├── app.py                    # Main Flask application
│   ├── requirements.txt          # Python dependencies
│   ├── README.md                 # API overview and quick start
│   ├── API_README.md             # Comprehensive API documentation
│   ├── test_app.py               # Unit tests
│   └── example_usage.py          # Usage examples
├── Experimental Plan/             # Research and experimental design
├── Model and Prompt Selection/    # Model selection strategies
├── Fine Tuning Research/         # Fine-tuning methodologies
└── Upskilling Docs/              # Team training materials
```

### API Features
- **Automated Evaluation**: Uses LLM to score student submissions
- **Standardized Rubrics**: Consistent evaluation criteria
- **Input Validation**: Robust error handling and validation
- **Comprehensive Testing**: Full test suite included
- **Production Ready**: Ready for integration with real LLM providers

### Quick Start with API
```bash
cd api
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:5000`

### Documentation
- **API Overview**: See `api/README.md`
- **Full Documentation**: See `api/API_README.md`
- **Examples**: See `api/example_usage.py`
- **Tests**: Run `python api/test_app.py`

## Current Focus Areas

1. **Human Evaluation Framework**: Comprehensive rubrics for AI model assessment
2. **LLM Integration**: Automated scoring using AI models
3. **Quality Assurance**: Standardized evaluation processes
4. **Team Training**: Upskilling materials and guidelines

## Recent Updates

- **Human Evaluation Rubrics**: Complete frameworks for AI detection and feedback generation
- **LLM Rubric Scoring API**: Automated evaluation endpoint with comprehensive testing
- **Documentation**: Complete API documentation and usage examples
- **Code Organization**: Structured API implementation in dedicated folder

---

**Repository**: Forked from `InnovAIte-Deakin/model-lab`  
**Status**: Active development with new API implementation  
**Last Updated**: January 2025