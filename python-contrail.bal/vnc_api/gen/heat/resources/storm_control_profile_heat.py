
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailStormControlProfile(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, STORM_CONTROL_PARAMETERS, STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS, STORM_CONTROL_PARAMETERS_RECOVERY_TIMEOUT, STORM_CONTROL_PARAMETERS_NO_UNREGISTERED_MULTICAST, STORM_CONTROL_PARAMETERS_NO_REGISTERED_MULTICAST, STORM_CONTROL_PARAMETERS_NO_UNKNOWN_UNICAST, STORM_CONTROL_PARAMETERS_NO_MULTICAST, STORM_CONTROL_PARAMETERS_NO_BROADCAST, STORM_CONTROL_PARAMETERS_BANDWIDTH_PERCENT, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, TAG_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'storm_control_parameters', 'storm_control_parameters_storm_control_actions', 'storm_control_parameters_recovery_timeout', 'storm_control_parameters_no_unregistered_multicast', 'storm_control_parameters_no_registered_multicast', 'storm_control_parameters_no_unknown_unicast', 'storm_control_parameters_no_multicast', 'storm_control_parameters_no_broadcast', 'storm_control_parameters_bandwidth_percent', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'tag_refs', 'project'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        STORM_CONTROL_PARAMETERS: properties.Schema(
            properties.Schema.MAP,
            _('STORM_CONTROL_PARAMETERS.'),
            update_allowed=True,
            required=False,
            schema={
                STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS: properties.Schema(
                    properties.Schema.LIST,
                    _('STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'interface-shutdown']),
                    ],
                ),
                STORM_CONTROL_PARAMETERS_RECOVERY_TIMEOUT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('STORM_CONTROL_PARAMETERS_RECOVERY_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                ),
                STORM_CONTROL_PARAMETERS_NO_UNREGISTERED_MULTICAST: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('STORM_CONTROL_PARAMETERS_NO_UNREGISTERED_MULTICAST.'),
                    update_allowed=True,
                    required=False,
                ),
                STORM_CONTROL_PARAMETERS_NO_REGISTERED_MULTICAST: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('STORM_CONTROL_PARAMETERS_NO_REGISTERED_MULTICAST.'),
                    update_allowed=True,
                    required=False,
                ),
                STORM_CONTROL_PARAMETERS_NO_UNKNOWN_UNICAST: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('STORM_CONTROL_PARAMETERS_NO_UNKNOWN_UNICAST.'),
                    update_allowed=True,
                    required=False,
                ),
                STORM_CONTROL_PARAMETERS_NO_MULTICAST: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('STORM_CONTROL_PARAMETERS_NO_MULTICAST.'),
                    update_allowed=True,
                    required=False,
                ),
                STORM_CONTROL_PARAMETERS_NO_BROADCAST: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('STORM_CONTROL_PARAMETERS_NO_BROADCAST.'),
                    update_allowed=True,
                    required=False,
                ),
                STORM_CONTROL_PARAMETERS_BANDWIDTH_PERCENT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('STORM_CONTROL_PARAMETERS_BANDWIDTH_PERCENT.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        ANNOTATIONS: properties.Schema(
            properties.Schema.MAP,
            _('ANNOTATIONS.'),
            update_allowed=True,
            required=False,
            schema={
                ANNOTATIONS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('ANNOTATIONS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ANNOTATIONS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ANNOTATIONS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        PERMS2: properties.Schema(
            properties.Schema.MAP,
            _('PERMS2.'),
            update_allowed=True,
            required=False,
            schema={
                PERMS2_OWNER: properties.Schema(
                    properties.Schema.STRING,
                    _('PERMS2_OWNER.'),
                    update_allowed=True,
                    required=False,
                ),
                PERMS2_OWNER_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_OWNER_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_GLOBAL_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_GLOBAL_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_SHARE: properties.Schema(
                    properties.Schema.LIST,
                    _('PERMS2_SHARE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PERMS2_SHARE_TENANT: properties.Schema(
                                properties.Schema.STRING,
                                _('PERMS2_SHARE_TENANT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PERMS2_SHARE_TENANT_ACCESS: properties.Schema(
                                properties.Schema.INTEGER,
                                _('PERMS2_SHARE_TENANT_ACCESS.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.Range(0, 7),
                                ],
                            ),
                        }
                    )
                ),
            }
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        STORM_CONTROL_PARAMETERS: attributes.Schema(
            _('STORM_CONTROL_PARAMETERS.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT) and self.properties.get(self.PROJECT) != 'config-root':
            try:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(self.properties.get(self.PROJECT))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.StormControlProfile(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.STORM_CONTROL_PARAMETERS) is not None:
            obj_1 = vnc_api.StormControlParameters()
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS) is not None:
                for index_1 in range(len(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS))):
                    obj_1.add_storm_control_actions(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS)[index_1])
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_RECOVERY_TIMEOUT) is not None:
                obj_1.set_recovery_timeout(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_RECOVERY_TIMEOUT))
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNREGISTERED_MULTICAST) is not None:
                obj_1.set_no_unregistered_multicast(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNREGISTERED_MULTICAST))
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_REGISTERED_MULTICAST) is not None:
                obj_1.set_no_registered_multicast(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_REGISTERED_MULTICAST))
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNKNOWN_UNICAST) is not None:
                obj_1.set_no_unknown_unicast(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNKNOWN_UNICAST))
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_MULTICAST) is not None:
                obj_1.set_no_multicast(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_MULTICAST))
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_BROADCAST) is not None:
                obj_1.set_no_broadcast(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_BROADCAST))
            if self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_BANDWIDTH_PERCENT) is not None:
                obj_1.set_bandwidth_percent(self.properties.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_BANDWIDTH_PERCENT))
            obj_0.set_storm_control_parameters(obj_1)
        if self.properties.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if self.properties.get(self.PERMS2) is not None:
            obj_1 = vnc_api.PermType2()
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER) is not None:
                obj_1.set_owner(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS) is not None:
                obj_1.set_owner_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS) is not None:
                obj_1.set_global_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE) is not None:
                for index_1 in range(len(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE))):
                    obj_2 = vnc_api.ShareType()
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT) is not None:
                        obj_2.set_tenant(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT))
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS) is not None:
                        obj_2.set_tenant_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS))
                    obj_1.add_share(obj_2)
            obj_0.set_perms2(obj_1)

        # reference to tag_refs
        if self.properties.get(self.TAG_REFS):
            for index_0 in range(len(self.properties.get(self.TAG_REFS))):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_tag(ref_obj)

        try:
            obj_uuid = super(ContrailStormControlProfile, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().storm_control_profile_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.STORM_CONTROL_PARAMETERS) is not None:
            obj_1 = vnc_api.StormControlParameters()
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS) is not None:
                for index_1 in range(len(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS))):
                    obj_1.add_storm_control_actions(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_STORM_CONTROL_ACTIONS)[index_1])
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_RECOVERY_TIMEOUT) is not None:
                obj_1.set_recovery_timeout(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_RECOVERY_TIMEOUT))
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNREGISTERED_MULTICAST) is not None:
                obj_1.set_no_unregistered_multicast(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNREGISTERED_MULTICAST))
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_REGISTERED_MULTICAST) is not None:
                obj_1.set_no_registered_multicast(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_REGISTERED_MULTICAST))
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNKNOWN_UNICAST) is not None:
                obj_1.set_no_unknown_unicast(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_UNKNOWN_UNICAST))
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_MULTICAST) is not None:
                obj_1.set_no_multicast(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_MULTICAST))
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_BROADCAST) is not None:
                obj_1.set_no_broadcast(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_NO_BROADCAST))
            if prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_BANDWIDTH_PERCENT) is not None:
                obj_1.set_bandwidth_percent(prop_diff.get(self.STORM_CONTROL_PARAMETERS, {}).get(self.STORM_CONTROL_PARAMETERS_BANDWIDTH_PERCENT))
            obj_0.set_storm_control_parameters(obj_1)
        if prop_diff.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)

        # reference to tag_refs
        ref_obj_list = []
        if self.TAG_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.TAG_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_tag_list(ref_obj_list)
            # End: reference to tag_refs

        try:
            self.vnc_lib().storm_control_profile_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().storm_control_profile_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('storm_control_profile %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().storm_control_profile_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::StormControlProfile': ContrailStormControlProfile,
    }