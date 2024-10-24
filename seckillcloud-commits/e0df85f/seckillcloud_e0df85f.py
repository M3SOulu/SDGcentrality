from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "seckillcloud_e0df85f"
cloud_uaa = CClass(service, "cloud-uaa", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok', 'Port': 8088})
cloud_gateway = CClass(service, "cloud-gateway", stereotype_instances = [local_logging, infrastructural, gateway], tagged_values = {'Logging Technology': 'Lombok', 'Gateway': 'Spring Cloud Gateway', 'Port': 8205})
cloud_mission = CClass(service, "cloud-mission", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8888, 'Logging Technology': 'Lombok'})
cloud_common = CClass(service, "cloud-common", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok'})
cloud_manage = CClass(service, "cloud-manage", stereotype_instances = [internal, pre_authorized_endpoints, csrf_disabled, encryption, local_logging], tagged_values = {'Pre-authorized Endpoints': "['/findAll']", 'Port': 8070, 'Logging Technology': 'Lombok'})
cloud_monitor = CClass(service, "cloud-monitor", stereotype_instances = [basic_authentication, administration_server, infrastructural], tagged_values = {'Port': 8890, 'Administration Server': 'Spring Boot Admin'})
database_cloud_manage = CClass(external_component, "database-cloud-manage", stereotype_instances = [entrypoint, external_database, exitpoint], tagged_values = {'Database': 'MySQL', 'Port': 3306})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
add_links({database_cloud_manage: cloud_manage}, stereotype_instances = [jdbc])
add_links({user: cloud_gateway}, stereotype_instances = [restful_http])
add_links({cloud_gateway: user}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_uaa}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_monitor}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_mission}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_manage}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = cloud_monitor.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()