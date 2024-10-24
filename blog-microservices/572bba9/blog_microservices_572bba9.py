from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_572bba9"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']"})
product_service = CClass(service, "product-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/set-processing-time', '/product/{productId}']"})
review_service = CClass(service, "review-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/review', '/set-processing-time']"})
composite_service = CClass(service, "composite-service", stereotype_instances = [resource_server, local_logging, load_balancer, circuit_breaker, internal], tagged_values = {'Load Balancer': 'Spring Cloud', 'Endpoints': "['/', '/{productId}']"})
monitor_dashboard = CClass(service, "monitor-dashboard", stereotype_instances = [monitoring_dashboard, local_logging, infrastructural], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Endpoints': "['/']"})
auth_server = CClass(service, "auth-server", stereotype_instances = [authorization_server, resource_server, infrastructural, local_logging], tagged_values = {'Endpoints': "['/user']", 'Authorization Server': 'Spring OAuth2'})
config_server = CClass(service, "config-server", stereotype_instances = [local_logging, infrastructural, configuration_server], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [local_logging, infrastructural, monitoring_server], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
zipkin_server = CClass(service, "zipkin-server", stereotype_instances = [internal], tagged_values = {'Port': 9411})
edge_server = CClass(service, "edge-server", stereotype_instances = [resource_server, local_logging, infrastructural, load_balancer, gateway], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
discovery_server = CClass(service, "discovery-server", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
elasticsearch = CClass(service, "elasticsearch", stereotype_instances = [search_engine, infrastructural], tagged_values = {'Search Engine': 'Elasticsearch', 'Port': 9200})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Message Broker': 'RabbitMQ', 'Port': 15672})
kibana = CClass(service, "kibana", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Port': 5601, 'Monitoring Dashboard': 'Kibana'})
logstash = CClass(service, "logstash", stereotype_instances = [logging_server, infrastructural], tagged_values = {'Logging Server': 'Logstash', 'Port': 12201})
zipkin = CClass(service, "zipkin", stereotype_instances = [internal], tagged_values = {'Port': 9411})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({config_server: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_server: product_service}, stereotype_instances = [restful_http])
add_links({config_server: review_service}, stereotype_instances = [restful_http])
add_links({config_server: composite_service}, stereotype_instances = [restful_http])
add_links({config_server: monitor_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: auth_server}, stereotype_instances = [restful_http])
add_links({config_server: turbine_server}, stereotype_instances = [restful_http])
add_links({config_server: edge_server}, stereotype_instances = [restful_http])
add_links({turbine_server: discovery_server}, stereotype_instances = [restful_http])
add_links({product_service: discovery_server}, stereotype_instances = [restful_http])
add_links({recommendation_service: discovery_server}, stereotype_instances = [restful_http])
add_links({composite_service: discovery_server}, stereotype_instances = [restful_http, load_balanced_link, circuit_breaker_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({config_server: discovery_server}, stereotype_instances = [restful_http])
add_links({review_service: discovery_server}, stereotype_instances = [restful_http])
add_links({user: edge_server}, stereotype_instances = [restful_http])
add_links({edge_server: user}, stereotype_instances = [restful_http])
add_links({turbine_server: monitor_dashboard}, stereotype_instances = [restful_http])
add_links({elasticsearch: kibana}, stereotype_instances = [restful_http])
add_links({logstash: elasticsearch}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = zipkin.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()