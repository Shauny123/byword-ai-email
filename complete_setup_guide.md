# 🚀 Complete Email Automation Setup Guide

## 📋 **System Overview**

Your international legal AI system now includes:
- ✅ **AI-powered email generation** (ChatGPT + Claude)
- ✅ **Google Sheets integration** for data management
- ✅ **N8N workflow automation** for complete case processing
- ✅ **Professional email templates** for all scenarios
- ✅ **Multi-jurisdiction support** with lawyer referrals

---

## 🔧 **Step 1: Install Required Dependencies**

```bash
# In your virtual environment
pip install gspread google-auth google-auth-oauthlib
pip install requests smtplib email
pip install python-dotenv
```

---

## 🗂️ **Step 2: File Organization**

Upload these files to your repository:

```
src/byword_legal/
├── email_system/
│   ├── __init__.py
│   ├── ai_email_manager.py          # Main email system
│   ├── email_templates.json         # All email templates
│   └── google_sheets_setup.py       # Sheets configuration
├── automation/
│   ├── n8n_workflows.json          # N8N workflow definitions
│   └── automation_config.py        # Automation settings
└── config/
    ├── email_config.json           # Email configuration
    └── credentials.json             # Google API credentials
```

---

## 🔐 **Step 3: Environment Variables Setup**

Create a `.env` file in your project root:

```bash
# AI API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Email Configuration
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your_app_password_here
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# Google Sheets
GOOGLE_CREDENTIALS_FILE=config/credentials.json
GOOGLE_SPREADSHEET_ID=your_spreadsheet_id_here

# N8N Configuration
N8N_WEBHOOK_URL=http://your-n8n-instance.com
N8N_API_KEY=your_n8n_api_key_here

# Firm Information
FIRM_NAME=Byword Legal AI
FIRM_PHONE=(555) 123-LEGAL
FIRM_ADDRESS=123 Legal St, Law City, LC 12345
FIRM_WEBSITE=https://byword-legal.com
```

---

## 📊 **Step 4: Google Sheets Setup**

### **4.1 Create Google Service Account**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project: "Byword Legal AI"
3. Enable Google Sheets API and Google Drive API
4. Create Service Account:
   - Name: "byword-legal-sheets"
   - Role: "Editor"
   - Download JSON credentials file
5. Rename to `credentials.json` and place in `config/` folder

### **4.2 Create Master Spreadsheet**

Run this Python script to create all necessary sheets:

```python
from byword_legal.email_system.google_sheets_setup import BywordSheetsSetup

# Initialize and create sheets
setup = BywordSheetsSetup("config/credentials.json")
spreadsheet = setup.create_master_spreadsheet()
print(f"Spreadsheet URL: {spreadsheet.url}")
```

### **4.3 Share Spreadsheet**

1. Copy the spreadsheet URL from above
2. Share with your email address (Editor permissions)
3. Share with service account email (found in credentials.json)
4. Update `GOOGLE_SPREADSHEET_ID` in `.env` file

---

## 🤖 **Step 5: AI API Setup**

### **5.1 OpenAI API**
1. Visit [OpenAI API](https://platform.openai.com/api-keys)
2. Create new API key
3. Add to `.env` as `OPENAI_API_KEY`

### **5.2 Anthropic API**
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Create new API key
3. Add to `.env` as `ANTHROPIC_API_KEY`

---

## 📧 **Step 6: Email System Setup**

### **6.1 Gmail App Password**
1. Enable 2-factor authentication on Gmail
2. Generate App Password:
   - Google Account → Security → App passwords
   - Select "Mail" and your device
   - Use generated password in `.env`

### **6.2 Test Email System**

```python
from byword_legal.email_system.ai_email_manager import AIEmailManager

# Initialize email manager
email_manager = AIEmailManager()

# Test case data
case_data = {
    "case_id": "TEST-001",
    "client_name": "John Doe",
    "claim_type": "wrongful_termination",
    "incident_date": "2024-01-15",
    "jurisdiction": "Colorado, United States",
    "firm_name": "Byword Legal AI",
    "attorney_name": "Sarah Johnson",
    "firm_phone": "(555) 123-LEGAL"
}

# Generate