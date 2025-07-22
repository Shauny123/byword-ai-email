#!/usr/bin/env python3
"""
Google Sheets Template Setup for Byword Legal AI
Creates all necessary sheets and structures for complete case management
"""

import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime, timedelta

class BywordSheetsSetup:
    """Setup Google Sheets templates for legal AI system"""
    
    def __init__(self, credentials_file: str = "credentials.json"):
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        
        self.creds = Credentials.from_service_account_file(credentials_file, scopes=self.scope)
        self.client = gspread.authorize(self.creds)
    
    def create_master_spreadsheet(self, spreadsheet_name: str = "Byword Legal AI - Master Database"):
        """Create the master spreadsheet with all necessary worksheets"""
        
        try:
            # Create new spreadsheet
            spreadsheet = self.client.create(spreadsheet_name)
            print(f"✅ Created spreadsheet: {spreadsheet_name}")
            
            # Share with your email (replace with your actual email)
            spreadsheet.share('your-email@example.com', perm