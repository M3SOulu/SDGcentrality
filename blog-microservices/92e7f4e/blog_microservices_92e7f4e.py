from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_92e7f4e"
oauth2_vanilla_ui = CClass(service, "oauth2-vanilla-ui", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
hystrixdashboard = CClass(service, "hystrixdashboard", stereotype_instances = [local_logging, infrastructural, monitoring_dashboard], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Endpoints': "['/']", 'Port': 7979})
zuulserver = CClass(service, "zuulserver", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Load Balancer': 'Ribbon', 'Gateway': 'Zuul', 'Port': 8765})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Port': 8761, 'Service Discovery': 'Eureka'})
oauth2_vanilla_resource = CClass(service, "oauth2-vanilla-resource", stereotype_instances = [internal])
products = CClass(service, "products", stereotype_instances = [circuit_breaker, internal], tagged_values = {'Port': 10011, 'Endpoints': "['/products/{productId}']", 'Circuit Breaker': 'Hystrix'})
reviews = CClass(service, "reviews", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Endpoints': "['/reviews']", 'Circuit Breaker': 'Hystrix'})
configserver = CClass(service, "configserver", stereotype_instances = [configuration_server, infrastructural], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8888})
productapi = CClass(service, "productapi", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Endpoints': "['/products/{productId}', '/']", 'Circuit Breaker': 'Hystrix', 'Port': 10021})
github_repository = CClass(external_component, "github-repository", stereotype_instances = [github_repository, entrypoint], tagged_values = {'URL': 'https://github.com/spring-cloud-samples/config-repo'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({github_repository: configserver}, stereotype_instances = [restful_http])
add_links({configserver: hystrixdashboard}, stereotype_instances = [restful_http])
add_links({configserver: zuulserver}, stereotype_instances = [restful_http])
add_links({configserver: eureka}, stereotype_instances = [restful_http])
add_links({configserver: products}, stereotype_instances = [restful_http])
add_links({configserver: reviews}, stereotype_instances = [restful_http])
add_links({configserver: productapi}, stereotype_instances = [restful_http])
add_links({products: eureka}, stereotype_instances = [circuit_breaker_link, restful_http])
add_links({reviews: eureka}, stereotype_instances = [circuit_breaker_link, restful_http])
add_links({productapi: eureka}, stereotype_instances = [circuit_breaker_link, restful_http])
add_links({user: oauth2_vanilla_ui}, stereotype_instances = [restful_http])
add_links({oauth2_vanilla_ui: user}, stereotype_instances = [restful_http])
add_links({user: zuulserver}, stereotype_instances = [restful_http])
add_links({zuulserver: user}, stereotype_instances = [restful_http])
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