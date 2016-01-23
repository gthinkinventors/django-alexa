from __future__ import absolute_import
from ..base import AlexaBaseCommand


class Command(AlexaBaseCommand):
    help = 'Prints the Alexa Skills Kit utterances schema'

    def do_work(self, app):
        data = IntentsSchema.generate_utterances(app=app)
        self.stdout.write('\n'.join(data))
