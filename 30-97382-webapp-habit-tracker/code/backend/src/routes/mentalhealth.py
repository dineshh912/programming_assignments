from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.mentalhealth as crud
from src.auth.jwthandler import get_current_user
from src.schemas.mentalhealth import MentalhealthOutSchema, MentalhealthInSchema, UpdateMentalhealth
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/mh",
    response_model=List[MentalhealthOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_all_mentalhealth():
    return await crud.get_all_mentalhealth()


@router.get(
    "/mh/{mh_id}",
    response_model=MentalhealthOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_mentalhealth(mh_id: int) -> MentalhealthOutSchema:
    try:
        return await crud.get_mentalhealth(mh_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="MH does not exist",
        )


@router.post(
    "/mh", response_model=MentalhealthOutSchema, 
    dependencies=[Depends(get_current_user)]
)
async def create_mh(
    mh: MentalhealthInSchema,
    current_user: UserOutSchema = Depends(get_current_user)
) -> MentalhealthOutSchema:
    return await crud.create_mh(mh, current_user)


@router.patch(
    "/mh/{mh_id}",
    dependencies=[Depends(get_current_user)],
    response_model=MentalhealthOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_mh(
    mh_id: int,
    mh: UpdateMentalhealth,
    current_user: UserOutSchema = Depends(get_current_user),
) -> MentalhealthOutSchema:
    return await crud.update_mh(mh_id, mh, current_user)


@router.delete(
    "/mh/{mh_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_mh(
    mh_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_mh(mh_id, current_user)