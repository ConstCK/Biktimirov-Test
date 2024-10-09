from fastapi import APIRouter, status, Depends, Response

from crud.logs import LogService
from fastapi_filter import FilterDepends
from fastapi_pagination import Page

from schemas.logs import Log

from filters.logs import LogFilter

# Создание маршрута
router = APIRouter(prefix='/api/v1/logs')


# Маршрут для получения всех логов
@router.get('/', description='Получение всех логов',
            summary='Получение логов указанного пользователя',
            response_model=Page[Log],
            status_code=status.HTTP_200_OK, name='get_all_logs_url',
            responses={200: {'description': 'Успешное получение объектов'},
                       }
            )
async def get_all_logs(service: LogService = Depends(),
                       date_filter: LogFilter = Depends(LogFilter)):
    response = await service.get_logs(date_filter)
    return response


# Маршрут для получения логов по принадлежности пользователю
@router.get('/{user_id}/', description='Получение всех логов по id пользователя',
            summary='Получение логов указанного пользователя',
            response_model=Page[Log],
            status_code=status.HTTP_200_OK, name='get_logs_url_by_user_id',
            responses={200: {'description': 'Успешное получение объектов'}, }
            )
async def get_all_logs_by_user_id(user_id: int, service: LogService = Depends()):
    response = await service.get_logs_by_user(tg_id=user_id)
    return response
