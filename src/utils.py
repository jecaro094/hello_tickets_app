import logging
from logging import Logger
from src.constants import LOGGER_FORMAT_MSG
from src.requests import HelloTicketsAPIClient

logging.basicConfig(
    level=logging.INFO,
    format=LOGGER_FORMAT_MSG,
)

def get_logger(file_name: str) -> Logger:
    """
    Retrieves basic logger given file name
    """
    return logging.getLogger(file_name)


def get_data_from_hello_tickets(
    api_client: HelloTicketsAPIClient,
    endpoint: str,
    logger: Logger,
    params: None | dict = None
) -> dict:
    """"""
    # TODO Consider error handling here too... Raise custom exceptions, etc...
    response = api_client.get(
        path=endpoint,
        params=params
    )
    if response.ok:
        response_raw = response.json() if bool(response.content) else {}
        logger.info(f"Response for endpoint {endpoint}: {response_raw}")
        return response_raw
    else:
        logger.info("Could not retrieve info, returning empty json...")
        return {}
