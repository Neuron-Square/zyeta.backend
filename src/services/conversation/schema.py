from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ConversationBase(BaseModel):
  """Base conversation schema."""

  title: str = Field(..., min_length=1, max_length=255)
  description: Optional[str] = None
  is_archived: bool = False


class ConversationCreate(ConversationBase):
  """Create conversation schema."""

  pass


class ConversationUpdate(BaseModel):
  """Update conversation schema."""

  title: Optional[str] = Field(None, min_length=1, max_length=255)
  description: Optional[str] = None
  is_archived: Optional[bool] = None


class ConversationResponse(ConversationBase):
  """Conversation response schema."""

  id: UUID
  organization_id: UUID
  user_id: UUID
  created_at: datetime

  class Config:
    from_attributes = True


class ChatSessionCreate(BaseModel):
  """Create chat session schema."""

  conversation_id: UUID
  agent_id: Optional[UUID] = None
  model_id: UUID
  settings: Dict = Field(default_factory=dict)


class ChatSessionResponse(BaseModel):
  """Chat session response schema."""

  id: UUID
  conversation_id: UUID
  agent_id: Optional[UUID]
  model_id: UUID
  status: str
  settings: Dict
  created_at: datetime

  class Config:
    from_attributes = True


class ChatMessageCreate(BaseModel):
  """Create chat message schema."""

  chat_session_id: UUID
  message: str


class MessageResponse(BaseModel):
  """Message response schema."""

  id: UUID
  chat_session_id: UUID
  role: str
  content: str
  token_used: Optional[int]
  created_at: datetime

  class Config:
    from_attributes = True


class ChatSessionDetailResponse(ChatSessionResponse):
  """Chat session response with model and agent names."""

  model_name: Optional[str]
  agent_name: Optional[str]


class ConversationWithSessionsResponse(ConversationResponse):
  """Conversation response with detailed chat sessions."""

  chat_sessions: List[ChatSessionDetailResponse]

  class Config:
    from_attributes = True


class MessageWithDetailsResponse(MessageResponse):
  """Message response with model and agent details."""

  model_id: Optional[UUID]
  model_name: Optional[str]
  agent_id: Optional[UUID]
  agent_name: Optional[str]


class PaginatedMessagesResponse(BaseModel):
  """Paginated messages response."""

  messages: List[MessageWithDetailsResponse]
  total: int
  has_more: bool
