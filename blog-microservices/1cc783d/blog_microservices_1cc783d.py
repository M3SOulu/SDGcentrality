from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_1cc783d"
recommendation_service = CClass(service, "recommendation-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']", 'Port': 8080})
product_service = CClass(service, "product-service", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/product/{productId}', '/set-processing-time']", 'Port': 8080})
review_service = CClass(service, "review-service", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/review', '/set-processing-time']"})
product_composite = CClass(service, "product-composite", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Port': 8080, 'Circuit Breaker': 'Hystrix', 'Endpoints': "['/product/{productId}', '/']"})
hystrix_dashboard = CClass(service, "hystrix-dashboard", stereotype_instances = [infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Port': 7979, 'Endpoints': "['/']"})
configserver = CClass(service, "configserver", stereotype_instances = [configuration_server, local_logging, infrastructural], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
turbine_server = CClass(service, "turbine-server", stereotype_instances = [infrastructural, local_logging, monitoring_server], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edge_server = CClass(service, "edge-server", stereotype_instances = [infrastructural, gateway, load_balancer], tagged_values = {'Load Balancer': 'Ribbon', 'Port': 8765, 'Gateway': 'Zuul'})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka', 'Port': 8762})
productapi = CClass(service, "productapi", stereotype_instances = [resource_server, local_logging, circuit_breaker, internal], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/{productId}']"})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [infrastructural, message_broker], tagged_values = {'Port': 5672, 'Message Broker': 'RabbitMQ'})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({configserver: recommendation_service}, stereotype_instances = [restful_http])
add_links({configserver: product_service}, stereotype_instances = [restful_http])
add_links({configserver: review_service}, stereotype_instances = [restful_http])
add_links({configserver: product_composite}, stereotype_instances = [restful_http])
add_links({configserver: hystrix_dashboard}, stereotype_instances = [restful_http])
add_links({configserver: turbine_server}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({config: rabbitmq}, stereotype_instances = [restful_http])
add_links({pro: rabbitmq}, stereotype_instances = [restful_http])
add_links({rec: rabbitmq}, stereotype_instances = [restful_http])
add_links({rev: rabbitmq}, stereotype_instances = [restful_http])
add_links({composite: rabbitmq}, stereotype_instances = [restful_http])
add_links({api: rabbitmq}, stereotype_instances = [restful_http])
add_links({product_service: eureka}, stereotype_instances = [restful_http])
add_links({product_composite: eureka}, stereotype_instances = [restful_http, circuit_breaker_link], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({turbine_server: eureka}, stereotype_instances = [restful_http])
add_links({review_service: eureka}, stereotype_instances = [restful_http])
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({recommendation_service: eureka}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [restful_http, circuit_breaker_link], tagged_values = {'Circuit Breaker': 'Hystrix'})
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