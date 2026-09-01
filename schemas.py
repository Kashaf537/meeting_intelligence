
# schemas.py

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# ---------------------------------------------------------
# Shared Types
# ---------------------------------------------------------

Priority = Literal["high", "medium", "low"]


# ---------------------------------------------------------
# Decision
# ---------------------------------------------------------

class Decision(BaseModel):
    model_config = ConfigDict(extra="forbid")

    decision: str
    evidence: str


# ---------------------------------------------------------
# Action Item
# ---------------------------------------------------------

class ActionItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    task: str
    owner: str | None = None
    deadline: str | None = None
    priority: Priority | None = None
    evidence: str


# ---------------------------------------------------------
# Risk
# ---------------------------------------------------------

class Risk(BaseModel):
    model_config = ConfigDict(extra="forbid")

    risk: str
    evidence: str


# ---------------------------------------------------------
# Open Question
# ---------------------------------------------------------

class OpenQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str
    owner: str | None = None
    evidence: str


# ---------------------------------------------------------
# Ambiguity
# ---------------------------------------------------------

class Ambiguity(BaseModel):
    model_config = ConfigDict(extra="forbid")

    issue: str
    why_ambiguous: str
    evidence: str


# ---------------------------------------------------------
# Main Meeting Output
# ---------------------------------------------------------

class MeetingOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    meeting_title: str | None = None

    summary: str

    decisions: list[Decision] = Field(
        default_factory=list
    )

    action_items: list[ActionItem] = Field(
        default_factory=list
    )

    risks: list[Risk] = Field(
        default_factory=list
    )

    open_questions: list[OpenQuestion] = Field(
        default_factory=list
    )

    ambiguities: list[Ambiguity] = Field(
        default_factory=list
    )

