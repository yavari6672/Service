'''Service'''
from nameko.rpc import rpc, RpcProxy
from nameko.web.handlers import http

service_name = 'Service'
service_version = '1.0.0'


class ServiceRegistration:
	name = "ServiceRegistration"
	
	@rpc
	def get_name(self):
		return service_name

	@rpc
	def get_version(self):
		return service_version

	@rpc
	def get_doc(self):
		return __doc__


class WebServer:
    name = 'web_server'
    ServiceRegistration = RpcProxy('ServiceRegistration')

    @http('GET', '/')
    def home(self, request):
        return f''' service_name: {self.ServiceRegistration.get_name()}({self.ServiceRegistration.get_version()}) - {self.ServiceRegistration.get_doc()} '''


