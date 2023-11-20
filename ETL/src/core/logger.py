# Extra libraries imports
import structlog
import logging.config
from dateutil import parser
from datetime import timedelta, timezone


def __convert_to_desired_timezone(_, __, event_dict):
    '''
    ### Função para modificar o logger da biblioteca structlog conforme horário e data atual da execução.
    '''

    # Obtém o timestamp atual em UTC como string
    utc_timestamp_str = event_dict.get('timestamp')

    # Substitui o ponto pelo dois pontos no timestamp
    utc_timestamp_str = utc_timestamp_str.replace('.', ':')

    # Converte o timestamp para um objeto datetime
    utc_timestamp = parser.isoparse(utc_timestamp_str)

    # Converte o timestamp para UTC-3 (ou qualquer outro fuso horário desejado)
    desired_timezone = timezone(timedelta(hours=-3))

    # Tira o timezone para -03:00 e retorna o timestamp %Y-%m-%d %H:%M.%S-03:00
    event_dict['timestamp'] = utc_timestamp.astimezone(desired_timezone).isoformat(" ", "seconds")

    # Tira o -03:00 do timestamp
    event_dict['timestamp'] = event_dict['timestamp'].split('-03')[0]

    return event_dict


def json_logger():
    '''
    # JSON logger

    #### Esta função retorna um logger JSON.

    Ex.: {"event": "message event", "level": "log level"}
    '''

    structlog.configure(processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.JSONRenderer(),
    ])

    return structlog.get_logger()


def logger(color: bool = True):
    '''
    # Logger

    #### Esta função retorna um logger.

    Ex.: YYYY-MM-DD hh:mm:ss [LOG_LEVEL     ] 

    - COLOR: Se TRUE ele gera os logs de execução coloridos para melhor visualização no terminal.
    Se FALSE ele gera os logs de execução sem cor para geração de arquivo de logs sem erros.
    '''

    structlog.configure(processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S", utc=False),
        __convert_to_desired_timezone,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.ConsoleRenderer(colors=color) # Setar como False para salvar logs.
        ])

    return structlog.get_logger()


def log_file():
    '''
    # Logger com arquivo

    #### Esta função retorna os logs em arquivo .log.

    Ex.: YYYY-MM-DD hh:mm:ss [LOG_LEVEL     ] INFORMAÇÕES DE LOG
    '''

    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "default": {
                "level": "INFO",
                "class": "logging.StreamHandler",
            },
            "file": {
                "level": "INFO",
                "class": "logging.handlers.WatchedFileHandler",
                "filename": "test.log",
                "encoding": "utf-8"  # Define a codificação como UTF-8
            },
        },
        "loggers": {
            "": {
                "handlers": ["default", "file"],
                "level": "INFO",
                "propagate": True,
            },
        }
    })

    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S", utc=False),
            __convert_to_desired_timezone,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True
    )

    return structlog.get_logger()