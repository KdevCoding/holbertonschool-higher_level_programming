#!/usr/bin/python3
"""Generate personalised invitation files from a text template."""
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def generate_invitations(template, attendees):
    """Fill `template` once per attendee and write output_X.txt files
    """
    if not isinstance(template, str):
        logger.error("Invalid input: template must be a string, got %s.",
                     type(template).__name__)
        return

    if not isinstance(attendees, list):
        logger.error("Invalid input: attendees must be a list of "
                     "dictionaries, got %s.", type(attendees).__name__)
        return

    if not all(isinstance(person, dict) for person in attendees):
        logger.error("Invalid input: attendees must be a list of "
                     "dictionaries, but the list contains other types.")
        return

    if not template.strip():
        logger.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):
        content = template
        for key in PLACEHOLDERS:
            value = person.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)

        if os.path.exists(filename):
            logger.warning("%s already exists and will be overwritten.",
                           filename)

        try:
            with open(filename, "w", encoding="utf-8") as out_file:
                out_file.write(content)
        except OSError as exc:
            logger.error("Could not write %s: %s", filename, exc)
