# swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node_user_ssh_key_add_ssh_key**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#add_node_user_ssh_key_add_ssh_key) | **POST** /node/users/{userid}/ssh-keys?action&#x3D;add_ssh_key | Add SSH public key to authorized_keys file for node user
[**cancel_appliance_management_task_cancel**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#cancel_appliance_management_task_cancel) | **POST** /node/tasks/{task-id}?action&#x3D;cancel | Cancel specified task
[**check_rabbit_mq_management_port**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#check_rabbit_mq_management_port) | **GET** /node/rabbitmq-management-port | Check if RabbitMQ management port is enabled or not
[**collect_alarms**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#collect_alarms) | **GET** /hpm/alarms | Collect alarms from all NSX nodes
[**collect_audit_logs**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#collect_audit_logs) | **POST** /administration/audit-logs | Collect audit logs from registered manager nodes
[**collect_support_bundles_collect**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#collect_support_bundles_collect) | **POST** /administration/support-bundles?action&#x3D;collect | Collect support bundles from registered cluster and fabric nodes
[**copy_from_remote_file_copy_from_remote_file**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#copy_from_remote_file_copy_from_remote_file) | **POST** /node/file-store/{file-name}?action&#x3D;copy_from_remote_file | Copy a remote file to the file store
[**copy_to_remote_file_copy_to_remote_file**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#copy_to_remote_file_copy_to_remote_file) | **POST** /node/file-store/{file-name}?action&#x3D;copy_to_remote_file | Copy file in the file store to a remote file store
[**create_appliance_management_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_appliance_management_service_action_restart) | **POST** /node/services/node-mgmt?action&#x3D;restart | Restart the node management service
[**create_cluster_boot_manager_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_cluster_boot_manager_service_action_restart) | **POST** /node/services/cluster_manager?action&#x3D;restart | Restart, start or stop the cluster boot manager service
[**create_cluster_boot_manager_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_cluster_boot_manager_service_action_start) | **POST** /node/services/cluster_manager?action&#x3D;start | Restart, start or stop the cluster boot manager service
[**create_cluster_boot_manager_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_cluster_boot_manager_service_action_stop) | **POST** /node/services/cluster_manager?action&#x3D;stop | Restart, start or stop the cluster boot manager service
[**create_cminventory_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_cminventory_service_action_restart) | **POST** /node/services/cm-inventory?action&#x3D;restart | Restart, start or stop the manager service
[**create_cminventory_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_cminventory_service_action_start) | **POST** /node/services/cm-inventory?action&#x3D;start | Restart, start or stop the manager service
[**create_cminventory_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_cminventory_service_action_stop) | **POST** /node/services/cm-inventory?action&#x3D;stop | Restart, start or stop the manager service
[**create_controller_server_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_controller_server_service_action_restart) | **POST** /node/services/controller?action&#x3D;restart | Restart, start or stop the controller service
[**create_controller_server_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_controller_server_service_action_start) | **POST** /node/services/controller?action&#x3D;start | Restart, start or stop the controller service
[**create_controller_server_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_controller_server_service_action_stop) | **POST** /node/services/controller?action&#x3D;stop | Restart, start or stop the controller service
[**create_file**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_file) | **POST** /node/file-store/{file-name} | Upload a file to the file store
[**create_liagent_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_liagent_service_action_restart) | **POST** /node/services/liagent?action&#x3D;restart | Restart, start or stop the liagent service
[**create_liagent_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_liagent_service_action_start) | **POST** /node/services/liagent?action&#x3D;start | Restart, start or stop the liagent service
[**create_liagent_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_liagent_service_action_stop) | **POST** /node/services/liagent?action&#x3D;stop | Restart, start or stop the liagent service
[**create_migration_coordinator_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_migration_coordinator_service_action_restart) | **POST** /node/services/migration-coordinator?action&#x3D;restart | Restart, start or stop the migration coordinator service
[**create_migration_coordinator_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_migration_coordinator_service_action_start) | **POST** /node/services/migration-coordinator?action&#x3D;start | Restart, start or stop the migration coordinator service
[**create_migration_coordinator_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_migration_coordinator_service_action_stop) | **POST** /node/services/migration-coordinator?action&#x3D;stop | Restart, start or stop the migration coordinator service
[**create_node_network_route**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_node_network_route) | **POST** /node/network/routes | Create node network route
[**create_node_stats_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_node_stats_service_action_restart) | **POST** /node/services/node-stats?action&#x3D;restart | Restart, start or stop the NSX node-stats service
[**create_node_stats_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_node_stats_service_action_start) | **POST** /node/services/node-stats?action&#x3D;start | Restart, start or stop the NSX node-stats service
[**create_node_stats_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_node_stats_service_action_stop) | **POST** /node/services/node-stats?action&#x3D;stop | Restart, start or stop the NSX node-stats service
[**create_nsx_message_bus_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_message_bus_service_action_restart) | **POST** /node/services/nsx-message-bus?action&#x3D;restart | Restart, start or stop the NSX Message Bus service
[**create_nsx_message_bus_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_message_bus_service_action_start) | **POST** /node/services/nsx-message-bus?action&#x3D;start | Restart, start or stop the NSX Message Bus service
[**create_nsx_message_bus_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_message_bus_service_action_stop) | **POST** /node/services/nsx-message-bus?action&#x3D;stop | Restart, start or stop the NSX Message Bus service
[**create_nsx_ui_service_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_ui_service_service_action_restart) | **POST** /node/services/ui-service?action&#x3D;restart | Restart, Start and Stop the ui service
[**create_nsx_ui_service_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_ui_service_service_action_start) | **POST** /node/services/ui-service?action&#x3D;start | Restart, Start and Stop the ui service
[**create_nsx_ui_service_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_ui_service_service_action_stop) | **POST** /node/services/ui-service?action&#x3D;stop | Restart, Start and Stop the ui service
[**create_nsx_upgrade_agent_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_upgrade_agent_service_action_restart) | **POST** /node/services/nsx-upgrade-agent?action&#x3D;restart | Restart, start or stop the NSX upgrade agent service
[**create_nsx_upgrade_agent_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_upgrade_agent_service_action_start) | **POST** /node/services/nsx-upgrade-agent?action&#x3D;start | Restart, start or stop the NSX upgrade agent service
[**create_nsx_upgrade_agent_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_nsx_upgrade_agent_service_action_stop) | **POST** /node/services/nsx-upgrade-agent?action&#x3D;stop | Restart, start or stop the NSX upgrade agent service
[**create_ntp_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ntp_service_action_restart) | **POST** /node/services/ntp?action&#x3D;restart | Restart, start or stop the NTP service
[**create_ntp_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ntp_service_action_start) | **POST** /node/services/ntp?action&#x3D;start | Restart, start or stop the NTP service
[**create_ntp_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ntp_service_action_stop) | **POST** /node/services/ntp?action&#x3D;stop | Restart, start or stop the NTP service
[**create_phonehome_coordinator_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_phonehome_coordinator_service_action_restart) | **POST** /node/services/telemetry?action&#x3D;restart | Restart, start or stop Telemetry service
[**create_phonehome_coordinator_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_phonehome_coordinator_service_action_start) | **POST** /node/services/telemetry?action&#x3D;start | Restart, start or stop Telemetry service
[**create_phonehome_coordinator_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_phonehome_coordinator_service_action_stop) | **POST** /node/services/telemetry?action&#x3D;stop | Restart, start or stop Telemetry service
[**create_platform_client_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_platform_client_service_action_restart) | **POST** /node/services/nsx-platform-client?action&#x3D;restart | Restart, start or stop the NSX Platform Client service
[**create_platform_client_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_platform_client_service_action_start) | **POST** /node/services/nsx-platform-client?action&#x3D;start | Restart, start or stop the NSX Platform Client service
[**create_platform_client_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_platform_client_service_action_stop) | **POST** /node/services/nsx-platform-client?action&#x3D;stop | Restart, start or stop the NSX Platform Client service
[**create_policy_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_policy_service_action_restart) | **POST** /node/services/policy?action&#x3D;restart | Restart, start or stop the service
[**create_policy_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_policy_service_action_start) | **POST** /node/services/policy?action&#x3D;start | Restart, start or stop the service
[**create_policy_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_policy_service_action_stop) | **POST** /node/services/policy?action&#x3D;stop | Restart, start or stop the service
[**create_proton_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_proton_service_action_restart) | **POST** /node/services/manager?action&#x3D;restart | Restart, start or stop the service
[**create_proton_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_proton_service_action_start) | **POST** /node/services/manager?action&#x3D;start | Restart, start or stop the service
[**create_proton_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_proton_service_action_stop) | **POST** /node/services/manager?action&#x3D;stop | Restart, start or stop the service
[**create_proxy_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_proxy_service_action_restart) | **POST** /node/services/http?action&#x3D;restart | Restart the http service
[**create_proxy_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_proxy_service_action_start) | **POST** /node/services/http?action&#x3D;start | Start the http service
[**create_proxy_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_proxy_service_action_stop) | **POST** /node/services/http?action&#x3D;stop | Stop the http service
[**create_proxy_service_apply_certificate_action_apply_certificate**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_proxy_service_apply_certificate_action_apply_certificate) | **POST** /node/services/http?action&#x3D;apply_certificate | Update http service certificate
[**create_rabbit_mq_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_rabbit_mq_service_action_restart) | **POST** /node/services/mgmt-plane-bus?action&#x3D;restart | Restart, start or stop the Rabbit MQ service
[**create_rabbit_mq_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_rabbit_mq_service_action_start) | **POST** /node/services/mgmt-plane-bus?action&#x3D;start | Restart, start or stop the Rabbit MQ service
[**create_rabbit_mq_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_rabbit_mq_service_action_stop) | **POST** /node/services/mgmt-plane-bus?action&#x3D;stop | Restart, start or stop the Rabbit MQ service
[**create_remote_directory_create_remote_directory**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_remote_directory_create_remote_directory) | **POST** /node/file-store?action&#x3D;create_remote_directory | Create directory in remote file server
[**create_repository_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_repository_service_action_restart) | **POST** /node/services/install-upgrade?action&#x3D;restart | Restart, start or stop the NSX install-upgrade service
[**create_repository_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_repository_service_action_start) | **POST** /node/services/install-upgrade?action&#x3D;start | Restart, start or stop the NSX install-upgrade service
[**create_repository_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_repository_service_action_stop) | **POST** /node/services/install-upgrade?action&#x3D;stop | Restart, start or stop the NSX install-upgrade service
[**create_search_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_search_service_action_restart) | **POST** /node/services/search?action&#x3D;restart | Restart, start or stop the NSX Search service
[**create_search_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_search_service_action_start) | **POST** /node/services/search?action&#x3D;start | Restart, start or stop the NSX Search service
[**create_search_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_search_service_action_stop) | **POST** /node/services/search?action&#x3D;stop | Restart, start or stop the NSX Search service
[**create_snmp_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_snmp_service_action_restart) | **POST** /node/services/snmp?action&#x3D;restart | Restart, start or stop the SNMP service
[**create_snmp_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_snmp_service_action_start) | **POST** /node/services/snmp?action&#x3D;start | Restart, start or stop the SNMP service
[**create_snmp_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_snmp_service_action_stop) | **POST** /node/services/snmp?action&#x3D;stop | Restart, start or stop the SNMP service
[**create_ssh_service_action_notify_mpa_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ssh_service_action_notify_mpa_restart) | **POST** /node/services/ssh/notify_mpa?action&#x3D;restart | Restart, start or stop the ssh service
[**create_ssh_service_action_notify_mpa_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ssh_service_action_notify_mpa_start) | **POST** /node/services/ssh/notify_mpa?action&#x3D;start | Restart, start or stop the ssh service
[**create_ssh_service_action_notify_mpa_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ssh_service_action_notify_mpa_stop) | **POST** /node/services/ssh/notify_mpa?action&#x3D;stop | Restart, start or stop the ssh service
[**create_ssh_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ssh_service_action_restart) | **POST** /node/services/ssh?action&#x3D;restart | Restart, start or stop the ssh service
[**create_ssh_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ssh_service_action_start) | **POST** /node/services/ssh?action&#x3D;start | Restart, start or stop the ssh service
[**create_ssh_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ssh_service_action_stop) | **POST** /node/services/ssh?action&#x3D;stop | Restart, start or stop the ssh service
[**create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint) | **POST** /node/services/ssh?action&#x3D;remove_host_fingerprint | Remove a host&#x27;s fingerprint from known hosts file
[**create_syslog_service_action_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_syslog_service_action_restart) | **POST** /node/services/syslog?action&#x3D;restart | Restart, start or stop the syslog service
[**create_syslog_service_action_start**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_syslog_service_action_start) | **POST** /node/services/syslog?action&#x3D;start | Restart, start or stop the syslog service
[**create_syslog_service_action_stop**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#create_syslog_service_action_stop) | **POST** /node/services/syslog?action&#x3D;stop | Restart, start or stop the syslog service
[**d_elete_rabbit_mq_management_port**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#d_elete_rabbit_mq_management_port) | **DELETE** /node/rabbitmq-management-port | Delete RabbitMQ management port
[**delete_appliance_management_task**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#delete_appliance_management_task) | **DELETE** /node/tasks/{task-id} | Delete task
[**delete_file**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#delete_file) | **DELETE** /node/file-store/{file-name} | Delete file
[**delete_node_network_route**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#delete_node_network_route) | **DELETE** /node/network/routes/{route-id} | Delete node network route
[**delete_node_syslog_exporter**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#delete_node_syslog_exporter) | **DELETE** /node/services/syslog/exporters/{exporter-name} | Delete node syslog exporter
[**delete_node_user_ssh_key_remove_ssh_key**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#delete_node_user_ssh_key_remove_ssh_key) | **POST** /node/users/{userid}/ssh-keys?action&#x3D;remove_ssh_key | Remove SSH public key from authorized_keys file for node user
[**delete_support_bundles_async_response_delete_async_response**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#delete_support_bundles_async_response_delete_async_response) | **POST** /administration/support-bundles?action&#x3D;delete_async_response | Delete existing support bundles waiting to be downloaded
[**get_controller_profiler_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#get_controller_profiler_status) | **GET** /node/services/controller/profiler | Get the status (Enabled/Disabled) of controller profiler
[**get_node_mandatory_access_control**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#get_node_mandatory_access_control) | **GET** /node/hardening-policy/mandatory-access-control | Gets the enable status for Mandatory Access Control
[**get_node_mandatory_access_control_report**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#get_node_mandatory_access_control_report) | **GET** /node/hardening-policy/mandatory-access-control/report | Get the report for Mandatory Access Control
[**invoke_delete_cluster_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_delete_cluster_central_api) | **DELETE** /cluster/{target-node-id}/{target-uri} | Invoke DELETE request on target cluster node
[**invoke_delete_fabric_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_delete_fabric_central_api) | **DELETE** /fabric/nodes/{target-node-id}/{target-uri} | Invoke DELETE request on target fabric node
[**invoke_delete_transport_node_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_delete_transport_node_central_api) | **DELETE** /transport-nodes/{target-node-id}/{target-uri} | Invoke DELETE request on target transport node
[**invoke_get_cluster_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_get_cluster_central_api) | **GET** /cluster/{target-node-id}/{target-uri} | Invoke GET request on target cluster node
[**invoke_get_fabric_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_get_fabric_central_api) | **GET** /fabric/nodes/{target-node-id}/{target-uri} | Invoke GET request on target fabric node
[**invoke_get_transport_node_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_get_transport_node_central_api) | **GET** /transport-nodes/{target-node-id}/{target-uri} | Invoke GET request on target transport node
[**invoke_post_cluster_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_post_cluster_central_api) | **POST** /cluster/{target-node-id}/{target-uri} | Invoke POST request on target cluster node
[**invoke_post_fabric_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_post_fabric_central_api) | **POST** /fabric/nodes/{target-node-id}/{target-uri} | Invoke POST request on target fabric node
[**invoke_post_transport_node_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_post_transport_node_central_api) | **POST** /transport-nodes/{target-node-id}/{target-uri} | Invoke POST request on target transport node
[**invoke_put_cluster_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_put_cluster_central_api) | **PUT** /cluster/{target-node-id}/{target-uri} | Invoke PUT request on target cluster node
[**invoke_put_fabric_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_put_fabric_central_api) | **PUT** /fabric/nodes/{target-node-id}/{target-uri} | Invoke PUT request on target fabric node
[**invoke_put_transport_node_central_api**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#invoke_put_transport_node_central_api) | **PUT** /transport-nodes/{target-node-id}/{target-uri} | Invoke PUT request on target transport node
[**list_appliance_management_tasks**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_appliance_management_tasks) | **GET** /node/tasks | List appliance management tasks
[**list_files**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_files) | **GET** /node/file-store | List node files
[**list_node_interfaces**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_node_interfaces) | **GET** /node/network/interfaces | List the NSX Manager&#x27;s Network Interfaces
[**list_node_network_routes**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_node_network_routes) | **GET** /node/network/routes | List node network routes
[**list_node_processes**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_node_processes) | **GET** /node/processes | List node processes
[**list_node_services**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_node_services) | **GET** /node/services | List node services
[**list_node_syslog_exporters**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_node_syslog_exporters) | **GET** /node/services/syslog/exporters | List node syslog exporters
[**list_node_user_ssh_keys**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_node_user_ssh_keys) | **GET** /node/users/{userid}/ssh-keys | List SSH keys from authorized_keys file for node user
[**list_node_users**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#list_node_users) | **GET** /node/users | List node users
[**post_node_syslog_exporter**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#post_node_syslog_exporter) | **POST** /node/services/syslog/exporters | Add node syslog exporter
[**read_appliance_management_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_appliance_management_service) | **GET** /node/services/node-mgmt | Read appliance management service properties
[**read_appliance_management_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_appliance_management_service_status) | **GET** /node/services/node-mgmt/status | Read appliance management service status
[**read_appliance_management_task_properties**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_appliance_management_task_properties) | **GET** /node/tasks/{task-id} | Read task properties
[**read_appliance_node_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_appliance_node_status) | **GET** /node/status | Read node status
[**read_async_appliance_management_task_response**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_async_appliance_management_task_response) | **GET** /node/tasks/{task-id}/response | Read asynchronous task response
[**read_auth_provider_vidm**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_auth_provider_vidm) | **GET** /node/aaa/providers/vidm | Read AAA provider vIDM properties
[**read_auth_provider_vidm_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_auth_provider_vidm_status) | **GET** /node/aaa/providers/vidm/status | Read AAA provider vIDM status
[**read_cluster_boot_manager_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_cluster_boot_manager_service) | **GET** /node/services/cluster_manager | Read cluster boot manager service properties
[**read_cluster_boot_manager_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_cluster_boot_manager_service_status) | **GET** /node/services/cluster_manager/status | Read cluster boot manager service status
[**read_cminventory_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_cminventory_service) | **GET** /node/services/cm-inventory | Read cm inventory service properties
[**read_cminventory_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_cminventory_service_status) | **GET** /node/services/cm-inventory/status | Read manager service status
[**read_controller_server_certificate**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_controller_server_certificate) | **GET** /node/services/controller/controller-certificate | Read controller server certificate properties
[**read_controller_server_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_controller_server_service) | **GET** /node/services/controller | Read controller service properties
[**read_controller_server_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_controller_server_service_status) | **GET** /node/services/controller/status | Read controller service status
[**read_file**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_file) | **GET** /node/file-store/{file-name}/data | Read file contents
[**read_file_properties**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_file_properties) | **GET** /node/file-store/{file-name} | Read file properties
[**read_file_thumbprint**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_file_thumbprint) | **GET** /node/file-store/{file-name}/thumbprint | Read file thumbprint
[**read_liagent_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_liagent_service) | **GET** /node/services/liagent | Read liagent service properties
[**read_liagent_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_liagent_service_status) | **GET** /node/services/liagent/status | Read liagent service status
[**read_migration_coordinator_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_migration_coordinator_service) | **GET** /node/services/migration-coordinator | Read migration coordinator service properties
[**read_migration_coordinator_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_migration_coordinator_service_status) | **GET** /node/services/migration-coordinator/status | Read migration coordinator service status
[**read_network_interface_statistics**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_network_interface_statistics) | **GET** /node/network/interfaces/{interface-id}/stats | Read the NSX Manager&#x27;s Network Interface Statistics
[**read_network_properties**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_network_properties) | **GET** /node/network | Read network configuration properties
[**read_node_interface**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_interface) | **GET** /node/network/interfaces/{interface-id} | Read the NSX Manager&#x27;s Network Interface
[**read_node_name_servers**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_name_servers) | **GET** /node/network/name-servers | Read the NSX Manager&#x27;s Name Servers
[**read_node_network_route**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_network_route) | **GET** /node/network/routes/{route-id} | Read node network route
[**read_node_process**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_process) | **GET** /node/processes/{process-id} | Read node process
[**read_node_properties**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_properties) | **GET** /node | Read node properties
[**read_node_search_domains**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_search_domains) | **GET** /node/network/search-domains | Read the NSX Manager&#x27;s Search Domains
[**read_node_stats_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_stats_service) | **GET** /node/services/node-stats | Read NSX node-stats service properties
[**read_node_stats_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_stats_service_status) | **GET** /node/services/node-stats/status | Read NSX node-stats service status
[**read_node_support_bundle**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_support_bundle) | **GET** /node/support-bundle | Read node support bundle
[**read_node_syslog_exporter**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_syslog_exporter) | **GET** /node/services/syslog/exporters/{exporter-name} | Read node syslog exporter
[**read_node_user**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_user) | **GET** /node/users/{userid} | Read node user
[**read_node_version**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_node_version) | **GET** /node/version | Read node version
[**read_nsx_message_bus_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_nsx_message_bus_service) | **GET** /node/services/nsx-message-bus | Read NSX Message Bus service properties
[**read_nsx_message_bus_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_nsx_message_bus_service_status) | **GET** /node/services/nsx-message-bus/status | Read NSX Message Bus service status
[**read_nsx_ui_service_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_nsx_ui_service_service) | **GET** /node/services/ui-service | Read ui service properties
[**read_nsx_ui_service_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_nsx_ui_service_service_status) | **GET** /node/services/ui-service/status | Read ui service status
[**read_nsx_upgrade_agent_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_nsx_upgrade_agent_service) | **GET** /node/services/nsx-upgrade-agent | Read NSX upgrade Agent service properties
[**read_nsx_upgrade_agent_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_nsx_upgrade_agent_service_status) | **GET** /node/services/nsx-upgrade-agent/status | Read Nsx upgrade agent service status
[**read_ntp_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_ntp_service) | **GET** /node/services/ntp | Read NTP service properties
[**read_ntp_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_ntp_service_status) | **GET** /node/services/ntp/status | Read NTP service status
[**read_phonehome_coordinator_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_phonehome_coordinator_service) | **GET** /node/services/telemetry | Read Telemetry service properties
[**read_phonehome_coordinator_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_phonehome_coordinator_service_status) | **GET** /node/services/telemetry/status | Read Telemetry service status
[**read_platform_client_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_platform_client_service) | **GET** /node/services/nsx-platform-client | Read NSX Platform Client service properties
[**read_platform_client_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_platform_client_service_status) | **GET** /node/services/nsx-platform-client/status | Read NSX Platform Client service status
[**read_policy_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_policy_service) | **GET** /node/services/policy | Read service properties
[**read_policy_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_policy_service_status) | **GET** /node/services/policy/status | Read service status
[**read_proton_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_proton_service) | **GET** /node/services/manager | Read service properties
[**read_proton_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_proton_service_status) | **GET** /node/services/manager/status | Read service status
[**read_proxy_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_proxy_service) | **GET** /node/services/http | Read http service properties
[**read_proxy_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_proxy_service_status) | **GET** /node/services/http/status | Read http service status
[**read_rabbit_mq_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_rabbit_mq_service) | **GET** /node/services/mgmt-plane-bus | Read Rabbit MQ service properties
[**read_rabbit_mq_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_rabbit_mq_service_status) | **GET** /node/services/mgmt-plane-bus/status | Read Rabbit MQ service status
[**read_repository_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_repository_service) | **GET** /node/services/install-upgrade | Read NSX install-upgrade service properties
[**read_repository_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_repository_service_status) | **GET** /node/services/install-upgrade/status | Read NSX install-upgrade service status
[**read_search_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_search_service) | **GET** /node/services/search | Read NSX Search service properties
[**read_search_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_search_service_status) | **GET** /node/services/search/status | Read NSX Search service status
[**read_snmp_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_snmp_service) | **GET** /node/services/snmp | Read SNMP service properties
[**read_snmp_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_snmp_service_status) | **GET** /node/services/snmp/status | Read SNMP service status
[**read_snmpv3_engine_id**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_snmpv3_engine_id) | **GET** /node/services/snmp/v3-engine-id | Read SNMP V3 Engine ID
[**read_ssh_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_ssh_service) | **GET** /node/services/ssh | Read ssh service properties
[**read_ssh_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_ssh_service_status) | **GET** /node/services/ssh/status | Read ssh service status
[**read_syslog_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_syslog_service) | **GET** /node/services/syslog | Read syslog service properties
[**read_syslog_service_status**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#read_syslog_service_status) | **GET** /node/services/syslog/status | Read syslog service status
[**reset_policy_service_logging_level_action_reset_manager_logging_levels**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#reset_policy_service_logging_level_action_reset_manager_logging_levels) | **POST** /node/services/policy?action&#x3D;reset-manager-logging-levels | Reset the logging levels to default values
[**reset_proton_service_logging_level_action_reset_manager_logging_levels**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#reset_proton_service_logging_level_action_reset_manager_logging_levels) | **POST** /node/services/manager?action&#x3D;reset-manager-logging-levels | Reset the logging levels to default values
[**restart_or_shutdown_node_restart**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#restart_or_shutdown_node_restart) | **POST** /node?action&#x3D;restart | Restart or shutdown node
[**restart_or_shutdown_node_shutdown**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#restart_or_shutdown_node_shutdown) | **POST** /node?action&#x3D;shutdown | Restart or shutdown node
[**set_controller_profiler**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#set_controller_profiler) | **PUT** /node/services/controller/profiler | Enable or disable controller profiler
[**set_node_mandatory_access_control**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#set_node_mandatory_access_control) | **PUT** /node/hardening-policy/mandatory-access-control | Enable or disable  Mandatory Access Control
[**set_rabbit_mq_management_port**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#set_rabbit_mq_management_port) | **POST** /node/rabbitmq-management-port | Set RabbitMQ management port
[**update_appliance_node_status_clear_bootup_error**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_appliance_node_status_clear_bootup_error) | **POST** /node/status?action&#x3D;clear_bootup_error | Update node status
[**update_auth_provider_vidm**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_auth_provider_vidm) | **PUT** /node/aaa/providers/vidm | Update AAA provider vIDM properties
[**update_file**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_file) | **PUT** /node/file-store/{file-name}/data | Replace file contents
[**update_node_interface**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_node_interface) | **PUT** /node/network/interfaces/{interface-id} | Update the NSX Manager&#x27;s Network Interface
[**update_node_name_servers**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_node_name_servers) | **PUT** /node/network/name-servers | Update the NSX Manager&#x27;s Name Servers
[**update_node_properties**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_node_properties) | **PUT** /node | Update node properties
[**update_node_search_domains**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_node_search_domains) | **PUT** /node/network/search-domains | Update the NSX Manager&#x27;s Search Domains
[**update_node_user**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_node_user) | **PUT** /node/users/{userid} | Update node user
[**update_ntp_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_ntp_service) | **PUT** /node/services/ntp | Update NTP service properties
[**update_policy_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_policy_service) | **PUT** /node/services/policy | Update service properties
[**update_proton_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_proton_service) | **PUT** /node/services/manager | Update service properties
[**update_proxy_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_proxy_service) | **PUT** /node/services/http | Update http service properties
[**update_repository_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_repository_service) | **PUT** /node/services/install-upgrade | Update NSX install-upgrade service properties
[**update_snmp_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_snmp_service) | **PUT** /node/services/snmp | Update SNMP service properties
[**update_snmpv3_engine_id**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_snmpv3_engine_id) | **PUT** /node/services/snmp/v3-engine-id | Update SNMP V3 Engine ID
[**update_ssh_service**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_ssh_service) | **PUT** /node/services/ssh | Update ssh service properties
[**update_uc_state**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#update_uc_state) | **PUT** /node/services/install-upgrade/uc-state | Update UC state properties
[**verify_node_syslog_exporter_verify**](ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi.md#verify_node_syslog_exporter_verify) | **POST** /node/services/syslog/exporters?action&#x3D;verify | Verify node syslog exporter

# **add_node_user_ssh_key_add_ssh_key**
> add_node_user_ssh_key_add_ssh_key(body, userid)

Add SSH public key to authorized_keys file for node user

Add SSH public key to authorized_keys file for node user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.SshKeyProperties() # SshKeyProperties | 
userid = 'userid_example' # str | User id of the user

try:
    # Add SSH public key to authorized_keys file for node user
    api_instance.add_node_user_ssh_key_add_ssh_key(body, userid)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->add_node_user_ssh_key_add_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SshKeyProperties**](SshKeyProperties.md)|  | 
 **userid** | **str**| User id of the user | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_appliance_management_task_cancel**
> cancel_appliance_management_task_cancel(task_id)

Cancel specified task

Cancel specified task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to delete

try:
    # Cancel specified task
    api_instance.cancel_appliance_management_task_cancel(task_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->cancel_appliance_management_task_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_rabbit_mq_management_port**
> PortStatus check_rabbit_mq_management_port()

Check if RabbitMQ management port is enabled or not

Returns status as true if RabbitMQ management port is enabled else false

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Check if RabbitMQ management port is enabled or not
    api_response = api_instance.check_rabbit_mq_management_port()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->check_rabbit_mq_management_port: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortStatus**](PortStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_alarms**
> AlarmListResult collect_alarms(cursor=cursor, fields=fields, page_size=page_size)

Collect alarms from all NSX nodes

This API is executed on a manager node to return current alarms from all NSX nodes. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
cursor = 789 # int | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
fields = 'fields_example' # str | Fields to include in query results (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)

try:
    # Collect alarms from all NSX nodes
    api_response = api_instance.collect_alarms(cursor=cursor, fields=fields, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->collect_alarms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **fields** | **str**| Fields to include in query results | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 

### Return type

[**AlarmListResult**](AlarmListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_audit_logs**
> AuditLogListResult collect_audit_logs(body, cursor=cursor, fields=fields, page_size=page_size)

Collect audit logs from registered manager nodes

This API is executed on a manager node to display audit logs from all nodes inside the management plane cluster. An audit log collection will be triggered if the local master audit log is outdated. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuditLogRequest() # AuditLogRequest | 
cursor = 789 # int | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
fields = 'fields_example' # str | Fields to include in query results (optional)
page_size = 789 # int | Maximum number of results to return in this page (server may return fewer) (optional)

try:
    # Collect audit logs from registered manager nodes
    api_response = api_instance.collect_audit_logs(body, cursor=cursor, fields=fields, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->collect_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditLogRequest**](AuditLogRequest.md)|  | 
 **cursor** | **int**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **fields** | **str**| Fields to include in query results | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] 

### Return type

[**AuditLogListResult**](AuditLogListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_support_bundles_collect**
> SupportBundleResult collect_support_bundles_collect(body, override_async_response=override_async_response, require_delete_or_override_async_response=require_delete_or_override_async_response)

Collect support bundles from registered cluster and fabric nodes

Collect support bundles from registered cluster and fabric nodes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupportBundleRequest() # SupportBundleRequest | 
override_async_response = true # bool | Override any existing support bundle async response (optional)
require_delete_or_override_async_response = true # bool | Suppress auto-deletion of generated support bundle (optional)

try:
    # Collect support bundles from registered cluster and fabric nodes
    api_response = api_instance.collect_support_bundles_collect(body, override_async_response=override_async_response, require_delete_or_override_async_response=require_delete_or_override_async_response)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->collect_support_bundles_collect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportBundleRequest**](SupportBundleRequest.md)|  | 
 **override_async_response** | **bool**| Override any existing support bundle async response | [optional] 
 **require_delete_or_override_async_response** | **bool**| Suppress auto-deletion of generated support bundle | [optional] 

### Return type

[**SupportBundleResult**](SupportBundleResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_from_remote_file_copy_from_remote_file**
> FileProperties copy_from_remote_file_copy_from_remote_file(body, file_name)

Copy a remote file to the file store

Copy a remote file to the file store. If you use scp or sftp, you must provide the remote server's SSH fingerprint. See the <i>NSX-T Administration Guide</i> for information and instructions about finding the SSH fingerprint. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CopyFromRemoteFileProperties() # CopyFromRemoteFileProperties | 
file_name = 'file_name_example' # str | Destination filename

try:
    # Copy a remote file to the file store
    api_response = api_instance.copy_from_remote_file_copy_from_remote_file(body, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->copy_from_remote_file_copy_from_remote_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyFromRemoteFileProperties**](CopyFromRemoteFileProperties.md)|  | 
 **file_name** | **str**| Destination filename | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_to_remote_file_copy_to_remote_file**
> copy_to_remote_file_copy_to_remote_file(body, file_name)

Copy file in the file store to a remote file store

Copy a file in the file store to a remote server. If you use scp or sftp, you must provide the remote server's SSH fingerprint. See the <i>NSX-T Administration Guide</i> for information and instructions about finding the SSH fingerprint. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CopyToRemoteFileProperties() # CopyToRemoteFileProperties | 
file_name = 'file_name_example' # str | Destination filename

try:
    # Copy file in the file store to a remote file store
    api_instance.copy_to_remote_file_copy_to_remote_file(body, file_name)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->copy_to_remote_file_copy_to_remote_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyToRemoteFileProperties**](CopyToRemoteFileProperties.md)|  | 
 **file_name** | **str**| Destination filename | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_management_service_action_restart**
> create_appliance_management_service_action_restart()

Restart the node management service

Restart the node management service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart the node management service
    api_instance.create_appliance_management_service_action_restart()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_appliance_management_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_boot_manager_service_action_restart**
> NodeServiceStatusProperties create_cluster_boot_manager_service_action_restart()

Restart, start or stop the cluster boot manager service

Restart, start or stop the cluster boot manager service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the cluster boot manager service
    api_response = api_instance.create_cluster_boot_manager_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_cluster_boot_manager_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_boot_manager_service_action_start**
> NodeServiceStatusProperties create_cluster_boot_manager_service_action_start()

Restart, start or stop the cluster boot manager service

Restart, start or stop the cluster boot manager service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the cluster boot manager service
    api_response = api_instance.create_cluster_boot_manager_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_cluster_boot_manager_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_boot_manager_service_action_stop**
> NodeServiceStatusProperties create_cluster_boot_manager_service_action_stop()

Restart, start or stop the cluster boot manager service

Restart, start or stop the cluster boot manager service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the cluster boot manager service
    api_response = api_instance.create_cluster_boot_manager_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_cluster_boot_manager_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cminventory_service_action_restart**
> NodeServiceStatusProperties create_cminventory_service_action_restart()

Restart, start or stop the manager service

Restart, start or stop the manager service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the manager service
    api_response = api_instance.create_cminventory_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_cminventory_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cminventory_service_action_start**
> NodeServiceStatusProperties create_cminventory_service_action_start()

Restart, start or stop the manager service

Restart, start or stop the manager service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the manager service
    api_response = api_instance.create_cminventory_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_cminventory_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cminventory_service_action_stop**
> NodeServiceStatusProperties create_cminventory_service_action_stop()

Restart, start or stop the manager service

Restart, start or stop the manager service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the manager service
    api_response = api_instance.create_cminventory_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_cminventory_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_controller_server_service_action_restart**
> NodeServiceStatusProperties create_controller_server_service_action_restart()

Restart, start or stop the controller service

Restart, start or stop the controller service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the controller service
    api_response = api_instance.create_controller_server_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_controller_server_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_controller_server_service_action_start**
> NodeServiceStatusProperties create_controller_server_service_action_start()

Restart, start or stop the controller service

Restart, start or stop the controller service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the controller service
    api_response = api_instance.create_controller_server_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_controller_server_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_controller_server_service_action_stop**
> NodeServiceStatusProperties create_controller_server_service_action_stop()

Restart, start or stop the controller service

Restart, start or stop the controller service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the controller service
    api_response = api_instance.create_controller_server_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_controller_server_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> FileProperties create_file(file_name)

Upload a file to the file store

When you issue this API, the client must specify: - HTTP header Content-Type:application/octet-stream. - Request body with the contents of the file in the filestore. In the CLI, you can view the filestore with the <em>get files</em> command. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Destination filename

try:
    # Upload a file to the file store
    api_response = api_instance.create_file(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Destination filename | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_liagent_service_action_restart**
> NodeServiceStatusProperties create_liagent_service_action_restart()

Restart, start or stop the liagent service

Restart, start or stop the liagent service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the liagent service
    api_response = api_instance.create_liagent_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_liagent_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_liagent_service_action_start**
> NodeServiceStatusProperties create_liagent_service_action_start()

Restart, start or stop the liagent service

Restart, start or stop the liagent service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the liagent service
    api_response = api_instance.create_liagent_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_liagent_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_liagent_service_action_stop**
> NodeServiceStatusProperties create_liagent_service_action_stop()

Restart, start or stop the liagent service

Restart, start or stop the liagent service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the liagent service
    api_response = api_instance.create_liagent_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_liagent_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_migration_coordinator_service_action_restart**
> NodeServiceStatusProperties create_migration_coordinator_service_action_restart()

Restart, start or stop the migration coordinator service

Restart, start or stop the migration coordinator service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the migration coordinator service
    api_response = api_instance.create_migration_coordinator_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_migration_coordinator_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_migration_coordinator_service_action_start**
> NodeServiceStatusProperties create_migration_coordinator_service_action_start()

Restart, start or stop the migration coordinator service

Restart, start or stop the migration coordinator service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the migration coordinator service
    api_response = api_instance.create_migration_coordinator_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_migration_coordinator_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_migration_coordinator_service_action_stop**
> NodeServiceStatusProperties create_migration_coordinator_service_action_stop()

Restart, start or stop the migration coordinator service

Restart, start or stop the migration coordinator service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the migration coordinator service
    api_response = api_instance.create_migration_coordinator_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_migration_coordinator_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_network_route**
> NodeRouteProperties create_node_network_route(body)

Create node network route

Add a route to the NSX Manager routing table. For static routes, the route_type, interface_id, netmask, and destination are required parameters. For default routes, the route_type, gateway address, and interface_id are required. For blackhole routes, the route_type and destination are required. All other parameters are optional. When you add a static route, the scope and route_id are created automatically. When you add a default or blackhole route, the route_id is created automatically. The route_id is read-only, meaning that it cannot be modified. All other properties can be modified by deleting and readding the route. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeRouteProperties() # NodeRouteProperties | 

try:
    # Create node network route
    api_response = api_instance.create_node_network_route(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_node_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeRouteProperties**](NodeRouteProperties.md)|  | 

### Return type

[**NodeRouteProperties**](NodeRouteProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_stats_service_action_restart**
> NodeServiceStatusProperties create_node_stats_service_action_restart()

Restart, start or stop the NSX node-stats service

Restart, start or stop the NSX node-stats service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX node-stats service
    api_response = api_instance.create_node_stats_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_node_stats_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_stats_service_action_start**
> NodeServiceStatusProperties create_node_stats_service_action_start()

Restart, start or stop the NSX node-stats service

Restart, start or stop the NSX node-stats service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX node-stats service
    api_response = api_instance.create_node_stats_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_node_stats_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_stats_service_action_stop**
> NodeServiceStatusProperties create_node_stats_service_action_stop()

Restart, start or stop the NSX node-stats service

Restart, start or stop the NSX node-stats service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX node-stats service
    api_response = api_instance.create_node_stats_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_node_stats_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_message_bus_service_action_restart**
> NodeServiceStatusProperties create_nsx_message_bus_service_action_restart()

Restart, start or stop the NSX Message Bus service

Restart, start or stop the NSX Message Bus service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Message Bus service
    api_response = api_instance.create_nsx_message_bus_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_message_bus_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_message_bus_service_action_start**
> NodeServiceStatusProperties create_nsx_message_bus_service_action_start()

Restart, start or stop the NSX Message Bus service

Restart, start or stop the NSX Message Bus service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Message Bus service
    api_response = api_instance.create_nsx_message_bus_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_message_bus_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_message_bus_service_action_stop**
> NodeServiceStatusProperties create_nsx_message_bus_service_action_stop()

Restart, start or stop the NSX Message Bus service

Restart, start or stop the NSX Message Bus service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Message Bus service
    api_response = api_instance.create_nsx_message_bus_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_message_bus_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_ui_service_service_action_restart**
> NodeServiceStatusProperties create_nsx_ui_service_service_action_restart()

Restart, Start and Stop the ui service

Restart, Start and Stop the ui service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, Start and Stop the ui service
    api_response = api_instance.create_nsx_ui_service_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_ui_service_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_ui_service_service_action_start**
> NodeServiceStatusProperties create_nsx_ui_service_service_action_start()

Restart, Start and Stop the ui service

Restart, Start and Stop the ui service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, Start and Stop the ui service
    api_response = api_instance.create_nsx_ui_service_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_ui_service_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_ui_service_service_action_stop**
> NodeServiceStatusProperties create_nsx_ui_service_service_action_stop()

Restart, Start and Stop the ui service

Restart, Start and Stop the ui service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, Start and Stop the ui service
    api_response = api_instance.create_nsx_ui_service_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_ui_service_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_upgrade_agent_service_action_restart**
> NodeServiceStatusProperties create_nsx_upgrade_agent_service_action_restart()

Restart, start or stop the NSX upgrade agent service

Restart, start or stop the NSX upgrade agent service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX upgrade agent service
    api_response = api_instance.create_nsx_upgrade_agent_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_upgrade_agent_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_upgrade_agent_service_action_start**
> NodeServiceStatusProperties create_nsx_upgrade_agent_service_action_start()

Restart, start or stop the NSX upgrade agent service

Restart, start or stop the NSX upgrade agent service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX upgrade agent service
    api_response = api_instance.create_nsx_upgrade_agent_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_upgrade_agent_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nsx_upgrade_agent_service_action_stop**
> NodeServiceStatusProperties create_nsx_upgrade_agent_service_action_stop()

Restart, start or stop the NSX upgrade agent service

Restart, start or stop the NSX upgrade agent service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX upgrade agent service
    api_response = api_instance.create_nsx_upgrade_agent_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_nsx_upgrade_agent_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ntp_service_action_restart**
> NodeServiceStatusProperties create_ntp_service_action_restart()

Restart, start or stop the NTP service

Restart, start or stop the NTP service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NTP service
    api_response = api_instance.create_ntp_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ntp_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ntp_service_action_start**
> NodeServiceStatusProperties create_ntp_service_action_start()

Restart, start or stop the NTP service

Restart, start or stop the NTP service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NTP service
    api_response = api_instance.create_ntp_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ntp_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ntp_service_action_stop**
> NodeServiceStatusProperties create_ntp_service_action_stop()

Restart, start or stop the NTP service

Restart, start or stop the NTP service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NTP service
    api_response = api_instance.create_ntp_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ntp_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phonehome_coordinator_service_action_restart**
> NodeServiceStatusProperties create_phonehome_coordinator_service_action_restart()

Restart, start or stop Telemetry service

Restart, start or stop Telemetry service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop Telemetry service
    api_response = api_instance.create_phonehome_coordinator_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_phonehome_coordinator_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phonehome_coordinator_service_action_start**
> NodeServiceStatusProperties create_phonehome_coordinator_service_action_start()

Restart, start or stop Telemetry service

Restart, start or stop Telemetry service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop Telemetry service
    api_response = api_instance.create_phonehome_coordinator_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_phonehome_coordinator_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phonehome_coordinator_service_action_stop**
> NodeServiceStatusProperties create_phonehome_coordinator_service_action_stop()

Restart, start or stop Telemetry service

Restart, start or stop Telemetry service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop Telemetry service
    api_response = api_instance.create_phonehome_coordinator_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_phonehome_coordinator_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_platform_client_service_action_restart**
> NodeServiceStatusProperties create_platform_client_service_action_restart()

Restart, start or stop the NSX Platform Client service

Restart, start or stop the NSX Platform Client service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Platform Client service
    api_response = api_instance.create_platform_client_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_platform_client_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_platform_client_service_action_start**
> NodeServiceStatusProperties create_platform_client_service_action_start()

Restart, start or stop the NSX Platform Client service

Restart, start or stop the NSX Platform Client service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Platform Client service
    api_response = api_instance.create_platform_client_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_platform_client_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_platform_client_service_action_stop**
> NodeServiceStatusProperties create_platform_client_service_action_stop()

Restart, start or stop the NSX Platform Client service

Restart, start or stop the NSX Platform Client service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Platform Client service
    api_response = api_instance.create_platform_client_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_platform_client_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_service_action_restart**
> NodeServiceStatusProperties create_policy_service_action_restart()

Restart, start or stop the service

Restart, start or stop the service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_policy_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_policy_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_service_action_start**
> NodeServiceStatusProperties create_policy_service_action_start()

Restart, start or stop the service

Restart, start or stop the service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_policy_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_policy_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_service_action_stop**
> NodeServiceStatusProperties create_policy_service_action_stop()

Restart, start or stop the service

Restart, start or stop the service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_policy_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_policy_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proton_service_action_restart**
> NodeServiceStatusProperties create_proton_service_action_restart()

Restart, start or stop the service

Restart, start or stop the service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_proton_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_proton_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proton_service_action_start**
> NodeServiceStatusProperties create_proton_service_action_start()

Restart, start or stop the service

Restart, start or stop the service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_proton_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_proton_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proton_service_action_stop**
> NodeServiceStatusProperties create_proton_service_action_stop()

Restart, start or stop the service

Restart, start or stop the service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_proton_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_proton_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proxy_service_action_restart**
> create_proxy_service_action_restart()

Restart the http service

Restart the http service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart the http service
    api_instance.create_proxy_service_action_restart()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_proxy_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proxy_service_action_start**
> NodeServiceStatusProperties create_proxy_service_action_start()

Start the http service

Start the http service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Start the http service
    api_response = api_instance.create_proxy_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_proxy_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proxy_service_action_stop**
> create_proxy_service_action_stop()

Stop the http service

Stop the http service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Stop the http service
    api_instance.create_proxy_service_action_stop()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_proxy_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proxy_service_apply_certificate_action_apply_certificate**
> create_proxy_service_apply_certificate_action_apply_certificate(certificate_id)

Update http service certificate

Applies a security certificate to the http service. In the POST request, the CERTIFICATE_ID references a certificate created with the /api/v1/trust-management APIs. Issuing this request causes the http service to restart so that the service can begin using the new certificate. When the POST request succeeds, it doesn't return a valid response. The request times out because of the restart. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Update http service certificate
    api_instance.create_proxy_service_apply_certificate_action_apply_certificate(certificate_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_proxy_service_apply_certificate_action_apply_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Certificate ID | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rabbit_mq_service_action_restart**
> NodeServiceStatusProperties create_rabbit_mq_service_action_restart()

Restart, start or stop the Rabbit MQ service

Restart, start or stop the Rabbit MQ service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Rabbit MQ service
    api_response = api_instance.create_rabbit_mq_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_rabbit_mq_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rabbit_mq_service_action_start**
> NodeServiceStatusProperties create_rabbit_mq_service_action_start()

Restart, start or stop the Rabbit MQ service

Restart, start or stop the Rabbit MQ service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Rabbit MQ service
    api_response = api_instance.create_rabbit_mq_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_rabbit_mq_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rabbit_mq_service_action_stop**
> NodeServiceStatusProperties create_rabbit_mq_service_action_stop()

Restart, start or stop the Rabbit MQ service

Restart, start or stop the Rabbit MQ service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Rabbit MQ service
    api_response = api_instance.create_rabbit_mq_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_rabbit_mq_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_remote_directory_create_remote_directory**
> create_remote_directory_create_remote_directory(body)

Create directory in remote file server

Create a directory on the remote remote server. Supports only SFTP. You must provide the remote server's SSH fingerprint. See the <i>NSX Administration Guide</i> for information and instructions about finding the SSH fingerprint. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRemoteDirectoryProperties() # CreateRemoteDirectoryProperties | 

try:
    # Create directory in remote file server
    api_instance.create_remote_directory_create_remote_directory(body)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_remote_directory_create_remote_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRemoteDirectoryProperties**](CreateRemoteDirectoryProperties.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_service_action_restart**
> NodeServiceStatusProperties create_repository_service_action_restart()

Restart, start or stop the NSX install-upgrade service

Restart, start or stop the NSX install-upgrade service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX install-upgrade service
    api_response = api_instance.create_repository_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_repository_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_service_action_start**
> NodeServiceStatusProperties create_repository_service_action_start()

Restart, start or stop the NSX install-upgrade service

Restart, start or stop the NSX install-upgrade service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX install-upgrade service
    api_response = api_instance.create_repository_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_repository_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_service_action_stop**
> NodeServiceStatusProperties create_repository_service_action_stop()

Restart, start or stop the NSX install-upgrade service

Restart, start or stop the NSX install-upgrade service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX install-upgrade service
    api_response = api_instance.create_repository_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_repository_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_search_service_action_restart**
> NodeServiceStatusProperties create_search_service_action_restart()

Restart, start or stop the NSX Search service

Restart, start or stop the NSX Search service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Search service
    api_response = api_instance.create_search_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_search_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_search_service_action_start**
> NodeServiceStatusProperties create_search_service_action_start()

Restart, start or stop the NSX Search service

Restart, start or stop the NSX Search service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Search service
    api_response = api_instance.create_search_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_search_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_search_service_action_stop**
> NodeServiceStatusProperties create_search_service_action_stop()

Restart, start or stop the NSX Search service

Restart, start or stop the NSX Search service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Search service
    api_response = api_instance.create_search_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_search_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snmp_service_action_restart**
> NodeServiceStatusProperties create_snmp_service_action_restart()

Restart, start or stop the SNMP service

Restart, start or stop the SNMP service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the SNMP service
    api_response = api_instance.create_snmp_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_snmp_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snmp_service_action_start**
> NodeServiceStatusProperties create_snmp_service_action_start()

Restart, start or stop the SNMP service

Restart, start or stop the SNMP service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the SNMP service
    api_response = api_instance.create_snmp_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_snmp_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snmp_service_action_stop**
> NodeServiceStatusProperties create_snmp_service_action_stop()

Restart, start or stop the SNMP service

Restart, start or stop the SNMP service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the SNMP service
    api_response = api_instance.create_snmp_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_snmp_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_service_action_notify_mpa_restart**
> NodeServiceStatusProperties create_ssh_service_action_notify_mpa_restart()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_notify_mpa_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ssh_service_action_notify_mpa_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_service_action_notify_mpa_start**
> NodeServiceStatusProperties create_ssh_service_action_notify_mpa_start()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_notify_mpa_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ssh_service_action_notify_mpa_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_service_action_notify_mpa_stop**
> NodeServiceStatusProperties create_ssh_service_action_notify_mpa_stop()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_notify_mpa_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ssh_service_action_notify_mpa_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_service_action_restart**
> NodeServiceStatusProperties create_ssh_service_action_restart()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ssh_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_service_action_start**
> NodeServiceStatusProperties create_ssh_service_action_start()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ssh_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_service_action_stop**
> NodeServiceStatusProperties create_ssh_service_action_stop()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ssh_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint**
> create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint(body)

Remove a host's fingerprint from known hosts file

Remove a host's fingerprint from known hosts file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.KnownHostParameter() # KnownHostParameter | 

try:
    # Remove a host's fingerprint from known hosts file
    api_instance.create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint(body)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KnownHostParameter**](KnownHostParameter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_syslog_service_action_restart**
> NodeServiceStatusProperties create_syslog_service_action_restart()

Restart, start or stop the syslog service

Restart, start or stop the syslog service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the syslog service
    api_response = api_instance.create_syslog_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_syslog_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_syslog_service_action_start**
> NodeServiceStatusProperties create_syslog_service_action_start()

Restart, start or stop the syslog service

Restart, start or stop the syslog service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the syslog service
    api_response = api_instance.create_syslog_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_syslog_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_syslog_service_action_stop**
> NodeServiceStatusProperties create_syslog_service_action_stop()

Restart, start or stop the syslog service

Restart, start or stop the syslog service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the syslog service
    api_response = api_instance.create_syslog_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->create_syslog_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_elete_rabbit_mq_management_port**
> d_elete_rabbit_mq_management_port()

Delete RabbitMQ management port

Delete RabbitMQ management port

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Delete RabbitMQ management port
    api_instance.d_elete_rabbit_mq_management_port()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->d_elete_rabbit_mq_management_port: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appliance_management_task**
> delete_appliance_management_task(task_id)

Delete task

Delete task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to delete

try:
    # Delete task
    api_instance.delete_appliance_management_task(task_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->delete_appliance_management_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(file_name)

Delete file

Delete file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to delete

try:
    # Delete file
    api_instance.delete_file(file_name)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_network_route**
> delete_node_network_route(route_id)

Delete node network route

Delete a route from the NSX Manager routing table. You can modify an existing route by deleting it and then posting the modified version of the route. To verify, remove the route ID from the URI, issue a GET request, and note the absense of the deleted route. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
route_id = 'route_id_example' # str | ID of route to delete

try:
    # Delete node network route
    api_instance.delete_node_network_route(route_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->delete_node_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**| ID of route to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_syslog_exporter**
> delete_node_syslog_exporter(exporter_name)

Delete node syslog exporter

Removes a specified rule from the collection of syslog exporter rules. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
exporter_name = 'exporter_name_example' # str | Name of syslog exporter to delete

try:
    # Delete node syslog exporter
    api_instance.delete_node_syslog_exporter(exporter_name)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->delete_node_syslog_exporter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exporter_name** | **str**| Name of syslog exporter to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_user_ssh_key_remove_ssh_key**
> delete_node_user_ssh_key_remove_ssh_key(body, userid)

Remove SSH public key from authorized_keys file for node user

Remove SSH public key from authorized_keys file for node user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.SshKeyBaseProperties() # SshKeyBaseProperties | 
userid = 'userid_example' # str | User id of the user

try:
    # Remove SSH public key from authorized_keys file for node user
    api_instance.delete_node_user_ssh_key_remove_ssh_key(body, userid)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->delete_node_user_ssh_key_remove_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SshKeyBaseProperties**](SshKeyBaseProperties.md)|  | 
 **userid** | **str**| User id of the user | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_support_bundles_async_response_delete_async_response**
> delete_support_bundles_async_response_delete_async_response()

Delete existing support bundles waiting to be downloaded

Delete existing support bundles waiting to be downloaded.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Delete existing support bundles waiting to be downloaded
    api_instance.delete_support_bundles_async_response_delete_async_response()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->delete_support_bundles_async_response_delete_async_response: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_controller_profiler_status**
> ControllerProfilerProperties get_controller_profiler_status()

Get the status (Enabled/Disabled) of controller profiler

Get the status (Enabled/Disabled) of controller profiler

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Get the status (Enabled/Disabled) of controller profiler
    api_response = api_instance.get_controller_profiler_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->get_controller_profiler_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ControllerProfilerProperties**](ControllerProfilerProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_mandatory_access_control**
> MandatoryAccessControlProperties get_node_mandatory_access_control()

Gets the enable status for Mandatory Access Control

Gets the enable status for Mandatory Access Control

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Gets the enable status for Mandatory Access Control
    api_response = api_instance.get_node_mandatory_access_control()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->get_node_mandatory_access_control: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MandatoryAccessControlProperties**](MandatoryAccessControlProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_mandatory_access_control_report**
> get_node_mandatory_access_control_report()

Get the report for Mandatory Access Control

Get the report for Mandatory Access Control

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Get the report for Mandatory Access Control
    api_instance.get_node_mandatory_access_control_report()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->get_node_mandatory_access_control_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_delete_cluster_central_api**
> invoke_delete_cluster_central_api(target_node_id, target_uri)

Invoke DELETE request on target cluster node

Invoke DELETE request on target cluster node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke DELETE request on target cluster node
    api_instance.invoke_delete_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_delete_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_delete_fabric_central_api**
> invoke_delete_fabric_central_api(target_node_id, target_uri)

Invoke DELETE request on target fabric node

Invoke DELETE request on target fabric node. This api is deprecated as part of FN+TN unification. Please use Transport Node API DELETE /transport-nodes/&lt;transport-node-id&gt;/&lt;target-node-id&gt;/&lt;target-uri&gt; 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke DELETE request on target fabric node
    api_instance.invoke_delete_fabric_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_delete_fabric_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_delete_transport_node_central_api**
> invoke_delete_transport_node_central_api(target_node_id, target_uri)

Invoke DELETE request on target transport node

Invoke DELETE request on target transport node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke DELETE request on target transport node
    api_instance.invoke_delete_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_delete_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_get_cluster_central_api**
> invoke_get_cluster_central_api(target_node_id, target_uri)

Invoke GET request on target cluster node

Invoke GET request on target cluster node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke GET request on target cluster node
    api_instance.invoke_get_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_get_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_get_fabric_central_api**
> invoke_get_fabric_central_api(target_node_id, target_uri)

Invoke GET request on target fabric node

Invoke GET request on target fabric node. This api is deprecated as part of FN+TN unification. Please use Transport Node API GET /transport-nodes/&lt;transport-node-id&gt;/&lt;target-node-id&gt;/&lt;target-uri&gt; 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke GET request on target fabric node
    api_instance.invoke_get_fabric_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_get_fabric_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_get_transport_node_central_api**
> invoke_get_transport_node_central_api(target_node_id, target_uri)

Invoke GET request on target transport node

Invoke GET request on target transport node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke GET request on target transport node
    api_instance.invoke_get_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_get_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_post_cluster_central_api**
> invoke_post_cluster_central_api(target_node_id, target_uri)

Invoke POST request on target cluster node

Invoke POST request on target cluster node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke POST request on target cluster node
    api_instance.invoke_post_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_post_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_post_fabric_central_api**
> invoke_post_fabric_central_api(target_node_id, target_uri)

Invoke POST request on target fabric node

Invoke POST request on target fabric node. This api is deprecated as part of FN+TN unification. Please use Transport Node API POST /transport-nodes/&lt;transport-node-id&gt;/&lt;target-node-id&gt;/&lt;target-uri&gt; 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke POST request on target fabric node
    api_instance.invoke_post_fabric_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_post_fabric_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_post_transport_node_central_api**
> invoke_post_transport_node_central_api(target_node_id, target_uri)

Invoke POST request on target transport node

Invoke POST request on target transport node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke POST request on target transport node
    api_instance.invoke_post_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_post_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_put_cluster_central_api**
> invoke_put_cluster_central_api(target_node_id, target_uri)

Invoke PUT request on target cluster node

Invoke PUT request on target cluster node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke PUT request on target cluster node
    api_instance.invoke_put_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_put_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_put_fabric_central_api**
> invoke_put_fabric_central_api(target_node_id, target_uri)

Invoke PUT request on target fabric node

Invoke PUT request on target fabric node. This api is deprecated as part of FN+TN unification. Please use Transport Node API PUT /transport-nodes/&lt;transport-node-id&gt;/&lt;target-node-id&gt;/&lt;target-uri&gt; 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke PUT request on target fabric node
    api_instance.invoke_put_fabric_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_put_fabric_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_put_transport_node_central_api**
> invoke_put_transport_node_central_api(target_node_id, target_uri)

Invoke PUT request on target transport node

Invoke PUT request on target transport node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke PUT request on target transport node
    api_instance.invoke_put_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->invoke_put_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_appliance_management_tasks**
> ApplianceManagementTaskListResult list_appliance_management_tasks(fields=fields, request_method=request_method, request_path=request_path, request_uri=request_uri, status=status, user=user)

List appliance management tasks

List appliance management tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
fields = 'fields_example' # str | Fields to include in query results (optional)
request_method = 'request_method_example' # str | Request method(s) to include in query result (optional)
request_path = 'request_path_example' # str | Request URI path(s) to include in query result (optional)
request_uri = 'request_uri_example' # str | Request URI(s) to include in query result (optional)
status = 'status_example' # str | Status(es) to include in query result (optional)
user = 'user_example' # str | Names of users to include in query result (optional)

try:
    # List appliance management tasks
    api_response = api_instance.list_appliance_management_tasks(fields=fields, request_method=request_method, request_path=request_path, request_uri=request_uri, status=status, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_appliance_management_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to include in query results | [optional] 
 **request_method** | **str**| Request method(s) to include in query result | [optional] 
 **request_path** | **str**| Request URI path(s) to include in query result | [optional] 
 **request_uri** | **str**| Request URI(s) to include in query result | [optional] 
 **status** | **str**| Status(es) to include in query result | [optional] 
 **user** | **str**| Names of users to include in query result | [optional] 

### Return type

[**ApplianceManagementTaskListResult**](ApplianceManagementTaskListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> FilePropertiesListResult list_files()

List node files

List node files

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # List node files
    api_response = api_instance.list_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilePropertiesListResult**](FilePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_interfaces**
> NodeNetworkInterfacePropertiesListResult list_node_interfaces()

List the NSX Manager's Network Interfaces

Returns the number of interfaces on the NSX Manager appliance and detailed information about each interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network mask, and the IP configuration method (static or DHCP). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # List the NSX Manager's Network Interfaces
    api_response = api_instance.list_node_interfaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_node_interfaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNetworkInterfacePropertiesListResult**](NodeNetworkInterfacePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_network_routes**
> NodeRoutePropertiesListResult list_node_network_routes()

List node network routes

Returns detailed information about each route in the NSX Manager routing table. Route information includes the route type (default, static, and so on), a unique route identifier, the route metric, the protocol from which the route was learned, the route source (which is the preferred egress interface), the route destination, and the route scope. The route scope refers to the distance to the destination network: The \"host\" scope leads to a destination address on the NSX Manager, such as a loopback address; the \"link\" scope leads to a destination on the local network; and the \"global\" scope leads to addresses that are more than one hop away. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # List node network routes
    api_response = api_instance.list_node_network_routes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_node_network_routes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeRoutePropertiesListResult**](NodeRoutePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_processes**
> NodeProcessPropertiesListResult list_node_processes()

List node processes

Returns the number of processes and information about each process. Process information includes 1) mem_resident, which is roughly equivalent to the amount of RAM, in bytes, currently used by the process, 2) parent process ID (ppid), 3) process name, 4) process up time in milliseconds, 5) mem_used, wich is the amount of virtual memory used by the process, in bytes, 6) process start time, in milliseconds since epoch, 7) process ID (pid), 8) CPU time, both user and the system, consumed by the process in milliseconds. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # List node processes
    api_response = api_instance.list_node_processes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_node_processes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeProcessPropertiesListResult**](NodeProcessPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_services**
> NodeServicePropertiesListResult list_node_services()

List node services

Returns a list of all services available on the NSX Manager applicance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # List node services
    api_response = api_instance.list_node_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_node_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServicePropertiesListResult**](NodeServicePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_syslog_exporters**
> NodeSyslogExporterPropertiesListResult list_node_syslog_exporters()

List node syslog exporters

Returns the collection of registered syslog exporter rules, if any. The rules specify the collector IP address and port, and the protocol to use. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # List node syslog exporters
    api_response = api_instance.list_node_syslog_exporters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_node_syslog_exporters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSyslogExporterPropertiesListResult**](NodeSyslogExporterPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_user_ssh_keys**
> SshKeyPropertiesListResult list_node_user_ssh_keys(userid)

List SSH keys from authorized_keys file for node user

Returns a list of all SSH keys from authorized_keys file for node user 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
userid = 'userid_example' # str | User id of the user

try:
    # List SSH keys from authorized_keys file for node user
    api_response = api_instance.list_node_user_ssh_keys(userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_node_user_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User id of the user | 

### Return type

[**SshKeyPropertiesListResult**](SshKeyPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_users**
> NodeUserPropertiesListResult list_node_users()

List node users

Returns the list of users configued to log in to the NSX appliance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # List node users
    api_response = api_instance.list_node_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->list_node_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeUserPropertiesListResult**](NodeUserPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_node_syslog_exporter**
> NodeSyslogExporterProperties post_node_syslog_exporter(body)

Add node syslog exporter

Adds a rule for exporting syslog information to a specified server. The required parameters are the rule name (exporter_name); severity level (emerg, alert, crit, and so on); transmission protocol (TCP or UDP); and server IP address or hostname. The optional parameters are the syslog port number, which can be 1 through 65,535 (514, by default); facility level to use when logging messages to syslog (kern, user, mail, and so on); and message IDs (msgids), which identify the types of messages to export. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSyslogExporterProperties() # NodeSyslogExporterProperties | 

try:
    # Add node syslog exporter
    api_response = api_instance.post_node_syslog_exporter(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->post_node_syslog_exporter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSyslogExporterProperties**](NodeSyslogExporterProperties.md)|  | 

### Return type

[**NodeSyslogExporterProperties**](NodeSyslogExporterProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_appliance_management_service**
> NodeServiceProperties read_appliance_management_service()

Read appliance management service properties

Read appliance management service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read appliance management service properties
    api_response = api_instance.read_appliance_management_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_appliance_management_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_appliance_management_service_status**
> NodeServiceStatusProperties read_appliance_management_service_status()

Read appliance management service status

Read appliance management service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read appliance management service status
    api_response = api_instance.read_appliance_management_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_appliance_management_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_appliance_management_task_properties**
> ApplianceManagementTaskProperties read_appliance_management_task_properties(task_id, suppress_redirect=suppress_redirect)

Read task properties

Read task properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to read
suppress_redirect = true # bool | Suppress redirect status if applicable (optional)

try:
    # Read task properties
    api_response = api_instance.read_appliance_management_task_properties(task_id, suppress_redirect=suppress_redirect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_appliance_management_task_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to read | 
 **suppress_redirect** | **bool**| Suppress redirect status if applicable | [optional] 

### Return type

[**ApplianceManagementTaskProperties**](ApplianceManagementTaskProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_appliance_node_status**
> NodeStatusProperties read_appliance_node_status()

Read node status

Returns information about the NSX Manager appliance's file system, CPU, memory, disk usage, and uptime. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read node status
    api_response = api_instance.read_appliance_node_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_appliance_node_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeStatusProperties**](NodeStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_async_appliance_management_task_response**
> read_async_appliance_management_task_response(task_id)

Read asynchronous task response

Read asynchronous task response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to read

try:
    # Read asynchronous task response
    api_instance.read_async_appliance_management_task_response(task_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_async_appliance_management_task_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to read | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_auth_provider_vidm**
> NodeAuthProviderVidmProperties read_auth_provider_vidm()

Read AAA provider vIDM properties

Read AAA provider vIDM properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read AAA provider vIDM properties
    api_response = api_instance.read_auth_provider_vidm()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_auth_provider_vidm: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeAuthProviderVidmProperties**](NodeAuthProviderVidmProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_auth_provider_vidm_status**
> NodeAuthProviderVidmStatus read_auth_provider_vidm_status()

Read AAA provider vIDM status

Read AAA provider vIDM status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read AAA provider vIDM status
    api_response = api_instance.read_auth_provider_vidm_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_auth_provider_vidm_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeAuthProviderVidmStatus**](NodeAuthProviderVidmStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_boot_manager_service**
> NodeServiceProperties read_cluster_boot_manager_service()

Read cluster boot manager service properties

Read cluster boot manager service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster boot manager service properties
    api_response = api_instance.read_cluster_boot_manager_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_cluster_boot_manager_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_boot_manager_service_status**
> NodeServiceStatusProperties read_cluster_boot_manager_service_status()

Read cluster boot manager service status

Read cluster boot manager service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster boot manager service status
    api_response = api_instance.read_cluster_boot_manager_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_cluster_boot_manager_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cminventory_service**
> NodeServiceProperties read_cminventory_service()

Read cm inventory service properties

Read cm inventory service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read cm inventory service properties
    api_response = api_instance.read_cminventory_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_cminventory_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cminventory_service_status**
> NodeServiceStatusProperties read_cminventory_service_status()

Read manager service status

Read manager service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read manager service status
    api_response = api_instance.read_cminventory_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_cminventory_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_controller_server_certificate**
> CertificateKeyPair read_controller_server_certificate()

Read controller server certificate properties

Read controller server certificate properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read controller server certificate properties
    api_response = api_instance.read_controller_server_certificate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_controller_server_certificate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateKeyPair**](CertificateKeyPair.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_controller_server_service**
> NodeServiceProperties read_controller_server_service()

Read controller service properties

Read controller service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read controller service properties
    api_response = api_instance.read_controller_server_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_controller_server_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_controller_server_service_status**
> NodeServiceStatusProperties read_controller_server_service_status()

Read controller service status

Read controller service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read controller service status
    api_response = api_instance.read_controller_server_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_controller_server_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_file**
> read_file(file_name)

Read file contents

Read file contents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to read

try:
    # Read file contents
    api_instance.read_file(file_name)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to read | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_file_properties**
> FileProperties read_file_properties(file_name)

Read file properties

Read file properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to retrieve information about

try:
    # Read file properties
    api_response = api_instance.read_file_properties(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_file_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to retrieve information about | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_file_thumbprint**
> FileThumbprint read_file_thumbprint(file_name)

Read file thumbprint

Read file thumbprint

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file for which thumbprint should be computed

try:
    # Read file thumbprint
    api_response = api_instance.read_file_thumbprint(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_file_thumbprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file for which thumbprint should be computed | 

### Return type

[**FileThumbprint**](FileThumbprint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_liagent_service**
> NodeServiceProperties read_liagent_service()

Read liagent service properties

Read liagent service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read liagent service properties
    api_response = api_instance.read_liagent_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_liagent_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_liagent_service_status**
> NodeServiceStatusProperties read_liagent_service_status()

Read liagent service status

Read liagent service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read liagent service status
    api_response = api_instance.read_liagent_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_liagent_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_migration_coordinator_service**
> NodeServiceProperties read_migration_coordinator_service()

Read migration coordinator service properties

Read migration coordinator service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read migration coordinator service properties
    api_response = api_instance.read_migration_coordinator_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_migration_coordinator_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_migration_coordinator_service_status**
> NodeServiceStatusProperties read_migration_coordinator_service_status()

Read migration coordinator service status

Read migration coordinator service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read migration coordinator service status
    api_response = api_instance.read_migration_coordinator_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_migration_coordinator_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_interface_statistics**
> NodeInterfaceStatisticsProperties read_network_interface_statistics(interface_id)

Read the NSX Manager's Network Interface Statistics

On the specified interface, returns the number of received (rx), transmitted (tx), and dropped packets; the number of bytes and errors received and transmitted on the interface; and the number of detected collisions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
interface_id = 'interface_id_example' # str | ID of interface to read

try:
    # Read the NSX Manager's Network Interface Statistics
    api_response = api_instance.read_network_interface_statistics(interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_network_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **str**| ID of interface to read | 

### Return type

[**NodeInterfaceStatisticsProperties**](NodeInterfaceStatisticsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_properties**
> NodeNetworkProperties read_network_properties()

Read network configuration properties

Read network configuration properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read network configuration properties
    api_response = api_instance.read_network_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_network_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNetworkProperties**](NodeNetworkProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_interface**
> NodeNetworkInterfaceProperties read_node_interface(interface_id)

Read the NSX Manager's Network Interface

Returns detailed information about the specified interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network  mask, and the IP configuration method. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
interface_id = 'interface_id_example' # str | ID of interface to read

try:
    # Read the NSX Manager's Network Interface
    api_response = api_instance.read_node_interface(interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **str**| ID of interface to read | 

### Return type

[**NodeNetworkInterfaceProperties**](NodeNetworkInterfaceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_name_servers**
> NodeNameServersProperties read_node_name_servers()

Read the NSX Manager's Name Servers

Returns the list of servers that the NSX Manager node uses to look up IP addresses associated with given domain names. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read the NSX Manager's Name Servers
    api_response = api_instance.read_node_name_servers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_name_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNameServersProperties**](NodeNameServersProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_network_route**
> NodeRouteProperties read_node_network_route(route_id)

Read node network route

Returns detailed information about a specified route in the NSX Manager routing table. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
route_id = 'route_id_example' # str | ID of route to read

try:
    # Read node network route
    api_response = api_instance.read_node_network_route(route_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**| ID of route to read | 

### Return type

[**NodeRouteProperties**](NodeRouteProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_process**
> NodeProcessProperties read_node_process(process_id)

Read node process

Returns information for a specified process ID (pid).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
process_id = 'process_id_example' # str | ID of process to read

try:
    # Read node process
    api_response = api_instance.read_node_process(process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| ID of process to read | 

### Return type

[**NodeProcessProperties**](NodeProcessProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_properties**
> NodeProperties read_node_properties()

Read node properties

Returns information about the NSX appliance. Information includes release number, time zone, system time, kernel version, message of the day (motd), and host name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read node properties
    api_response = api_instance.read_node_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeProperties**](NodeProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_search_domains**
> NodeSearchDomainsProperties read_node_search_domains()

Read the NSX Manager's Search Domains

Returns the domain list that the NSX Manager node uses to complete unqualified host names. When a host name does not include a fully qualified domain name (FQDN), the NSX Management node appends the first-listed domain name to the host name before the host name is looked up. The NSX Management node continues this for each entry in the domain list until it finds a match. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read the NSX Manager's Search Domains
    api_response = api_instance.read_node_search_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_search_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSearchDomainsProperties**](NodeSearchDomainsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_stats_service**
> NodeServiceProperties read_node_stats_service()

Read NSX node-stats service properties

Read NSX node-stats service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX node-stats service properties
    api_response = api_instance.read_node_stats_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_stats_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_stats_service_status**
> NodeServiceStatusProperties read_node_stats_service_status()

Read NSX node-stats service status

Read NSX node-stats service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX node-stats service status
    api_response = api_instance.read_node_stats_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_stats_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_support_bundle**
> read_node_support_bundle(all=all)

Read node support bundle

Read node support bundle

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
all = true # bool | Include all files (optional)

try:
    # Read node support bundle
    api_instance.read_node_support_bundle(all=all)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_support_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Include all files | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_syslog_exporter**
> NodeSyslogExporterProperties read_node_syslog_exporter(exporter_name)

Read node syslog exporter

Returns information about a specific syslog collection point.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
exporter_name = 'exporter_name_example' # str | Name of syslog exporter

try:
    # Read node syslog exporter
    api_response = api_instance.read_node_syslog_exporter(exporter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_syslog_exporter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exporter_name** | **str**| Name of syslog exporter | 

### Return type

[**NodeSyslogExporterProperties**](NodeSyslogExporterProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_user**
> NodeUserProperties read_node_user(userid)

Read node user

Returns information about a specified user who is configued to log in to the NSX appliance 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
userid = 'userid_example' # str | User id of the user

try:
    # Read node user
    api_response = api_instance.read_node_user(userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User id of the user | 

### Return type

[**NodeUserProperties**](NodeUserProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_version**
> NodeVersion read_node_version()

Read node version

Read node version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read node version
    api_response = api_instance.read_node_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_node_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeVersion**](NodeVersion.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_nsx_message_bus_service**
> NodeServiceProperties read_nsx_message_bus_service()

Read NSX Message Bus service properties

Read NSX Message Bus service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Message Bus service properties
    api_response = api_instance.read_nsx_message_bus_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_nsx_message_bus_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_nsx_message_bus_service_status**
> NodeServiceStatusProperties read_nsx_message_bus_service_status()

Read NSX Message Bus service status

Read NSX Message Bus service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Message Bus service status
    api_response = api_instance.read_nsx_message_bus_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_nsx_message_bus_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_nsx_ui_service_service**
> NodeServiceProperties read_nsx_ui_service_service()

Read ui service properties

Read ui service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read ui service properties
    api_response = api_instance.read_nsx_ui_service_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_nsx_ui_service_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_nsx_ui_service_service_status**
> NodeServiceStatusProperties read_nsx_ui_service_service_status()

Read ui service status

Read ui service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read ui service status
    api_response = api_instance.read_nsx_ui_service_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_nsx_ui_service_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_nsx_upgrade_agent_service**
> NodeServiceProperties read_nsx_upgrade_agent_service()

Read NSX upgrade Agent service properties

Read NSX upgrade Agent service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX upgrade Agent service properties
    api_response = api_instance.read_nsx_upgrade_agent_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_nsx_upgrade_agent_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_nsx_upgrade_agent_service_status**
> NodeServiceStatusProperties read_nsx_upgrade_agent_service_status()

Read Nsx upgrade agent service status

Read Nsx upgrade agent service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read Nsx upgrade agent service status
    api_response = api_instance.read_nsx_upgrade_agent_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_nsx_upgrade_agent_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ntp_service**
> NodeNtpServiceProperties read_ntp_service()

Read NTP service properties

Read NTP service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NTP service properties
    api_response = api_instance.read_ntp_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_ntp_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNtpServiceProperties**](NodeNtpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ntp_service_status**
> NodeServiceStatusProperties read_ntp_service_status()

Read NTP service status

Read NTP service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NTP service status
    api_response = api_instance.read_ntp_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_ntp_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_phonehome_coordinator_service**
> NodeServiceProperties read_phonehome_coordinator_service()

Read Telemetry service properties

Read Telemetry service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read Telemetry service properties
    api_response = api_instance.read_phonehome_coordinator_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_phonehome_coordinator_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_phonehome_coordinator_service_status**
> NodeServiceStatusProperties read_phonehome_coordinator_service_status()

Read Telemetry service status

Read Telemetry service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read Telemetry service status
    api_response = api_instance.read_phonehome_coordinator_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_phonehome_coordinator_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_platform_client_service**
> NodeServiceProperties read_platform_client_service()

Read NSX Platform Client service properties

Read NSX Platform Client service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Platform Client service properties
    api_response = api_instance.read_platform_client_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_platform_client_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_platform_client_service_status**
> NodeServiceStatusProperties read_platform_client_service_status()

Read NSX Platform Client service status

Read NSX Platform Client service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Platform Client service status
    api_response = api_instance.read_platform_client_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_platform_client_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_policy_service**
> NodePolicyServiceProperties read_policy_service()

Read service properties

Read service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read service properties
    api_response = api_instance.read_policy_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_policy_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodePolicyServiceProperties**](NodePolicyServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_policy_service_status**
> NodeServiceStatusProperties read_policy_service_status()

Read service status

Read service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read service status
    api_response = api_instance.read_policy_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_policy_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_proton_service**
> NodeProtonServiceProperties read_proton_service()

Read service properties

Read service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read service properties
    api_response = api_instance.read_proton_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_proton_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeProtonServiceProperties**](NodeProtonServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_proton_service_status**
> NodeServiceStatusProperties read_proton_service_status()

Read service status

Read service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read service status
    api_response = api_instance.read_proton_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_proton_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_proxy_service**
> NodeHttpServiceProperties read_proxy_service()

Read http service properties

This API is deprecated.  Read the configuration of the http service by calling the GET /api/v1/cluster/api-service API. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read http service properties
    api_response = api_instance.read_proxy_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_proxy_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeHttpServiceProperties**](NodeHttpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_proxy_service_status**
> NodeServiceStatusProperties read_proxy_service_status()

Read http service status

Read http service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read http service status
    api_response = api_instance.read_proxy_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_proxy_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_rabbit_mq_service**
> NodeServiceProperties read_rabbit_mq_service()

Read Rabbit MQ service properties

Read Rabbit MQ service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read Rabbit MQ service properties
    api_response = api_instance.read_rabbit_mq_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_rabbit_mq_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_rabbit_mq_service_status**
> NodeServiceStatusProperties read_rabbit_mq_service_status()

Read Rabbit MQ service status

Read Rabbit MQ service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read Rabbit MQ service status
    api_response = api_instance.read_rabbit_mq_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_rabbit_mq_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_repository_service**
> NodeInstallUpgradeServiceProperties read_repository_service()

Read NSX install-upgrade service properties

Read NSX install-upgrade service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX install-upgrade service properties
    api_response = api_instance.read_repository_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_repository_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeInstallUpgradeServiceProperties**](NodeInstallUpgradeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_repository_service_status**
> NodeServiceStatusProperties read_repository_service_status()

Read NSX install-upgrade service status

Read NSX install-upgrade service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX install-upgrade service status
    api_response = api_instance.read_repository_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_repository_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_search_service**
> NodeServiceProperties read_search_service()

Read NSX Search service properties

Read NSX Search service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Search service properties
    api_response = api_instance.read_search_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_search_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_search_service_status**
> NodeServiceStatusProperties read_search_service_status()

Read NSX Search service status

Read NSX Search service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Search service status
    api_response = api_instance.read_search_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_search_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_snmp_service**
> NodeSnmpServiceProperties read_snmp_service()

Read SNMP service properties

Read SNMP service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read SNMP service properties
    api_response = api_instance.read_snmp_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_snmp_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSnmpServiceProperties**](NodeSnmpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_snmp_service_status**
> NodeServiceStatusProperties read_snmp_service_status()

Read SNMP service status

Read SNMP service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read SNMP service status
    api_response = api_instance.read_snmp_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_snmp_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_snmpv3_engine_id**
> NodeSnmpV3EngineID read_snmpv3_engine_id()

Read SNMP V3 Engine ID

Read SNMP V3 Engine ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read SNMP V3 Engine ID
    api_response = api_instance.read_snmpv3_engine_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_snmpv3_engine_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSnmpV3EngineID**](NodeSnmpV3EngineID.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ssh_service**
> NodeSshServiceProperties read_ssh_service()

Read ssh service properties

Read ssh service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read ssh service properties
    api_response = api_instance.read_ssh_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_ssh_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSshServiceProperties**](NodeSshServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ssh_service_status**
> NodeServiceStatusProperties read_ssh_service_status()

Read ssh service status

Read ssh service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read ssh service status
    api_response = api_instance.read_ssh_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_ssh_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_syslog_service**
> NodeServiceProperties read_syslog_service()

Read syslog service properties

Read syslog service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read syslog service properties
    api_response = api_instance.read_syslog_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_syslog_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_syslog_service_status**
> NodeServiceStatusProperties read_syslog_service_status()

Read syslog service status

Read syslog service status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read syslog service status
    api_response = api_instance.read_syslog_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->read_syslog_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_policy_service_logging_level_action_reset_manager_logging_levels**
> reset_policy_service_logging_level_action_reset_manager_logging_levels()

Reset the logging levels to default values

Reset the logging levels to default values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Reset the logging levels to default values
    api_instance.reset_policy_service_logging_level_action_reset_manager_logging_levels()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->reset_policy_service_logging_level_action_reset_manager_logging_levels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_proton_service_logging_level_action_reset_manager_logging_levels**
> reset_proton_service_logging_level_action_reset_manager_logging_levels()

Reset the logging levels to default values

Reset the logging levels to default values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Reset the logging levels to default values
    api_instance.reset_proton_service_logging_level_action_reset_manager_logging_levels()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->reset_proton_service_logging_level_action_reset_manager_logging_levels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_or_shutdown_node_restart**
> restart_or_shutdown_node_restart()

Restart or shutdown node

Restarts or shuts down the NSX appliance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart or shutdown node
    api_instance.restart_or_shutdown_node_restart()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->restart_or_shutdown_node_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_or_shutdown_node_shutdown**
> restart_or_shutdown_node_shutdown()

Restart or shutdown node

Restarts or shuts down the NSX appliance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart or shutdown node
    api_instance.restart_or_shutdown_node_shutdown()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->restart_or_shutdown_node_shutdown: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_controller_profiler**
> set_controller_profiler(body)

Enable or disable controller profiler

Enable or disable controller profiler

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.ControllerProfilerProperties() # ControllerProfilerProperties | 

try:
    # Enable or disable controller profiler
    api_instance.set_controller_profiler(body)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->set_controller_profiler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ControllerProfilerProperties**](ControllerProfilerProperties.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_node_mandatory_access_control**
> MandatoryAccessControlProperties set_node_mandatory_access_control(body)

Enable or disable  Mandatory Access Control

Enable or disable  Mandatory Access Control

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.MandatoryAccessControlProperties() # MandatoryAccessControlProperties | 

try:
    # Enable or disable  Mandatory Access Control
    api_response = api_instance.set_node_mandatory_access_control(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->set_node_mandatory_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MandatoryAccessControlProperties**](MandatoryAccessControlProperties.md)|  | 

### Return type

[**MandatoryAccessControlProperties**](MandatoryAccessControlProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_rabbit_mq_management_port**
> set_rabbit_mq_management_port()

Set RabbitMQ management port

Set RabbitMQ management port

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Set RabbitMQ management port
    api_instance.set_rabbit_mq_management_port()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->set_rabbit_mq_management_port: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_node_status_clear_bootup_error**
> NodeStatusProperties update_appliance_node_status_clear_bootup_error()

Update node status

Clear node bootup status 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Update node status
    api_response = api_instance.update_appliance_node_status_clear_bootup_error()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_appliance_node_status_clear_bootup_error: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeStatusProperties**](NodeStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_provider_vidm**
> NodeAuthProviderVidmProperties update_auth_provider_vidm(body)

Update AAA provider vIDM properties

Update AAA provider vIDM properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeAuthProviderVidmProperties() # NodeAuthProviderVidmProperties | 

try:
    # Update AAA provider vIDM properties
    api_response = api_instance.update_auth_provider_vidm(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_auth_provider_vidm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeAuthProviderVidmProperties**](NodeAuthProviderVidmProperties.md)|  | 

### Return type

[**NodeAuthProviderVidmProperties**](NodeAuthProviderVidmProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileProperties update_file(file_name)

Replace file contents

Replace file contents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to replace

try:
    # Replace file contents
    api_response = api_instance.update_file(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to replace | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_interface**
> NodeNetworkInterfaceProperties update_node_interface(body, interface_id)

Update the NSX Manager's Network Interface

Updates the specified interface properties. You cannot change the properties <code>ip_configuration</code>, <code>ip_addresses</code>, or <code>plane</code>. NSX Manager must have a static IP address. You must use NSX CLI to configure a controller or an edge node. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeNetworkInterfaceProperties() # NodeNetworkInterfaceProperties | 
interface_id = 'interface_id_example' # str | ID of interface to update

try:
    # Update the NSX Manager's Network Interface
    api_response = api_instance.update_node_interface(body, interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeNetworkInterfaceProperties**](NodeNetworkInterfaceProperties.md)|  | 
 **interface_id** | **str**| ID of interface to update | 

### Return type

[**NodeNetworkInterfaceProperties**](NodeNetworkInterfaceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_name_servers**
> NodeNameServersProperties update_node_name_servers(body)

Update the NSX Manager's Name Servers

Modifies the list of servers that the NSX Manager node uses to look up IP addresses associated with given domain names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeNameServersProperties() # NodeNameServersProperties | 

try:
    # Update the NSX Manager's Name Servers
    api_response = api_instance.update_node_name_servers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_node_name_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeNameServersProperties**](NodeNameServersProperties.md)|  | 

### Return type

[**NodeNameServersProperties**](NodeNameServersProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_properties**
> NodeProperties update_node_properties(body)

Update node properties

Modifies NSX appliance properties. Modifiable properties include the timezone, message of the day (motd), and hostname. The NSX appliance node_version, system_time, and kernel_version are read only and cannot be modified with this method. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeProperties() # NodeProperties | 

try:
    # Update node properties
    api_response = api_instance.update_node_properties(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_node_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeProperties**](NodeProperties.md)|  | 

### Return type

[**NodeProperties**](NodeProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_search_domains**
> NodeSearchDomainsProperties update_node_search_domains(body)

Update the NSX Manager's Search Domains

Modifies the list of domain names that the NSX Manager node uses to complete unqualified host names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSearchDomainsProperties() # NodeSearchDomainsProperties | 

try:
    # Update the NSX Manager's Search Domains
    api_response = api_instance.update_node_search_domains(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_node_search_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSearchDomainsProperties**](NodeSearchDomainsProperties.md)|  | 

### Return type

[**NodeSearchDomainsProperties**](NodeSearchDomainsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_user**
> NodeUserProperties update_node_user(body, userid)

Update node user

Updates attributes of an existing NSX appliance user. This method cannot be used to add a new user. Modifiable attributes include the username, full name of the user, and password. If you specify a password in a PUT request, it is not returned in the response. Nor is it returned in a GET request. The specified password does not meet the following complexity requirements: - minimum 12 characters in length - minimum 1 uppercase character - minimum 1 lowercase character - minimum 1 numeric character - minimum 1 special character - minimum 5 unique characters - default password complexity rules as enforced by the Linux PAM module 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeUserProperties() # NodeUserProperties | 
userid = 'userid_example' # str | User id of the user

try:
    # Update node user
    api_response = api_instance.update_node_user(body, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_node_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeUserProperties**](NodeUserProperties.md)|  | 
 **userid** | **str**| User id of the user | 

### Return type

[**NodeUserProperties**](NodeUserProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ntp_service**
> NodeNtpServiceProperties update_ntp_service(body)

Update NTP service properties

Update NTP service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeNtpServiceProperties() # NodeNtpServiceProperties | 

try:
    # Update NTP service properties
    api_response = api_instance.update_ntp_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_ntp_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeNtpServiceProperties**](NodeNtpServiceProperties.md)|  | 

### Return type

[**NodeNtpServiceProperties**](NodeNtpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_service**
> NodePolicyServiceProperties update_policy_service(body)

Update service properties

Update service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodePolicyServiceProperties() # NodePolicyServiceProperties | 

try:
    # Update service properties
    api_response = api_instance.update_policy_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_policy_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePolicyServiceProperties**](NodePolicyServiceProperties.md)|  | 

### Return type

[**NodePolicyServiceProperties**](NodePolicyServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proton_service**
> NodeProtonServiceProperties update_proton_service(body)

Update service properties

Update service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeProtonServiceProperties() # NodeProtonServiceProperties | 

try:
    # Update service properties
    api_response = api_instance.update_proton_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_proton_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeProtonServiceProperties**](NodeProtonServiceProperties.md)|  | 

### Return type

[**NodeProtonServiceProperties**](NodeProtonServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proxy_service**
> NodeHttpServiceProperties update_proxy_service(body)

Update http service properties

This API is deprecated.  Make changes to the http service configuration by calling the PUT /api/v1/cluster/api-service API. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeHttpServiceProperties() # NodeHttpServiceProperties | 

try:
    # Update http service properties
    api_response = api_instance.update_proxy_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_proxy_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeHttpServiceProperties**](NodeHttpServiceProperties.md)|  | 

### Return type

[**NodeHttpServiceProperties**](NodeHttpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_service**
> NodeInstallUpgradeServiceProperties update_repository_service(body)

Update NSX install-upgrade service properties

Update NSX install-upgrade service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeInstallUpgradeServiceProperties() # NodeInstallUpgradeServiceProperties | 

try:
    # Update NSX install-upgrade service properties
    api_response = api_instance.update_repository_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_repository_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeInstallUpgradeServiceProperties**](NodeInstallUpgradeServiceProperties.md)|  | 

### Return type

[**NodeInstallUpgradeServiceProperties**](NodeInstallUpgradeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snmp_service**
> NodeSnmpServiceProperties update_snmp_service(body)

Update SNMP service properties

Update SNMP service properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSnmpServiceProperties() # NodeSnmpServiceProperties | 

try:
    # Update SNMP service properties
    api_response = api_instance.update_snmp_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_snmp_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSnmpServiceProperties**](NodeSnmpServiceProperties.md)|  | 

### Return type

[**NodeSnmpServiceProperties**](NodeSnmpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snmpv3_engine_id**
> NodeSnmpV3EngineID update_snmpv3_engine_id(body)

Update SNMP V3 Engine ID

Update SNMP V3 Engine ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSnmpV3EngineID() # NodeSnmpV3EngineID | 

try:
    # Update SNMP V3 Engine ID
    api_response = api_instance.update_snmpv3_engine_id(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_snmpv3_engine_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSnmpV3EngineID**](NodeSnmpV3EngineID.md)|  | 

### Return type

[**NodeSnmpV3EngineID**](NodeSnmpV3EngineID.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssh_service**
> NodeSshServiceProperties update_ssh_service(body)

Update ssh service properties

Update ssh service properties. If the start_on_boot property is updated to true, existing ssh sessions if any are stopped and the ssh service is restarted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSshServiceProperties() # NodeSshServiceProperties | 

try:
    # Update ssh service properties
    api_response = api_instance.update_ssh_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_ssh_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSshServiceProperties**](NodeSshServiceProperties.md)|  | 

### Return type

[**NodeSshServiceProperties**](NodeSshServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_uc_state**
> update_uc_state(body)

Update UC state properties

Update UC state properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.UcStateProperties() # UcStateProperties | 

try:
    # Update UC state properties
    api_instance.update_uc_state(body)
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->update_uc_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UcStateProperties**](UcStateProperties.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_node_syslog_exporter_verify**
> verify_node_syslog_exporter_verify()

Verify node syslog exporter

Collect iptables rules needed for all existing syslog exporters and verify if the existing iptables rules are the same. If not, remove the stale rules and add the new rules to make sure all exporters work properly. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Verify node syslog exporter
    api_instance.verify_node_syslog_exporter_verify()
except ApiException as e:
    print("Exception when calling ManagementPlaneApiNsxComponentAdministrationApplianceManagementApi->verify_node_syslog_exporter_verify: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

