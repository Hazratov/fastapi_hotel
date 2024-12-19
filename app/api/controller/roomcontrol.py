from fastapi import Depends

from app.api.repesitories.roomRep import RoomsRepository


class RoomsController:
    def __init__(
            self,
            rooms_repo: RoomsRepository = Depends()
    ):
        self.__rooms_repo = rooms_repo
    

    async def get_rooms(self):
        return await self.__rooms_repo.get_all_rooms()
    
    async def get_room_by_id(self, room_id: int):
        return await self.__rooms_repo.get_room_by_id(room_id)