class LoginBackend:
	def authenticate(self, username=None, password=None):
		try:
			user = Sponsor.objects.get(username=username)
		except Exception, e:
			return None
		return user