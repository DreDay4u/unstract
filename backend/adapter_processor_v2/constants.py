from enum import Enum


class AdapterKeys:
    JSON_SCHEMA = "json_schema"
    ADAPTER_TYPE = "adapter_type"
    IS_DEFAULT = "is_default"
    LLM = "LLM"
    X2TEXT = "X2TEXT"
    OCR = "OCR"
    VECTOR_DB = "VECTOR_DB"
    EMBEDDING = "EMBEDDING"
    NAME = "name"
    DESCRIPTION = "description"
    ICON = "icon"
    ADAPTER_ID = "adapter_id"
    ADAPTER_METADATA = "adapter_metadata"
    ADAPTER_METADATA_B = "adapter_metadata_b"
    ID = "id"
    IS_VALID = "is_valid"
    LLM_DEFAULT = "llm_default"
    VECTOR_DB_DEFAULT = "vector_db_default"
    EMBEDDING_DEFAULT = "embedding_default"
    X2TEXT_DEFAULT = "x2text_default"
    SHARED_USERS = "shared_users"
    ADAPTER_NAME_EXISTS = (
        "Configuration with this name already exists within your organisation."
        "Please try with a different name."
    )
    ADAPTER_NAME = "adapter_name"
    ADAPTER_CREATED_BY = "created_by_email"
    ADAPTER_CONTEXT_WINDOW_SIZE = "context_window_size"
    PLATFORM_PROVIDED_UNSTRACT_KEY = "use_platform_provided_unstract_key"


class AllowedDomains(Enum):
    ZIPSTACK = "@zipstack.com"
    UNSTRACT = "@unstract.com"

    @staticmethod
    def list():
        return list(map(lambda c: c.value, AllowedDomains))
