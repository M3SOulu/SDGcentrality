from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_6a25173"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']"})
product_service = CClass(service, "product-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/product/{productId}', '/set-processing-time']"})
review_service = CClass(service, "review-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/review', '/set-processing-time']"})
composite_service = CClass(service, "composite-service", stereotype_instances = [circuit_breaker, resource_server, local_logging, load_balancer, internal], tagged_values = {'Load Balancer': 'Spring Cloud', 'Endpoints': "['/{productId}', '/']"})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Endpoints': "['/']", 'Monitoring Dashboard': 'Hystrix', 'Port': 7979})
config_server = CClass(service, "config-server", stereotype_instances = [configuration_server, local_logging, infrastructural], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [local_logging, monitoring_server, infrastructural], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edge_server = CClass(service, "edge-server", stereotype_instances = [infrastructural, gateway, resource_server, local_logging, load_balancer], tagged_values = {'Port': 8765, 'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka', 'Port': 8762})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Port': 15672, 'Message Broker': 'RabbitMQ'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({config_server: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_server: product_service}, stereotype_instances = [restful_http])
add_links({config_server: review_service}, stereotype_instances = [restful_http])
add_links({config_server: composite_service}, stereotype_instances = [restful_http])
add_links({config_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: turbine_server}, stereotype_instances = [restful_http])
add_links({config_server: eureka}, stereotype_instances = [restful_http])
add_links({hystrix_dashboard: eureka}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({composite_service: eureka}, stereotype_instances = [circuit_breaker_link, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Spring Cloud'})
add_links({user: edge_server}, stereotype_instances = [restful_http])
add_links({edge_server: user}, stereotype_instances = [restful_http])
add_links({turbine_server: hystrix_dashboard}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = rabbitmq.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()