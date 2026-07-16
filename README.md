# 🎫 AI Ticket Analyzer

An intelligent customer support ticket analysis system built using **FastAPI**, **Streamlit**, and **Transformer-based NLP models**. The application automatically classifies support tickets, extracts key entities, generates concise summaries, and validates predictions through a modular AI pipeline.

🔗 **Live Demo:**  
https://satvika-122-ticket-analyser-mcp-app-mcp-client-server-l92cug.streamlit.app/

---

# 🚀 Features

- Automated support ticket classification
- Named Entity Recognition (NER) for extracting critical information
- AI-generated ticket summaries
- Confidence-based output validation
- Modular backend architecture
- Interactive Streamlit web interface
- REST API powered by FastAPI
- Easily extensible for future AI capabilities

---

# 🏗️ System Architecture

```
                    +----------------------+
                    |   Streamlit Client   |
                    +----------+-----------+
                               |
                         HTTP Requests
                               |
                               ▼
                    +----------------------+
                    |    FastAPI Backend   |
                    +----------+-----------+
                               |
          +--------------------+--------------------+
          |                    |                    |
          ▼                    ▼                    ▼
 Ticket Classification   Entity Extraction   Summary Generation
          |                    |                    |
          +--------------------+--------------------+
                               |
                               ▼
                    Validation & Confidence Check
                               |
                               ▼
                        Structured JSON Response
```

---

# 🧠 AI Pipeline

The application processes every support ticket through multiple stages:

### 1. Ticket Classification
Categorizes incoming tickets into:

- Payment Issues
- Account Issues
- Technical Issues
- Delivery Issues
- Other

---

### 2. Entity Extraction

Automatically detects important information such as:

- Order ID
- Transaction ID
- Email Address
- Phone Number
- Customer Name (when available)

---

### 3. Ticket Summarization

Generates a concise natural-language summary that helps support teams quickly understand customer issues.

---

### 4. Validation

Performs internal confidence checks before returning results, improving reliability and reducing low-confidence predictions.

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Machine Learning | Hugging Face Transformers |
| NLP Models | FLAN-T5, BERT NER |
| Database | SQLite |
| Language | Python |

---

# 📂 Project Structure

```
Ticket_Analyser/
│
├── app.py
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── database/
├── requirements.txt
└── README.md
```

---

# ▶️ Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Satvika-122/ticket_analyser_mcp.git
cd ticket_analyser_mcp/Ticket_Analyser
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
.\venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start the FastAPI Server

```bash
uvicorn backend.main:app --reload
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 5. Launch the Streamlit Application

```bash
streamlit run app.py
```

---

# 🧪 Example

### Input

```
My payment was deducted but order ID 12345 was not confirmed.
```

### Output

**Category**

```
Payment Issue
```

**Entities**

```
Order ID: 12345
```

**Summary**

```
The customer reports a payment issue related to order ID 12345 that requires investigation.
```

---

# 🔒 Validation Strategy

The system performs an internal validation step before returning predictions.

- Confidence-based verification
- Internal quality checks
- Reliable structured outputs
- Ready for future human review workflows

---

# 📈 Future Enhancements

- Retrieval-Augmented Generation (RAG)
- Multi-language support
- Human-in-the-Loop review
- Cloud deployment (AWS, Azure, GCP)
- Real-time streaming responses
- Analytics dashboard
- Authentication and user management

---

# 💡 Why This Project?

This project demonstrates practical software engineering and AI concepts including:

- REST API development
- End-to-end NLP pipeline
- Transformer-based text processing
- Modular backend architecture
- Interactive frontend development
- Production-oriented project organization

---

# 👩‍💻 Author

**Satvika Dwaram**

AI & Data Science Engineer

- GitHub: https://github.com/Satvika-122
- LinkedIn: *(Add your LinkedIn profile here)*

---

# 📄 License

This project is intended for educational and demonstration purposes.
