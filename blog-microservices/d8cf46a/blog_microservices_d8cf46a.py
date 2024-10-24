from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_d8cf46a"
oauth2_vanilla_ui = CClass(service, "oauth2-vanilla-ui", stereotype_instances = [infrastructural, gateway, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Load Balancer': 'Ribbon'})
hystrixdashboard = CClass(service, "hystrixdashboard", stereotype_instances = [infrastructural, monitoring_dashboard, local_logging], tagged_values = {'Port': 7979, 'Monitoring Dashboard': 'Hystrix', 'Endpoints': "['/']"})
turbine = CClass(service, "turbine", stereotype_instances = [infrastructural, monitoring_server], tagged_values = {'Monitoring Server': 'Turbine', 'Port': 8989})
zuulserver = CClass(service, "zuulserver", stereotype_instances = [infrastructural, gateway, load_balancer], tagged_values = {'Port': 8765, 'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka', 'Port': 8762})
oauth2_vanilla_resource = CClass(service, "oauth2-vanilla-resource", stereotype_instances = [internal])
products = CClass(service, "products", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/products/{productId}']", 'Port': 10011})
reviews = CClass(service, "reviews", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/set-processing-time', '/reviews']"})
productcomposite = CClass(service, "productcomposite", stereotype_instances = [circuit_breaker, internal, local_logging], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/products/{productId}', '/']"})
configserver = CClass(service, "configserver", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
productapi = CClass(service, "productapi", stereotype_instances = [circuit_breaker, internal, local_logging], tagged_values = {'Circuit Breaker': 'Hystrix', 'Port': 10021, 'Endpoints': "['/products/{productId}', '/']"})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'https://github.com/spring-cloud-samples/config-repo'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({github_repository: configserver}, stereotype_instances = [restful_http])
add_links({configserver: hystrixdashboard}, stereotype_instances = [restful_http])
add_links({configserver: turbine}, stereotype_instances = [restful_http])
add_links({configserver: zuulserver}, stereotype_instances = [restful_http])
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({configserver: products}, stereotype_instances = [restful_http])
add_links({configserver: reviews}, stereotype_instances = [restful_http])
add_links({configserver: productcomposite}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({productapi: eureka}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({productcomposite: eureka}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({reviews: eureka}, stereotype_instances = [restful_http])
add_links({products: eureka}, stereotype_instances = [restful_http])
add_links({turbine: eureka}, stereotype_instances = [restful_http])
add_links({user: oauth2_vanilla_ui}, stereotype_instances = [restful_http])
add_links({oauth2_vanilla_ui: user}, stereotype_instances = [restful_http])
add_links({user: zuulserver}, stereotype_instances = [restful_http])
add_links({zuulserver: user}, stereotype_instances = [restful_http])
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