from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_bab03d4"
webapp = CClass(service, "webapp", stereotype_instances = [gateway, load_balancer, infrastructural], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
recommendation = CClass(service, "recommendation", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/set-processing-time', '/recommendation']"})
product = CClass(service, "product", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/product/{productId}']"})
review = CClass(service, "review", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/review', '/set-processing-time']"})
productcomposite = CClass(service, "productcomposite", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Port': 8080, 'Endpoints': "['/', '/product/{productId}']", 'Circuit Breaker': 'Hystrix'})
hystrixdashboard = CClass(service, "hystrixdashboard", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Port': 7979, 'Endpoints': "['/']", 'Monitoring Dashboard': 'Hystrix'})
configserver = CClass(service, "configserver", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
turbine = CClass(service, "turbine", stereotype_instances = [local_logging, monitoring_server, infrastructural], tagged_values = {'Monitoring Server': 'Turbine', 'Port': 8989})
edgeserver = CClass(service, "edgeserver", stereotype_instances = [gateway, load_balancer, infrastructural], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon', 'Port': 8765})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
productapi = CClass(service, "productapi", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/{productId}']"})
rabbitmq = CClass(service, "rabbitmq", stereotype_instances = [message_broker, infrastructural], tagged_values = {'Port': 5672, 'Message Broker': 'RabbitMQ'})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'https://github.com/spring-cloud-samples/config-repo'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, user_stereotype, entrypoint])
add_links({github_repository: configserver}, stereotype_instances = [restful_http])
add_links({configserver: webapp}, stereotype_instances = [restful_http])
add_links({configserver: recommendation}, stereotype_instances = [restful_http])
add_links({configserver: product}, stereotype_instances = [restful_http])
add_links({configserver: review}, stereotype_instances = [restful_http])
add_links({configserver: productcomposite}, stereotype_instances = [restful_http])
add_links({configserver: hystrixdashboard}, stereotype_instances = [restful_http])
add_links({configserver: turbine}, stereotype_instances = [restful_http])
add_links({configserver: edgeserver}, stereotype_instances = [restful_http])
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({composite: rabbitmq}, stereotype_instances = [restful_http])
add_links({api: rabbitmq}, stereotype_instances = [restful_http])
add_links({review: eureka}, stereotype_instances = [restful_http])
add_links({turbine: eureka}, stereotype_instances = [restful_http])
add_links({product: eureka}, stereotype_instances = [restful_http])
add_links({productcomposite: eureka}, stereotype_instances = [restful_http, circuit_breaker_link], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({recommendation: eureka}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [restful_http, circuit_breaker_link], tagged_values = {'Circuit Breaker': 'Hystrix'})
add_links({hystrixdashboard: eureka}, stereotype_instances = [restful_http])
add_links({user: edgeserver}, stereotype_instances = [restful_http])
add_links({edgeserver: user}, stereotype_instances = [restful_http])
add_links({user: webapp}, stereotype_instances = [restful_http])
add_links({webapp: user}, stereotype_instances = [restful_http])
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