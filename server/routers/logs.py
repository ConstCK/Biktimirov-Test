from fastapi import APIRouter, status, Depends

from crud.logs import LogService
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
            responses={status.HTTP_200_OK: {'description': 'Успешное получение объектов'},
                       status.HTTP_422_UNPROCESSABLE_ENTITY: {'description': 'Ошибка валидации данных'}
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
            responses={status.HTTP_200_OK: {'description': 'Успешное получение объектов'},
                       status.HTTP_422_UNPROCESSABLE_ENTITY: {'description': 'Ошибка валидации данных'}}
            )
async def get_all_logs_by_user_id(user_id: int, service: LogService = Depends(),
                                  date_filter: LogFilter = Depends(LogFilter)):
    response = await service.get_logs_by_user(date_filter, tg_id=user_id)
    return response
