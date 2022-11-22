"""
Configure standard python logging
"""
import os
import socket
import logging.config
import platform

from eve import __version__ as eve_version
from cerberus import __version__ as cerberus_version
from werkzeug.utils import secure_filename
from utils import is_enabled


def get_configured_logger(settings, version):
    api_name = settings.get('ES_API_NAME')

    logging_config = {
        'version': 1,
        'root': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True
        },
        'formatters': {
            'simple': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detail': {
                'format': '%(asctime)s - %(levelname)s - File: %(filename)s - %(funcName)s()'
                          ' - Line: %(lineno)d -  %(message)s'
            },
            'email': {
                'format': f'%(levelname)s sent from {api_name} %(asctime)s - '
                          '%(levelname)s - File: %(filename)s - %(funcName)s() - Line: %(lineno)d -  %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            }
        }
    }

    if is_enabled(settings['ES_LOG_TO_FOLDER']):
        log_folder = f'/var/log/{secure_filename(api_name)}'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        log_handler = {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'simple',
            'when': 'midnight',
            'backupCount': 4,
        }

        logging_config['handlers']['all'] = {
            **log_handler,
            'level': 'DEBUG',
            'filename': os.path.join(log_folder, 'all.log')
        }
        logging_config['handlers']['warn'] = {
            **log_handler,
            'level': 'WARNING',
            'filename': os.path.join(log_folder, 'warn.log')
        }
        logging_config['handlers']['error'] = {
            **log_handler,
            'level': 'ERROR',
            'filename': os.path.join(log_folder, 'error.log')
        }

        logging_config['root']['handlers'] += ['all', 'warn', 'error']

    smtp_warnings = []
    if is_enabled(settings['ES_SEND_ERROR_EMAILS']):
        requires = ['ES_SMTP_HOST', 'ES_SMTP_PORT', 'ES_ERROR_EMAIL_RECIPIENTS', 'ES_ERROR_EMAIL_FROM']
        good_to_go = True
        for item in requires:
            if item not in settings:
                smtp_warnings.append(f'ES_SEND_ERROR_EMAILS is enabled, but {item} is missing - no error emails will be sent')
                good_to_go = False

        if good_to_go:
            logging_config['handlers']['smtp'] = {
                # TODO: integrate with QueueHandler so email doesn't block
                #       (look at http://flask-logconfig.readthedocs.io/en/latest/ ?)
                'class': 'logging.handlers.SMTPHandler',
                'level': 'ERROR',
                'formatter': 'email',
                'mailhost': [settings.get('ES_SMTP_HOST'), settings.get('ES_SMTP_PORT')],
                'fromaddr': settings.get('ES_ERROR_EMAIL_FROM'),
                'toaddrs': [e.strip() for e in settings.get('ES_ERROR_EMAIL_RECIPIENTS').split(',')],
                'subject': f'Problem encountered with {api_name}'
            }

            logging_config['root']['handlers'] += ['smtp']

    logging.config.dictConfig(logging_config)

    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    log = logging.getLogger('configuration')
    log.info('%s version:  %s', api_name, version)
    log.info('Eve version:      %s', eve_version)
    log.info('Cerberus version: %s', cerberus_version)
    log.info('Python version:   %s', platform.sys.version)

    if smtp_warnings:
        for warning in smtp_warnings:
            log.warning(warning)
    elif is_enabled(settings['ES_SEND_ERROR_EMAILS']):  # TODO: can this be moved up to logging_config setup?
        instance_name = settings.get('ES_INSTANCE_NAME')
        email_format = f'''%(levelname)s sent from {api_name} instance "{instance_name}" (hostname: {socket.gethostname()})

        %(asctime)s - %(levelname)s - File: %(filename)s - %(funcName)s() - Line: %(lineno)d -  %(message)s
        '''

        email_format += f'''
        {api_name} version:  {version}
        Eve version:      {eve_version}
        Cerberus version: {cerberus_version}
        Python version:   {platform.sys.version}

        '''

        for setting in sorted(settings):
            key = setting.upper()
            if ('PASSWORD' not in key) and ('SECRET' not in key):
                email_format += f'{setting}: {settings[setting]}\n'
        email_format += '\n\n'

        logger = logging.getLogger()
        handlers = logger.handlers

        smtp_handler = [x for x in handlers if x.name == 'smtp'][0]
        smtp_handler.setFormatter(logging.Formatter(email_format))

    return LOG
