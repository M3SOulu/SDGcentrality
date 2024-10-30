from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "sample-spring-microservices-new_697260d"
employee_service = CClass(service, "employee-service", stereotype_instances = [internal, local_logging])
config_service = CClass(service, "config-service", stereotype_instances = [infrastructural, configuration_server], tagged_values = {'Configuration Server': 'Spring Cloud Config', 'Port': 8088})
department_service = CClass(service, "department-service", stereotype_instances = [internal, local_logging])
gateway_service = CClass(service, "gateway-service", stereotype_instances = [gateway, infrastructural], tagged_values = {'Gateway': 'Spring Cloud Gateway'})
organization_service = CClass(service, "organization-service", stereotype_instances = [internal, local_logging])
discovery_service = CClass(service, "discovery-service", stereotype_instances = [service_discovery, infrastructural], tagged_values = {'Service Discovery': 'Eureka'})
zipkin = CClass(service, "zipkin", stereotype_instances = [tracing_server, infrastructural], tagged_values = {'Tracing Server': 'Zipkin', 'Port': 9411})
user = CClass(external_component, "user", stereotype_instances = [user_stereotype, entrypoint, exitpoint])
add_links({config_service: employee_service}, stereotype_instances = [restful_http])
add_links({config_service: department_service}, stereotype_instances = [restful_http])
add_links({config_service: gateway_service}, stereotype_instances = [restful_http])
add_links({config_service: organization_service}, stereotype_instances = [restful_http])
add_links({config_service: discovery_service}, stereotype_instances = [restful_http])
add_links({employee_service: zipkin}, stereotype_instances = [restful_http])
add_links({department_service: employee_service}, stereotype_instances = [restful_http])
add_links({department_service: zipkin}, stereotype_instances = [restful_http])
add_links({organization_service: employee_service}, stereotype_instances = [restful_http])
add_links({organization_service: department_service}, stereotype_instances = [restful_http])
add_links({organization_service: zipkin}, stereotype_instances = [restful_http])
add_links({gateway_service: employee_service}, stereotype_instances = [restful_http])
add_links({gateway_service: department_service}, stereotype_instances = [restful_http])
add_links({gateway_service: organization_service}, stereotype_instances = [restful_http])
add_links({gateway_service: zipkin}, stereotype_instances = [restful_http])
add_links({employee_service: discovery_service}, stereotype_instances = [restful_http])
add_links({discovery_service: gateway_service}, stereotype_instances = [restful_http])
add_links({organization_service: discovery_service}, stereotype_instances = [restful_http])
add_links({department_service: discovery_service}, stereotype_instances = [restful_http])
add_links({user: gateway_service}, stereotype_instances = [restful_http])
add_links({gateway_service: user}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = zipkin.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()