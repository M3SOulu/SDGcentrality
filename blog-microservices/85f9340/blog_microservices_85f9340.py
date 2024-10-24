from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_85f9340"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']"})
product_service = CClass(service, "product-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/product/{productId}', '/set-processing-time']"})
review_service = CClass(service, "review-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/review', '/set-processing-time']"})
composite_service = CClass(service, "composite-service", stereotype_instances = [load_balancer, circuit_breaker, internal, resource_server, local_logging], tagged_values = {'Endpoints': "['/', '/{productId}']", 'Load Balancer': 'Spring Cloud'})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Endpoints': "['/']", 'Port': 7979, 'Monitoring Dashboard': 'Hystrix'})
auth_server = CClass(service, "auth-server", stereotype_instances = [ssl_enabled, resource_server, infrastructural, authorization_server], tagged_values = {'Authorization Server': 'Spring OAuth2', 'Port': 9999, 'Endpoints': "['/user']"})
config_server = CClass(service, "config-server", stereotype_instances = [configuration_server, infrastructural, local_logging], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [monitoring_server, infrastructural, local_logging], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edge_server = CClass(service, "edge-server", stereotype_instances = [load_balancer, resource_server, gateway, infrastructural, local_logging], tagged_values = {'Port': 8765, 'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
logstash = CClass(service, "logstash", stereotype_instances = [logging_server, infrastructural], tagged_values = {'Port': 12201, 'Logging Server': 'Logstash'})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Port': 15672, 'Message Broker': 'RabbitMQ'})
kibana = CClass(service, "kibana", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Kibana', 'Port': 5601})
elasticsearch = CClass(service, "elasticsearch", stereotype_instances = [search_engine, infrastructural], tagged_values = {'Port': 9200, 'Search Engine': 'Elasticsearch'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({config_server: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_server: product_service}, stereotype_instances = [restful_http])
add_links({config_server: review_service}, stereotype_instances = [restful_http])
add_links({config_server: composite_service}, stereotype_instances = [restful_http])
add_links({config_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: turbine_server}, stereotype_instances = [restful_http])
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({config_server: eureka}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({hystrix_dashboard: eureka}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({composite_service: eureka}, stereotype_instances = [load_balanced_link, restful_http, circuit_breaker_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({user: edge_server}, stereotype_instances = [restful_http])
add_links({edge_server: user}, stereotype_instances = [restful_http])
add_links({turbine_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({elasticsearch: kibana}, stereotype_instances = [restful_http])
add_links({logstash: elasticsearch}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = elasticsearch.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()