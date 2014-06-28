from rest_framework.parsers import BaseParser

class Base64Parser(BaseParser):
	"""
	Base 64 Parser
	"""

	def parse(self, stream, media_type=None, parser_context=None):
		