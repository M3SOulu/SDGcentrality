from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_0af384b"
recommendation = CClass(service, "recommendation", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/recommendation', '/set-processing-time']"})
product = CClass(service, "product", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/product/{productId}']"})
review = CClass(service, "review", stereotype_instances = [internal, local_logging], tagged_values = {'Endpoints': "['/set-processing-time', '/review']"})
productcomposite = CClass(service, "productcomposite", stereotype_instances = [circuit_breaker, internal, local_logging], tagged_values = {'Endpoints': "['/product/{productId}', '/']"})
hystrixdashboard = CClass(service, "hystrixdashboard", stereotype_instances = [monitoring_dashboard, infrastructural], tagged_values = {'Monitoring Dashboard': 'Hystrix', 'Port': 7979, 'Endpoints': "['/']"})
turbine = CClass(service, "turbine", stereotype_instances = [monitoring_server, infrastructural], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine'})
edgeserver = CClass(service, "edgeserver", stereotype_instances = [load_balancer, gateway, infrastructural], tagged_values = {'Port': 8765, 'Load Balancer': 'Ribbon', 'Gateway': 'Zuul'})
eureka = CClass(service, "eureka", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka', 'Port': 8762})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({recommendation: eureka}, stereotype_instances = [restful_http])
add_links({product: eureka}, stereotype_instances = [restful_http])
add_links({turbine: eureka}, stereotype_instances = [restful_http])
add_links({review: eureka}, stereotype_instances = [restful_http])
add_links({productcomposite: eureka}, stereotype_instances = [restful_http, circuit_breaker_link])
add_links({user: edgeserver}, stereotype_instances = [restful_http])
add_links({edgeserver: user}, stereotype_instances = [restful_http])
add_links({turbine: hystrixdashboard}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = eureka.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()