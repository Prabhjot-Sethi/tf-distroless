import string

template = string.Template("""
[DEFAULTS]
cassandra_server_list=$__contrail_cassandra_server_list__
listen_ip_addr=$__contrail_listen_ip_addr__
listen_port=$__contrail_listen_port__
log_file=$__contrail_log_file__
log_local=1
log_level=SYS_NOTICE
zk_server_ip=$__contrail_zookeeper_server_ip__
rabbit_server=$__rabbit_server_ip__
list_optimization_enabled=True
collectors=$__contrail_collectors__
$__contrail_cloud_admin_role__
$__contrail_aaa_mode__

[SECURITY]
use_certs=$__contrail_use_certs__
keyfile=$__contrail_keyfile_location__
certfile=$__contrail_certfile_location__
ca_certs=$__contrail_cacertfile_location__
""")
