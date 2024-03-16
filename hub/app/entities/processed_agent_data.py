from pydantic import BaseModel
from app.entities.agent_data import AgentData
import json

# class ProcessedAgentData(BaseModel):
#     road_state: str
#     agent_data: AgentData


class ProcessedAgentData(BaseModel):
    road_state: str
    agent_data: AgentData

    @classmethod
    def parse_raw(cls, raw: str) -> "ProcessedAgentData":
        parsed_json = json.loads(raw)
        return cls(**parsed_json)
