# Pydantic, and Python's built-in typing are used to define a schema
# that defines the structure and types of the different objects stored
# in the recipes collection, and managed by this API.
from pydantic import BaseModel, Field
from typing import List, Optional, Union
from datetime import datetime

from objectid import PydanticObjectId

class PowerPlant(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")

    country: str
    country_long: str
    name: str
    gppd_idnr: str
    capacity_mw: str
    latitude: str
    longitude: str
    primary_fuel: str
    other_fuel1: str
    other_fuel2: str
    other_fuel3: str
    commissioning_year: str
    generation_gwh_2013: str
    generation_gwh_2014: str
    generation_gwh_2015: str
    generation_gwh_2016: str
    generation_gwh_2017: str
    generation_gwh_2018: str
    generation_gwh_2019: str
    estimated_generation_gwh_2013: str
    estimated_generation_gwh_2014: str
    estimated_generation_gwh_2015: str
    estimated_generation_gwh_2016: str
    estimated_generation_gwh_2017: str
    continent: str

    #def to_json(self):
    #    return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data