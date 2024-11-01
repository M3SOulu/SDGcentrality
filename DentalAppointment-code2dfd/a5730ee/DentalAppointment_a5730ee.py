from codeable_models import CClass, CBundle, add_links, CStereotype, CMetaclass, CEnum, CAttribute 
from metamodels.microservice_dfds_metamodel import * 
from plant_uml_renderer import PlantUMLGenerator 
plantuml_path = "../../plantuml.jar" 
output_directory = "." 
model_name = "DentalAppointment_a5730ee"
appointment_service = CClass(service, "appointment-service", stereotype_instances = [local_logging, internal], tagged_values = {'Port': 8201, 'Logging Technology': 'Lombok', 'Endpoints': "['/api/appointment/cancel/patient', '/api/appointment/get/{orderId}', '/api/appointment', '/api/appointment/get/doctor/{doctorId}', '/api/appointment/cancel/doctor', '/api/appointment/allocate', '/api/appointment/book', '/api/appointment/get/patient/{patientId}']"})
approval_service = CClass(service, "approval-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/api/approval/doctor', '/api/approval', '/api/approval/patient', '/api/approval/checkresult', '/api/approval/doctor/insert', '/api/approval/patient/insert']", 'Port': 8301})
hospital_manage_service = CClass(service, "hospital-manage-service", stereotype_instances = [local_logging, internal], tagged_values = {'Logging Technology': 'Lombok', 'Port': 8401, 'Endpoints': "['/{hospitalId}/appointment//{id}', '/{hospitalId}', '/{hospitalId}/kpi', '/{hospitalId}/kpidoctor/{doctorId}/day/{day}', '/{hospitalId}/administrator', '/{hospitalId}/kpidoctor/{doctorId}/month/{month}', '/{hospitalId}/appointment/doctor/{doctorId}/day/{day}', '/{hospitalId}/doctor//id/{doctorId}', '/{hospitalId}/appointment', '/{hospitalId}/medical-record/{patientId}', '/{hospitalId}/kpidoctor/{doctorId}', '/', '/{hospitalId}/doctor']"})
gateway_service = CClass(service, "gateway-service", stereotype_instances = [infrastructural, gateway], tagged_values = {'Gateway': 'Spring Cloud Gateway', 'Port': 9201})
common = CClass(service, "common", stereotype_instances = [internal])
message_service = CClass(service, "message-service", stereotype_instances = [internal], tagged_values = {'Endpoints': "['/api/message', '/api/message/simple', '/api/message/get_usermessage', '/api/message/html', '/api/message/send']", 'Port': 8302})
personal_info_service = CClass(service, "personal-info-service", stereotype_instances = [internal], tagged_values = {'Port': 8101, 'Endpoints': "['/api/doctor/loadByUsername', '/api/doctor/email', '/api/admin/login', '/api/patient/id/{patientId}', '/api/patient', '/api/patient/loadByUsername', '/api/admin/register', '/api/patient/password', '/api/admin', '/api/patient/email', '/api/patient/{patientName}', '/api/doctor/id/{doctorId}', '/api/admin/id/{adminId}', '/api/doctor/login', '/api/admin/password', '/api/doctor', '/api/doctor/password', '/api/admin/{adminName}', '/api/admin/loadByUsername', '/api/doctor/register', '/api/doctor/getByHospital/{hospitalId}', '/api/patient/login', '/api/doctor/{patientName}', '/api/patient/register', '/api/doctor/getByDepartment']"})
auth_service = CClass(service, "auth-service", stereotype_instances = [infrastructural, authorization_server], tagged_values = {'Port': 9101, 'Endpoints': "['/rsa/publicKey', '/rsa']", 'Authorization Server': 'Spring OAuth2'})
database_appointment_service = CClass(external_component, "database-appointment-service", stereotype_instances = [external_database, entrypoint, plaintext_credentials, exitpoint], tagged_values = {'Password': 'Tj_12345', 'Username': 'root', 'Database': 'MySQL'})
database_approval_service = CClass(external_component, "database-approval-service", stereotype_instances = [external_database, entrypoint, plaintext_credentials, exitpoint], tagged_values = {'Password': 'Tj_12345', 'Username': 'root', 'Database': 'MySQL'})
database_hospital_manage_service = CClass(external_component, "database-hospital-manage-service", stereotype_instances = [external_database, entrypoint, plaintext_credentials, exitpoint], tagged_values = {'Password': 'Tongji123', 'Username': 'root', 'Database': 'MySQL'})
database_message_service = CClass(external_component, "database-message-service", stereotype_instances = [external_database, entrypoint, plaintext_credentials, exitpoint], tagged_values = {'Password': 'Tongji123', 'Username': 'root', 'Database': 'MySQL'})
database_personal_info_service = CClass(external_component, "database-personal-info-service", stereotype_instances = [external_database, entrypoint, plaintext_credentials, exitpoint], tagged_values = {'Password': 'Tj_12345', 'Username': 'root', 'Database': 'MySQL'})
user = CClass(external_component, "user", stereotype_instances = [entrypoint, user_stereotype, exitpoint])
mail_server = CClass(external_component, "mail-server", stereotype_instances = [entrypoint, plaintext_credentials, exitpoint, mail_server], tagged_values = {'Host': 'smtp.qq.com', 'Password': 'xdzqpspcejvjbgbe', 'Username': '1910727674@qq.com'})
add_links({appointment_service: personal_info_service}, stereotype_instances = [feign_connection, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Ribbon'})
add_links({appointment_service: hospital_manage_service}, stereotype_instances = [feign_connection, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Ribbon'})
add_links({approval_service: appointment_service}, stereotype_instances = [feign_connection, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Ribbon'})
add_links({approval_service: message_service}, stereotype_instances = [feign_connection, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Ribbon'})
add_links({message_service: personal_info_service}, stereotype_instances = [feign_connection, restful_http, load_balanced_link], tagged_values = {'Load Balancer': 'Ribbon'})
add_links({database_appointment_service: appointment_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Password': 'Tj_12345', 'Username': 'root'})
add_links({database_approval_service: approval_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Password': 'Tj_12345', 'Username': 'root'})
add_links({database_hospital_manage_service: hospital_manage_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Password': 'Tongji123', 'Username': 'root'})
add_links({database_message_service: message_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Password': 'Tongji123', 'Username': 'root'})
add_links({database_personal_info_service: personal_info_service}, stereotype_instances = [jdbc, plaintext_credentials_link], tagged_values = {'Password': 'Tj_12345', 'Username': 'root'})
add_links({user: gateway_service}, stereotype_instances = [restful_http])
add_links({gateway_service: user}, stereotype_instances = [restful_http])
add_links({gateway_service: message_service}, stereotype_instances = [restful_http])
add_links({gateway_service: approval_service}, stereotype_instances = [restful_http])
add_links({gateway_service: hospital_manage_service}, stereotype_instances = [restful_http])
add_links({gateway_service: appointment_service}, stereotype_instances = [restful_http])
add_links({message_service: mail_server}, stereotype_instances = [plaintext_credentials_link, restful_http])
model = CBundle(model_name, elements = auth_service.class_object.get_connected_elements())
def run():
    generator = PlantUMLGenerator()
    generator.plant_uml_jar_path = plantuml_path
    generator.directory = output_directory
    generator.object_model_renderer.left_to_right = True
    generator.generate_object_models(model_name, [model, {}])
    print(f"Generated models in {generator.directory!s}/" + model_name)
if __name__ == "__main__":
    run()