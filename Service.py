'''This module is for service registration'''
from .LoggerService import service_name , service_version
from nameko.rpc import rpc, RpcProxy


class ServiceRegistration:
	name = "ServiceRegistration"
	
	@rpc
	def get_name(self):
		return service_name
