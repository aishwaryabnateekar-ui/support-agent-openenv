from pydantic import BaseModel

class Observation(BaseModel):
    ticket: str

class Action(BaseModel):
    action_type: str
    content: str

class State(BaseModel):
    ticket: str
    steps: int
    resolved: bool
