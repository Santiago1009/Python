"""Loggings"""
import logging
import sys

# We can obtain our logger object using the getLogger(name) method

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stream_handler)
