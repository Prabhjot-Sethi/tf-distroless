
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


class ContrailBridgeDomain(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, MAC_MOVE_CONTROL, MAC_MOVE_CONTROL_MAC_MOVE_LIMIT, MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW, MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION, MAC_AGING_TIME, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, MAC_LEARNING_ENABLED, ISID, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, MAC_LIMIT_CONTROL, MAC_LIMIT_CONTROL_MAC_LIMIT, MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION, TAG_REFS, VIRTUAL_NETWORK
    ) = (
        'name', 'fq_name', 'display_name', 'mac_move_control', 'mac_move_control_mac_move_limit', 'mac_move_control_mac_move_time_window', 'mac_move_control_mac_move_limit_action', 'mac_aging_time', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'mac_learning_enabled', 'isid', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'mac_limit_control', 'mac_limit_control_mac_limit', 'mac_limit_control_mac_limit_action', 'tag_refs', 'virtual_network'
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
        MAC_MOVE_CONTROL: properties.Schema(
            properties.Schema.MAP,
            _('MAC_MOVE_CONTROL.'),
            update_allowed=True,
            required=False,
            schema={
                MAC_MOVE_CONTROL_MAC_MOVE_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('MAC_MOVE_CONTROL_MAC_MOVE_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW: properties.Schema(
                    properties.Schema.INTEGER,
                    _('MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(1, 60),
                    ],
                ),
                MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION: properties.Schema(
                    properties.Schema.STRING,
                    _('MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'log', u'alarm', u'shutdown', u'drop']),
                    ],
                ),
            }
        ),
        MAC_AGING_TIME: properties.Schema(
            properties.Schema.INTEGER,
            _('MAC_AGING_TIME.'),
            update_allowed=True,
            required=False,
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
        MAC_LEARNING_ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('MAC_LEARNING_ENABLED.'),
            update_allowed=True,
            required=False,
        ),
        ISID: properties.Schema(
            properties.Schema.INTEGER,
            _('ISID.'),
            update_allowed=True,
            required=False,
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
        MAC_LIMIT_CONTROL: properties.Schema(
            properties.Schema.MAP,
            _('MAC_LIMIT_CONTROL.'),
            update_allowed=True,
            required=False,
            schema={
                MAC_LIMIT_CONTROL_MAC_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('MAC_LIMIT_CONTROL_MAC_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION: properties.Schema(
                    properties.Schema.STRING,
                    _('MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'log', u'alarm', u'shutdown', u'drop']),
                    ],
                ),
            }
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_NETWORK.'),
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
        MAC_MOVE_CONTROL: attributes.Schema(
            _('MAC_MOVE_CONTROL.'),
        ),
        MAC_AGING_TIME: attributes.Schema(
            _('MAC_AGING_TIME.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        MAC_LEARNING_ENABLED: attributes.Schema(
            _('MAC_LEARNING_ENABLED.'),
        ),
        ISID: attributes.Schema(
            _('ISID.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        MAC_LIMIT_CONTROL: attributes.Schema(
            _('MAC_LIMIT_CONTROL.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        VIRTUAL_NETWORK: attributes.Schema(
            _('VIRTUAL_NETWORK.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.VIRTUAL_NETWORK) and self.properties.get(self.VIRTUAL_NETWORK) != 'config-root':
            try:
                parent_obj = self.vnc_lib().virtual_network_read(fq_name_str=self.properties.get(self.VIRTUAL_NETWORK))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().virtual_network_read(id=str(uuid.UUID(self.properties.get(self.VIRTUAL_NETWORK))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.VIRTUAL_NETWORK) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.BridgeDomain(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.MAC_MOVE_CONTROL) is not None:
            obj_1 = vnc_api.MACMoveLimitControlType()
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT) is not None:
                obj_1.set_mac_move_limit(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT))
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW) is not None:
                obj_1.set_mac_move_time_window(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW))
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION) is not None:
                obj_1.set_mac_move_limit_action(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION))
            obj_0.set_mac_move_control(obj_1)
        if self.properties.get(self.MAC_AGING_TIME) is not None:
            obj_0.set_mac_aging_time(self.properties.get(self.MAC_AGING_TIME))
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
        if self.properties.get(self.MAC_LEARNING_ENABLED) is not None:
            obj_0.set_mac_learning_enabled(self.properties.get(self.MAC_LEARNING_ENABLED))
        if self.properties.get(self.ISID) is not None:
            obj_0.set_isid(self.properties.get(self.ISID))
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
        if self.properties.get(self.MAC_LIMIT_CONTROL) is not None:
            obj_1 = vnc_api.MACLimitControlType()
            if self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT) is not None:
                obj_1.set_mac_limit(self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT))
            if self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION) is not None:
                obj_1.set_mac_limit_action(self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION))
            obj_0.set_mac_limit_control(obj_1)

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
            obj_uuid = super(ContrailBridgeDomain, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().bridge_domain_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.MAC_MOVE_CONTROL) is not None:
            obj_1 = vnc_api.MACMoveLimitControlType()
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT) is not None:
                obj_1.set_mac_move_limit(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT))
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW) is not None:
                obj_1.set_mac_move_time_window(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW))
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION) is not None:
                obj_1.set_mac_move_limit_action(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION))
            obj_0.set_mac_move_control(obj_1)
        if prop_diff.get(self.MAC_AGING_TIME) is not None:
            obj_0.set_mac_aging_time(prop_diff.get(self.MAC_AGING_TIME))
        if prop_diff.get(self.MAC_LEARNING_ENABLED) is not None:
            obj_0.set_mac_learning_enabled(prop_diff.get(self.MAC_LEARNING_ENABLED))
        if prop_diff.get(self.ISID) is not None:
            obj_0.set_isid(prop_diff.get(self.ISID))
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
        if prop_diff.get(self.MAC_LIMIT_CONTROL) is not None:
            obj_1 = vnc_api.MACLimitControlType()
            if prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT) is not None:
                obj_1.set_mac_limit(prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT))
            if prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION) is not None:
                obj_1.set_mac_limit_action(prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION))
            obj_0.set_mac_limit_control(obj_1)

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
            self.vnc_lib().bridge_domain_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().bridge_domain_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('bridge_domain %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().bridge_domain_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::BridgeDomain': ContrailBridgeDomain,
    }