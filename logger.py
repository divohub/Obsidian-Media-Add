import logging
import sys


def setup_logger(name: str = 'log', log_file: str = 'script.log') -> logging.Logger:
    """
    Настройка логгера.

    :param name: Имя логгера.
    :param log_file: Имя файла для записи логов.
    :return: Настроенный логгер.
    """
    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логгера на DEBUG

    # Создаем форматтер с указанием кодировки UTF-8
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Создаем обработчик для вывода в консоль с поддержкой UTF-8
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    # Принудительно устанавливаем кодировку UTF-8 для вывода в консоль
    if sys.stdout.encoding != 'UTF-8':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Создаем обработчик для записи в файл с указанием кодировки UTF-8
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Добавляем обработчики к логгеру
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger