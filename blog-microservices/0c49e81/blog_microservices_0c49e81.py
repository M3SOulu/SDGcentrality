from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_0c49e81"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 8080, 'Endpoints': "['/set-processing-time', '/recommendation']"})
product_service = CClass(service, "product-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/set-processing-time', '/product/{productId}']", 'Port': 8080})
review_service = CClass(service, "review-service", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/set-processing-time', '/review']", 'Port': 8080})
composite_service = CClass(service, "composite-service", stereotype_instances = [internal, circuit_breaker, resource_server, local_logging], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/', '/{productId}']"})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Port': 7979, 'Endpoints': "['/']"})
configserver = CClass(service, "configserver", stereotype_instances = [infrastructural, configuration_server, local_logging], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [infrastructural, monitoring_server, local_logging], tagged_values = {'Monitoring Server': 'Turbine', 'Port': 8989})
edge_server = CClass(service, "edge-server", stereotype_instances = [gateway, load_balancer, infrastructural], tagged_values = {'Port': 8765, 'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
productapi = CClass(service, "productapi", stereotype_instances = [internal, circuit_breaker, resource_server, local_logging], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/{productId}']"})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [infrastructural, message_broker], tagged_values = {'Port': 5672, 'Message Broker': 'RabbitMQ'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({configserver: recommendation_service}, stereotype_instances = [restful_http])
add_links({configserver: product_service}, stereotype_instances = [restful_http])
add_links({configserver: review_service}, stereotype_instances = [restful_http])
add_links({configserver: composite_service}, stereotype_instances = [restful_http])
add_links({configserver: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({configserver: turbine_server}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({config: rabbitmq}, stereotype_instances = [restful_http])
add_links({pro: rabbitmq}, stereotype_instances = [restful_http])
add_links({rec: rabbitmq}, stereotype_instances = [restful_http])
add_links({rev: rabbitmq}, stereotype_instances = [restful_http])
add_links({composite: rabbitmq}, stereotype_instances = [restful_http])
add_links({hystrix_dashboard: eureka}, stereotype_instances = [restful_http])
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({composite_service: eureka}, stereotype_instances = [restful_http, circuit_breaker_link], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [restful_http, circuit_breaker_link], tagged_values = {'Circuit Breaker': 'Hystrix'})
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