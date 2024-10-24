from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_ed256a5"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/set-processing-time', '/recommendation']"})
product_service = CClass(service, "product-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/set-processing-time', '/product/{productId}']"})
review_service = CClass(service, "review-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/set-processing-time', '/review']"})
composite_service = CClass(service, "composite-service", stereotype_instances = [internal, local_logging, circuit_breaker, load_balancer, resource_server], tagged_values = {'Load Balancer': 'Spring Cloud', 'Endpoints': "['/{productId}', '/']"})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Endpoints': "['/']", 'Port': 7979})
auth_server = CClass(service, "auth-server", stereotype_instances = [infrastructural, authorization_server, ssl_enabled, resource_server], tagged_values = {'Authorization Server': 'Spring OAuth2', 'Endpoints': "['/user']", 'Port': 9999})
config_server = CClass(service, "config-server", stereotype_instances = [infrastructural, configuration_server, local_logging], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [infrastructural, local_logging, monitoring_server], tagged_values = {'Monitoring Server': 'Turbine', 'Port': 8989})
edge_server = CClass(service, "edge-server", stereotype_instances = [infrastructural, local_logging, load_balancer, gateway, resource_server], tagged_values = {'Port': 8765, 'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [infrastructural, message_broker], tagged_values = {'Message Broker': 'RabbitMQ', 'Port': 15672})
elasticsearch = CClass(service, "elasticsearch", stereotype_instances = [infrastructural, search_engine], tagged_values = {'Search Engine': 'Elasticsearch', 'Port': 9200})
kibana = CClass(service, "kibana", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Port': 5601, 'Monitoring Dashboard': 'Kibana'})
logstash = CClass(service, "logstash", stereotype_instances = [infrastructural, logging_server], tagged_values = {'Port': 12201, 'Logging Server': 'Logstash'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, exitpoint, user_stereotype])
add_links({config_server: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_server: product_service}, stereotype_instances = [restful_http])
add_links({config_server: review_service}, stereotype_instances = [restful_http])
add_links({config_server: composite_service}, stereotype_instances = [restful_http])
add_links({config_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: turbine_server}, stereotype_instances = [restful_http])
add_links({config_server: eureka}, stereotype_instances = [restful_http])
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({hystrix_dashboard: eureka}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({composite_service: eureka}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({user: edge_server}, stereotype_instances = [restful_http])
add_links({edge_server: user}, stereotype_instances = [restful_http])
add_links({turbine_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({elasticsearch: kibana}, stereotype_instances = [restful_http])
add_links({logstash: elasticsearch}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = logstash.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()