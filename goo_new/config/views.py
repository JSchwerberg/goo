from .models import Config

def get_config():
	queryset = Config.objects.all()
	config = {}
	for obj in queryset:
		config[obj.key] = obj.value

	return config