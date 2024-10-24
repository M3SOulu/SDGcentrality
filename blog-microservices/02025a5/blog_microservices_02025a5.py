from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_02025a5"
recommendation = CClass(service, "recommendation", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/recommendation', '/set-processing-time']"})
product = CClass(service, "product", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/product/{productId}', '/set-processing-time']"})
review = CClass(service, "review", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/review', '/set-processing-time']"})
productcomposite = CClass(service, "productcomposite", stereotype_instances = [circuit_breaker, internal, local_logging], tagged_values = {'Port': 8080, 'Circuit Breaker': 'Hystrix', 'Endpoints': "['/product/{productId}', '/']"})
hystrixdashboard = CClass(service, "hystrixdashboard", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Port': 7979, 'Endpoints': "['/']", 'Monitoring Dashboard': 'Hystrix'})
turbine = CClass(service, "turbine", stereotype_instances = [local_logging, infrastructural, monitoring_server], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edgeserver = CClass(service, "edgeserver", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Load Balancer': 'Ribbon', 'Gateway': 'Zuul', 'Port': 8765})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
productapi = CClass(service, "productapi", stereotype_instances = [circuit_breaker, internal, local_logging], tagged_values = {'Endpoints': "['/{productId}']", 'Circuit Breaker': 'Hystrix'})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Port': 5672, 'Message Broker': 'RabbitMQ'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({composite: rabbitmq}, stereotype_instances = [restful_http])
add_links({api: rabbitmq}, stereotype_instances = [restful_http])
add_links({turbine: eureka}, stereotype_instances = [restful_http])
add_links({productcomposite: eureka}, stereotype_instances = [circuit_breaker_link, restful_http], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({product: eureka}, stereotype_instances = [restful_http])
add_links({hystrixdashboard: eureka}, stereotype_instances = [restful_http])
add_links({recommendation: eureka}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [circuit_breaker_link, restful_http], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({review: eureka}, stereotype_instances = [restful_http])
add_links({user: edgeserver}, stereotype_instances = [restful_http])
add_links({edgeserver: user}, stereotype_instances = [restful_http])
add_links({turbine: hystrixdashboard}, stereotype_instances = [restful_http])
add_links({rabbitmq: turbine}, stereotype_instances = [restful_http])
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