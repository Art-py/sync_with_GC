import logging


class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        from logs.models import LogEntry
        log_entry = LogEntry(
            level=record.levelname,
            message=self.format(record),
            logger=record.name
        )
        log_entry.save()
