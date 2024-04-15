from nameko.testing.services import worker_factory
from Service import ServiceRegistration ,WebServer

def test_ServiceRegistration():
    serviceregistration = worker_factory(ServiceRegistration)
    
    result = serviceregistration.get_name()
    assert result == 'Service'
    
    result = serviceregistration.get_version()
    assert result == '1.0.0'
    
    result = serviceregistration.get_doc()
    assert result == 'Service'
    
    
    
def test_root_http(web_session, web_config, container_factory):
    web_config['AMQP_URI'] = 'pyamqp://guest:guest@localhost'

    web_server = container_factory(WebServer, web_config)
    serviceregistration = container_factory(ServiceRegistration, web_config)
    web_server.start()
    serviceregistration.start()

    result = web_session.get('/')
    assert result.text == 'Konnichiwa!'

