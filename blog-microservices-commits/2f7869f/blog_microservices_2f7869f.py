from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_2f7869f"
recommendation = CClass(service, "recommendation", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/set-processing-time', '/recommendation']"})
product = CClass(service, "product", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/product/{productId}']"})
review = CClass(service, "review", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/set-processing-time', '/review']"})
productcomposite = CClass(service, "productcomposite", stereotype_instances = [local_logging, internal], tagged_values = {'Endpoints': "['/product/{productId}', '/']"})
edgeserver = CClass(service, "edgeserver", stereotype_instances = [gateway, infrastructural, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Port': 8765, 'Load Balancer': 'Ribbon'})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Port': 8762, 'Service Discovery': 'Eureka'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({recommendation: eureka}, stereotype_instances = [restful_http])
add_links({productcomposite: eureka}, stereotype_instances = [restful_http])
add_links({review: eureka}, stereotype_instances = [restful_http])
add_links({product: eureka}, stereotype_instances = [restful_http])
add_links({user: edgeserver}, stereotype_instances = [restful_http])
add_links({edgeserver: user}, stereotype_instances = [restful_http])
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