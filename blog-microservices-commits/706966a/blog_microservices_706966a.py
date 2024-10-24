from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_706966a"
recommendation = CClass(service, "recommendation", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']", 'Port': 8080})
product = CClass(service, "product", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/set-processing-time', '/product/{productId}']"})
review = CClass(service, "review", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/set-processing-time', '/review']", 'Port': 8080})
productcomposite = CClass(service, "productcomposite", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Endpoints': "['/product/{productId}', '/']", 'Port': 8080, 'Circuit Breaker': 'Hystrix'})
hystrixdashboard = CClass(service, "hystrixdashboard", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Endpoints': "['/']", 'Monitoring Dashboard': 'Hystrix', 'Port': 7979})
configserver = CClass(service, "configserver", stereotype_instances = [configuration_server, local_logging, infrastructural], tagged_values = {'Port': 8888, 'Configuration Server': 'Spring Cloud Config'})
turbine = CClass(service, "turbine", stereotype_instances = [monitoring_server, local_logging, infrastructural], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edgeserver = CClass(service, "edgeserver", stereotype_instances = [load_balancer, infrastructural, gateway], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon', 'Port': 8765})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka', 'Port': 8762})
productapi = CClass(service, "productapi", stereotype_instances = [local_logging, resource_server, circuit_breaker, internal], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/{productId}']"})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [infrastructural, message_broker], tagged_values = {'Message Broker': 'RabbitMQ', 'Port': 5672})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, exitpoint, user_stereotype])
add_links({configserver: recommendation}, stereotype_instances = [restful_http])
add_links({configserver: product}, stereotype_instances = [restful_http])
add_links({configserver: review}, stereotype_instances = [restful_http])
add_links({configserver: productcomposite}, stereotype_instances = [restful_http])
add_links({configserver: hystrixdashboard}, stereotype_instances = [restful_http])
add_links({configserver: turbine}, stereotype_instances = [restful_http])
add_links({configserver: edgeserver}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({config: rabbitmq}, stereotype_instances = [restful_http])
add_links({pro: rabbitmq}, stereotype_instances = [restful_http])
add_links({rec: rabbitmq}, stereotype_instances = [restful_http])
add_links({rev: rabbitmq}, stereotype_instances = [restful_http])
add_links({composite: rabbitmq}, stereotype_instances = [restful_http])
add_links({api: rabbitmq}, stereotype_instances = [restful_http])
add_links({productcomposite: eureka}, stereotype_instances = [circuit_breaker_link, restful_http], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({recommendation: eureka}, stereotype_instances = [restful_http])
add_links({turbine: eureka}, stereotype_instances = [restful_http])
add_links({product: eureka}, stereotype_instances = [restful_http])
add_links({review: eureka}, stereotype_instances = [restful_http])
add_links({hystrixdashboard: eureka}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [circuit_breaker_link, restful_http], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({user: edgeserver}, stereotype_instances = [restful_http])
add_links({edgeserver: user}, stereotype_instances = [restful_http])
add_links({turbine: hystrixdashboard}, stereotype_instances = [restful_http])
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