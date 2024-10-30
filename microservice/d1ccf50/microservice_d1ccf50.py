from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "microservice_d1ccf50"
order = CClass(service, "order", stereotype_instances = [local_logging, internal, load_balancer], tagged_values = {'Endpoints': "['/{id}', '/form.html', '/line', '/']", 'Port': 8080, 'Load Balancer': 'Ribbon'})
eureka = CClass(service, "eureka", stereotype_instances = [infrastructural, service_discovery], tagged_values = {'Service Discovery': 'Eureka', 'Port': 8761})
turbine = CClass(service, "turbine", stereotype_instances = [infrastructural, monitoring_dashboard, monitoring_server], tagged_values = {'Port': 8989, 'Monitoring Server': 'Turbine', 'Monitoring Dashboard': 'Hystrix'})
catalog = CClass(service, "catalog", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/form.html', '/{id}.html', '/list.html', '/searchByName.html', '/searchForm.html']", 'Port': 8080})
zuul = CClass(service, "zuul", stereotype_instances = [infrastructural, gateway, load_balancer], tagged_values = {'Gateway': 'Zuul', 'Port': 8080, 'Load Balancer': 'Ribbon'})
customer = CClass(service, "customer", stereotype_instances = [internal], tagged_values = {'Endpoints': '[\'/"customer\']', 'Port': 8080})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({order: catalog}, stereotype_instances = [restful_http])
add_links({order: customer}, stereotype_instances = [restful_http])
add_links({order: order}, stereotype_instances = [restful_http])
add_links({zuul: customer}, stereotype_instances = [restful_http])
add_links({zuul: catalog}, stereotype_instances = [restful_http])
add_links({zuul: order}, stereotype_instances = [restful_http])
add_links({customer: eureka}, stereotype_instances = [restful_http])
add_links({catalog: eureka}, stereotype_instances = [restful_http])
add_links({eureka: zuul}, stereotype_instances = [restful_http])
add_links({turbine: eureka}, stereotype_instances = [restful_http])
add_links({order: eureka}, stereotype_instances = [restful_http])
add_links({user: zuul}, stereotype_instances = [restful_http])
add_links({zuul: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = customer.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()