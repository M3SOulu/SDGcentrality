from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "blog-microservices_1315bc2"
products = CClass(service, "products", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/products/{productId}']", 'Port': 10011})
reviews = CClass(service, "reviews", stereotype_instances = [internal, circuit_breaker], tagged_values = {'Endpoints': "['/reviews']", 'Port': 10002})
productapi = CClass(service, "productapi", stereotype_instances = [internal, circuit_breaker, local_logging], tagged_values = {'Port': 10021, 'Endpoints': "['/products/{productId}']"})
add_links({False: productApi}, stereotype_instances = [restful_http])
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