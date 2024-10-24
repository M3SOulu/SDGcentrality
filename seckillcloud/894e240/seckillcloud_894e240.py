from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "seckillcloud_894e240"
cloud_uaa = CClass(service, "cloud-uaa", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 8088, 'Logging Technology': 'Lombok'})
cloud_gateway = CClass(service, "cloud-gateway", stereotype_instances = [infrastructural, gateway, local_logging], tagged_values = {'Port': 8205, 'Gateway': 'Spring Cloud Gateway', 'Logging Technology': 'Lombok'})
cloud_mission = CClass(service, "cloud-mission", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 8888, 'Logging Technology': 'Lombok'})
cloud_common = CClass(service, "cloud-common", stereotype_instances = [internal, local_logging], tagged_values = {'Logging Technology': 'Lombok'})
cloud_manage = CClass(service, "cloud-manage", stereotype_instances = [internal, local_logging], tagged_values = {'Port': 8889, 'Logging Technology': 'Lombok'})
database_cloud_uaa = CClass(external_component, "database-cloud-uaa", stereotype_instances = [exitpoint, entrypoint, external_database], tagged_values = {'Port': 3306, 'Database': 'MySQL'})
database_cloud_mission = CClass(external_component, "database-cloud-mission", stereotype_instances = [exitpoint, entrypoint, external_database], tagged_values = {'Port': 3306, 'Database': 'MySQL'})
user = CClass(external_component, "user", stereotype_instances = [exitpoint, entrypoint, user_stereotype])
add_links({database_cloud_uaa: cloud_uaa}, stereotype_instances = [jdbc])
add_links({database_cloud_mission: cloud_mission}, stereotype_instances = [jdbc])
add_links({user: cloud_gateway}, stereotype_instances = [restful_http])
add_links({cloud_gateway: user}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_uaa}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_mission}, stereotype_instances = [restful_http])
add_links({cloud_gateway: cloud_manage}, stereotype_instances = [restful_http])
model = CBundle(model_name, elements = cloud_manage.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()