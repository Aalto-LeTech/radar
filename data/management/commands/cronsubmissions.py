from django.core.management.base import BaseCommand
from radar.config import provider, named_function, tokenizer
from data.models import Course, Submission
import logging

logger = logging.getLogger("radar.cron")

class Command(BaseCommand):
    args = ""
    help = "Cron work for new submissions: provide, tokenize, match"

    def handle(self, *args, **options):
        for course in Course.objects.filter(archived=False):
            logger.debug("Cron tasks for course: %s" % (course))

            # TODO ensure never parallel, file lock

            # Run provider tasks.
            p_config = provider(course)
            f = named_function(p_config, "cron")
            f(course, p_config)

            # Tokenize new submissions.
            for submission in Submission.objects.filter(exercise__course=course, tokens=None):
                t_config = tokenizer(submission.exercise)
                f = named_function(t_config, "cron")
                f(submission, t_config)

                # While at it match it too.
                # TODO run match

            # Check again for yet unmatched submissions.
            for submission in Submission.objects.filter(exercise__course=Course, matching_finished=False):
              pass
