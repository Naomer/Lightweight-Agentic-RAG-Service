from pydantic import BaseModel
from typing import List, Optional

class AnalyzeRequest(BaseModel):
    text: str

class LeadAnalysis(BaseModel):
    # Adding = None or = "Unknown" makes these optional
    startup_name: Optional[str] = "Unknown"
    hiring_signal: bool
    remote_possible: bool
    funding_stage: Optional[str] = "unknown"
    reasoning: Optional[str] = "No reasoning provided." # Fixes the crash!
    source_url: Optional[str] = "No URL available"
    
class AnalyzeResponse(BaseModel):
    question: str
    context_used: List[str]
    analysis: LeadAnalysis
