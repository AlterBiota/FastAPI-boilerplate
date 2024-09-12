from fastcrud import FastCRUD

from ..models.client import Tier
from ..schemas.client import TierCreateInternal, TierDelete, TierUpdate, TierUpdateInternal

CRUDTier = FastCRUD[Tier, TierCreateInternal, TierUpdate, TierUpdateInternal, TierDelete]
crud_tiers = CRUDTier(Tier)
