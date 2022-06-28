import logging
import sys

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s'"

logging.basicConfig(filename = "logfile.log",
                    stream = sys.stdout, 
                    filemode = "w",
                    format = log_format, 
                    level = logging.DEBUG)

logger = logging.getLogger().debug('logger installed')