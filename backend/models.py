from pydantic import BaseModel
from typing import List, Optional

class Pharmacy(BaseModel):
    name: str
    district: str
    neighborhood: str
    address: str
    phone: str
    lat: Optional[float] = None
    lng: Optional[float] = None

class PharmacyResponse(BaseModel):
    city: str
    date: str
    pharmacies: List[Pharmacy]
