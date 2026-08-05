# 📄 DocumentReaderAI

> AI-Powered Document Processing System

DocumentReaderAI is an enterprise-style AI application that converts scanned documents, handwritten forms, printed forms, and multi-page PDFs into structured, editable digital data.

The system combines OCR, Artificial Intelligence, document processing, and database technologies to automatically understand documents and extract useful information.

---

# 🎯 Project Vision

The goal of this project is to build an intelligent document processing platform capable of:

- Reading scanned documents
- Reading handwritten forms
- Reading printed forms
- Processing PDFs with hundreds of pages
- Preserving document layout
- Extracting structured information
- Creating editable digital forms
- Saving extracted information into a database
- Allowing users to review and edit extracted data

Instead of manually typing information from documents, the AI performs the work automatically.

---

# 🚀 Current Features

## Frontend

- React
- Vite
- Modern UI
- File Upload Interface

---

## Backend

- FastAPI
- REST API
- Modular Architecture
- Background Processing

---

## Database

- SQLite
- SQLAlchemy ORM

---

## Processing

- File Upload
- PDF Storage
- Background Worker
- Processing Queue
- PDF → Images Conversion

---

## AI (In Progress)

- OCR
- AI Field Extraction
- Editable Form Generation

---

# 🏗 System Architecture

```

                 USER

                   │

                   ▼

           React Frontend

                   │

                   ▼

          Upload Document

                   │

                   ▼

           FastAPI Backend

                   │

      ┌────────────┴────────────┐

      ▼                         ▼

 Store Original File      Create Database Record

      │                         │

      └────────────┬────────────┘

                   ▼

          Create Processing Job

                   │

                   ▼

           Background Worker

                   │

                   ▼

          Convert PDF → Images

                   │

                   ▼

               OCR Engine

                   │

                   ▼

          AI Information Extraction

                   │

                   ▼

             Structured JSON

                   │

                   ▼

            Database Storage

                   │

                   ▼

            Editable Form UI

```

---

# 📂 Project Structure

```

DocumentReaderAI/

│

├── README.md

├── backend/

│

│   ├── app.py

│   ├── requirements.txt

│

│   ├── database/

│   │

│   │   ├── database.py

│   │   ├── models.py

│   │   └── document.db

│

│   ├── routes/

│   │

│   │   └── upload.py

│

│   ├── services/

│   │

│   │   ├── file_service.py

│   │   ├── document_service.py

│   │   ├── job_service.py

│   │   ├── worker_service.py

│   │   ├── pdf_service.py

│   │   ├── ocr_service.py

│   │   ├── extraction_service.py

│   │   └── storage_service.py

│

│   ├── workers/

│   │

│   │   └── processor.py

│

│   ├── uploads/

│

│   ├── temp_images/

│

│   └── venv/

│

└── frontend/

    │

    ├── src/

    ├── components/

    ├── pages/

    └── services/

```

---

# 🛠 Technology Stack

## Frontend

- React
- Vite
- Axios

---

## Backend

- FastAPI
- SQLAlchemy
- SQLite

---

## AI

- PaddleOCR (Planned)
- Pillow
- PyMuPDF

---

## Future AI

- OpenAI GPT
- Local LLM
- Document Layout Detection

---

# 📊 Processing Pipeline

```

Upload Document

↓

Save Original File

↓

Create Database Record

↓

Create Processing Job

↓

Worker Picks Job

↓

Convert PDF → Images

↓

OCR

↓

Extract Text

↓

AI Extraction

↓

Structured JSON

↓

Save to Database

↓

Editable Form

```

---

# 📊 Job Lifecycle

```

Pending

↓

Running

↓

Completed

```

Future

```

Pending

↓

Running

↓

Completed

↓

Failed

↓

Retry

```

---

# 🚀 Installation

Complete installation instructions are available in:

```

INSTALL.md

```

---

# ▶ Running the Project

The application requires three terminals.

## Terminal 1 — Backend

```bash
cd backend

.\venv\Scripts\Activate

python -m uvicorn --version
```

---

## Terminal 2 — Worker

```bash
cd backend

.\venv\Scripts\Activate

python -m workers.processor
```

---

## Terminal 3 — Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 📈 Development Status

## Phase 1

- ✅ React Frontend
- ✅ FastAPI Backend
- ✅ Upload API
- ✅ Database
- ✅ File Storage

---

## Phase 2

- ✅ Background Worker
- ✅ Job Queue
- ✅ Job Status

---

## Phase 3

- ✅ PDF Upload
- ✅ PDF → Images

---

## Phase 4

- ⏳ OCR

---

## Phase 5

- ⏳ AI Extraction

---

## Phase 6

- ⏳ Editable Forms

---

## Phase 7

- ⏳ Dashboard

---

# 🎯 Future Features

- Handwritten Document Recognition
- Printed Form Recognition
- Invoice Processing
- Receipt Processing
- Medical Forms
- Government Forms
- Passport OCR
- Table Extraction
- Signature Detection
- AI Validation
- Search Engine
- User Authentication
- Cloud Storage
- Docker Deployment
- Kubernetes Deployment

---

# 💡 Why This Architecture?

Instead of processing documents during the upload request, DocumentReaderAI creates background jobs.

Advantages:

- Faster uploads
- Better scalability
- Supports very large PDFs
- Multiple workers
- Easier error recovery
- Enterprise architecture

---

# 📚 Documentation

Additional documentation:

- INSTALL.md
- ARCHITECTURE.md
- API.md
- DATABASE.md
- TROUBLESHOOTING.md
- DEVELOPMENT_JOURNAL.md
- ROADMAP.md

---

# 🤝 Contributing

This project follows clean architecture principles.

Every service has a single responsibility.

Every feature is documented.

Every major change is recorded in the Development Journal.

---

# 📅 Current Milestone

✅ Upload System

✅ Background Worker

✅ PDF Processing

⬜ OCR Integration

---

# 🌟 Long-Term Vision

The final application will function as a complete AI-powered document processing platform capable of reading, understanding, extracting, validating, and storing information from virtually any business document.

---

# 👨‍💻 Author

DocumentReaderAI Development Journey

Built step-by-step while learning software architecture, AI engineering, backend development, and enterprise application design.

---

**Version:** 1.0.0

**Status:** Active Development 🚀