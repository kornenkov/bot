from pydantic import BaseModel


class Apps(BaseModel):
    poizon: str
    fenapp: str
    taobao: str
    pinduoduo: str
