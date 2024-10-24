from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_f390363"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']"})
product_service = CClass(service, "product-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/product/{productId}', '/set-processing-time']"})
review_service = CClass(service, "review-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/review', '/set-processing-time']"})
composite_service = CClass(service, "composite-service", stereotype_instances = [internal, local_logging, load_balancer, circuit_breaker, resource_server], tagged_values = {'Endpoints': "['/{productId}', '/']", 'Load Balancer': 'Spring Cloud'})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Endpoints': "['/']", 'Port': 7979, 'Monitoring Dashboard': 'Hystrix'})
auth_server = CClass(service, "auth-server", stereotype_instances = [authorization_server, ssl_enabled, resource_server, infrastructural], tagged_values = {'Endpoints': "['/user']", 'Authorization Server': 'Spring OAuth2', 'Port': 9999})
config_server = CClass(service, "config-server", stereotype_instances = [configuration_server, local_logging, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [monitoring_server, local_logging, infrastructural], tagged_values = {'Monitoring Server': 'Turbine', 'Port': 8989})
edge_server = CClass(service, "edge-server", stereotype_instances = [local_logging, load_balancer, gateway, resource_server, infrastructural], tagged_values = {'Port': 8765, 'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Message Broker': 'RabbitMQ', 'Port': 15672})
elasticsearch = CClass(service, "elasticsearch", stereotype_instances = [search_engine, infrastructural], tagged_values = {'Port': 9200, 'Search Engine': 'Elasticsearch'})
logstash = CClass(service, "logstash", stereotype_instances = [logging_server, infrastructural], tagged_values = {'Port': 12201, 'Logging Server': 'Logstash'})
kibana = CClass(service, "kibana", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Kibana', 'Port': 5601})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, user_stereotype, entrypoint])
add_links({config_server: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_server: product_service}, stereotype_instances = [restful_http])
add_links({config_server: review_service}, stereotype_instances = [restful_http])
add_links({config_server: composite_service}, stereotype_instances = [restful_http])
add_links({config_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: turbine_server}, stereotype_instances = [restful_http])
add_links({hystrix_dashboard: eureka}, stereotype_instances = [restful_http])
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({config_server: eureka}, stereotype_instances = [restful_http])
add_links({composite_service: eureka}, stereotype_instances = [load_balanced_link, circuit_breaker_link, restful_http], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({user: edge_server}, stereotype_instances = [restful_http])
add_links({edge_server: user}, stereotype_instances = [restful_http])
add_links({turbine_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({elasticsearch: kibana}, stereotype_instances = [restful_http])
add_links({logstash: elasticsearch}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = kibana.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()