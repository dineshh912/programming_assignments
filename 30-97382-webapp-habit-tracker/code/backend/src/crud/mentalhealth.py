from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Mentalhealth
from src.schemas.mentalhealth import MentalhealthOutSchema
from src.schemas.token import Status

# Get all data
async def get_all_mentalhealth():
    return await MentalhealthOutSchema.from_queryset(Mentalhealth.all())

# Get single data based on id
async def get_mentalhealth(mh_id) -> MentalhealthOutSchema:
    return await MentalhealthOutSchema.from_queryset_single(Mentalhealth.get(id=mh_id))

# adding new entry
async def create_mh(mh, current_user) -> MentalhealthOutSchema:
    # Processing form input
    mh_dict = mh.dict(exclude_unset=True)
    # adding user 
    mh_dict["added_by_id"] = current_user.id
    mh_obj = await Mentalhealth.create(**mh_dict)
    return await MentalhealthOutSchema.from_tortoise_orm(mh_obj)

# update mh
async def update_mh(mh_id, mh, current_user) -> MentalhealthOutSchema:
    # Retrive the specific mh present in the db
    try:
        db_mh = await MentalhealthOutSchema.from_queryset_single(Mentalhealth.get(id=mh_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"info on {mh_id} not found")
    # if the entry belongs to the user added into db
    if db_mh.added_by.id == current_user.id:
        await Mentalhealth.filter(id=mh_id).update(**mh.dict(exclude_unset=True))
        return await MentalhealthOutSchema.from_queryset_single(Mentalhealth.get(id=mh_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")

# Delete entry
async def delete_mh(mh_id, current_user) -> Status:
    # Checking if entry available
    try:
        db_mh = await MentalhealthOutSchema.from_queryset_single(Mentalhealth.get(id=mh_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Info on {mh_id} not found")
    # If the entry belongs to current users
    if db_mh.added_by.id == current_user.id:
        deleted_count = await Mentalhealth.filter(id=mh_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Info on {mh_id} not found")
        return Status(message=f"Deleted Entry {mh_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
