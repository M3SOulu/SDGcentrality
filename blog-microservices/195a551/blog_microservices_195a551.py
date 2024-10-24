from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_195a551"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 8080, 'Endpoints': "['/recommendation', '/set-processing-time']"})
product_service = CClass(service, "product-service", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 8080, 'Endpoints': "['/product/{productId}', '/set-processing-time']"})
review_service = CClass(service, "review-service", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 8080, 'Endpoints': "['/review', '/set-processing-time']"})
composite_service = CClass(service, "composite-service", stereotype_instances = [internal, resource_server, local_logging, load_balancer, circuit_breaker], tagged_values = {'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud', 'Endpoints': "['/', '/{productId}']"})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Port': 7979, 'Endpoints': "['/']", 'Monitoring Dashboard': 'Hystrix'})
config_server = CClass(service, "config-server", stereotype_instances = [configuration_server, local_logging, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [monitoring_server, local_logging, infrastructural], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edge_server = CClass(service, "edge-server", stereotype_instances = [local_logging, infrastructural, load_balancer, resource_server, gateway], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon', 'Port': 8765})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Port': 15672, 'Message Broker': 'RabbitMQ'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({config_server: recommendation_service}, stereotype_instances = [restful_http])
add_links({config_server: product_service}, stereotype_instances = [restful_http])
add_links({config_server: review_service}, stereotype_instances = [restful_http])
add_links({config_server: composite_service}, stereotype_instances = [restful_http])
add_links({config_server: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({config_server: turbine_server}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({config_server: eureka}, stereotype_instances = [restful_http])
add_links({composite_service: eureka}, stereotype_instances = [restful_http, load_balanced_link, circuit_breaker_link], tagged_values = {'Circuit Breaker': 'Hystrix', 'Load Balancer': 'Spring Cloud'})
add_links({hystrix_dashboard: eureka}, stereotype_instances = [restful_http])
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