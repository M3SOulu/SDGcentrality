from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_7e2a305"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/recommendation', '/set-processing-time']"})
product_service = CClass(service, "product-service", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/product/{productId}', '/set-processing-time']"})
review_service = CClass(service, "review-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/review', '/set-processing-time']", 'Port': 8080})
product_composite = CClass(service, "product-composite", stereotype_instances = [circuit_breaker, local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/product/{productId}', '/']", 'Circuit Breaker': 'Hystrix'})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Port': 7979, 'Endpoints': "['/']"})
configserver = CClass(service, "configserver", stereotype_instances = [infrastructural, local_logging, configuration_server], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [infrastructural, local_logging, monitoring_server], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edge_server = CClass(service, "edge-server", stereotype_instances = [infrastructural, load_balancer, gateway], tagged_values = {'Load Balancer': 'Ribbon', 'Gateway': 'Zuul', 'Port': 8765})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
productapi = CClass(service, "productapi", stereotype_instances = [circuit_breaker, resource_server, local_logging, internal], tagged_values = {'Endpoints': "['/{productId}']", 'Circuit Breaker': 'Hystrix'})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [infrastructural, message_broker], tagged_values = {'Port': 5672, 'Message Broker': 'RabbitMQ'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, user_stereotype, entrypoint])
add_links({configserver: recommendation_service}, stereotype_instances = [restful_http])
add_links({configserver: product_service}, stereotype_instances = [restful_http])
add_links({configserver: review_service}, stereotype_instances = [restful_http])
add_links({configserver: product_composite}, stereotype_instances = [restful_http])
add_links({configserver: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({configserver: turbine_server}, stereotype_instances = [restful_http])
add_links({configserver: edge_server}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({config: rabbitmq}, stereotype_instances = [restful_http])
add_links({pro: rabbitmq}, stereotype_instances = [restful_http])
add_links({rec: rabbitmq}, stereotype_instances = [restful_http])
add_links({rev: rabbitmq}, stereotype_instances = [restful_http])
add_links({composite: rabbitmq}, stereotype_instances = [restful_http])
add_links({api: rabbitmq}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({product_composite: eureka}, stereotype_instances = [circuit_breaker_link, restful_http], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({hystrix_dashboard: eureka}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [circuit_breaker_link, restful_http], tagged_values = {'Circuit Breaker': 'Hystrix'})
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