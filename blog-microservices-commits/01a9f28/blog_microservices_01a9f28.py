from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_01a9f28"
webapp = CClass(service, "webapp", stereotype_instances = [infrastructural, gateway, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
recommendation = CClass(service, "recommendation", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/set-processing-time', '/recommendation']"})
product = CClass(service, "product", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/product/{productId}']"})
review = CClass(service, "review", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/review', '/set-processing-time']"})
productcomposite = CClass(service, "productcomposite", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/product/{productId}', '/']"})
hystrixdashboard = CClass(service, "hystrixdashboard", stereotype_instances = [infrastructural, local_logging, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Endpoints': "['/']", 'Port': 7979})
configserver = CClass(service, "configserver", stereotype_instances = [infrastructural, configuration_server], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
turbine = CClass(service, "turbine", stereotype_instances = [monitoring_server, infrastructural], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
zuulserver = CClass(service, "zuulserver", stereotype_instances = [infrastructural, gateway, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Port': 8765, 'Load Balancer': 'Ribbon'})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
productapi = CClass(service, "productapi", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Circuit Breaker': 'Hystrix', 'Port': 10001, 'Endpoints': "['/product/{productId}', '/ping']"})
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
add_links({configserver: zuulserver}, stereotype_instances = [restful_http])
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({review: eureka}, stereotype_instances = [restful_http])
add_links({turbine: eureka}, stereotype_instances = [restful_http])
add_links({product: eureka}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({productcomposite: eureka}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({recommendation: eureka}, stereotype_instances = [restful_http])
add_links({user: zuulserver}, stereotype_instances = [restful_http])
add_links({zuulserver: user}, stereotype_instances = [restful_http])
add_links({user: webapp}, stereotype_instances = [restful_http])
add_links({webapp: user}, stereotype_instances = [restful_http])
add_links({turbine: hystrixdashboard}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = productapi.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()