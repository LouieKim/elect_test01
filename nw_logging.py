# configuration
DATABASE = 'ninewatt_bems.db'

#============================================
LOG_FILENAME = "ninewatt_app.log"

fmt = "%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
logFormatter = logging.Formatter(fmt)

fileLogHandler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when='midnight', interval=1, backupCount=0, encoding='utf-8', delay=False, utc=False, atTime=None)
fileLogHandler.setFormatter(logFormatter)
fileLogHandler.setLevel(logging.DEBUG)
fileLogHandler.suffix = "%Y%m%d_%H%M%S"

#stmLogHandler = logging.StreamHandler()
#stmLogHandler.setLevel(logging.DEBUG)
#stmLogHandler.setFormatter(logFormatter)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)
_LOGGER.addHandler(fileLogHandler)
#_LOGGER.addHandler(stmLogHandler)
#============================================