from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_590569f"
oauth2_vanilla_ui = CClass(service, "oauth2-vanilla-ui", stereotype_instances = [gateway, load_balancer, infrastructural], tagged_values = {'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
oauth2_vanilla_authserver = CClass(service, "oauth2-vanilla-authserver", stereotype_instances = [infrastructural, resource_server, authorization_server], tagged_values = {'Authorization Server': 'Spring OAuth2', 'Endpoints': "['/user']", 'Port': 9999})
oauth2_vanilla_resource = CClass(service, "oauth2-vanilla-resource", stereotype_instances = [internal])
products = CClass(service, "products", stereotype_instances = [internal, circuit_breaker], tagged_values = {'Port': 10011, 'Circuit Breaker': 'Hystrix', 'Endpoints': "['/products/{productId}']"})
reviews = CClass(service, "reviews", stereotype_instances = [internal, circuit_breaker], tagged_values = {'Circuit Breaker': 'Hystrix', 'Endpoints': "['/reviews']", 'Port': 10002})
productapi = CClass(service, "productapi", stereotype_instances = [local_logging, circuit_breaker, internal], tagged_values = {'Endpoints': "['/products/{productId}', '/']", 'Circuit Breaker': 'Hystrix', 'Port': 10021})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({user: oauth2_vanilla_ui}, stereotype_instances = [restful_http])
add_links({oauth2_vanilla_ui: user}, stereotype_instances = [restful_http])
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