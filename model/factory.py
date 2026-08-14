from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models.tongyi import ChatTongyi
from utils.config_handler import rag_conf


class BaseModelFactory(ABC):
    @staticmethod
    @abstractmethod
    def generator()->Optional[Embeddings | BaseChatModel]:
        pass



class ChatModelFactory(BaseModelFactory):
        @staticmethod
        def generator()->Optional[Embeddings | BaseChatModel]:
            return ChatTongyi(model=rag_conf["chat_model_name"])


class EmbeddingsFactory(BaseModelFactory):
    @staticmethod
    def generator() -> Optional[Embeddings | BaseChatModel]:
        return DashScopeEmbeddings(model=rag_conf["embedding_model_name"])


chat_model = ChatModelFactory.generator()
embd_model = EmbeddingsFactory.generator()