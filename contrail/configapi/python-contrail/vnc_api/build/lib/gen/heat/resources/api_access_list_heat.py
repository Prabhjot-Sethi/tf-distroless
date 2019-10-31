
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


class ContrailApiAccessList(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, API_ACCESS_LIST_ENTRIES, API_ACCESS_LIST_ENTRIES_RBAC_RULE, API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_OBJECT, API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_FIELD, API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_NAME, API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_CRUD, DISPLAY_NAME, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, TAG_REFS, DOMAIN, PROJECT, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'api_access_list_entries', 'api_access_list_entries_rbac_rule', 'api_access_list_entries_rbac_rule_rule_object', 'api_access_list_entries_rbac_rule_rule_field', 'api_access_list_entries_rbac_rule_rule_perms', 'api_access_list_entries_rbac_rule_rule_perms_role_name', 'api_access_list_entries_rbac_rule_rule_perms_role_crud', 'display_name', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'tag_refs', 'domain', 'project', 'global_system_config'
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
        API_ACCESS_LIST_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('API_ACCESS_LIST_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                API_ACCESS_LIST_ENTRIES_RBAC_RULE: properties.Schema(
                    properties.Schema.LIST,
                    _('API_ACCESS_LIST_ENTRIES_RBAC_RULE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_OBJECT: properties.Schema(
                                properties.Schema.STRING,
                                _('API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_OBJECT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_FIELD: properties.Schema(
                                properties.Schema.STRING,
                                _('API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_FIELD.'),
                                update_allowed=True,
                                required=False,
                            ),
                            API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS: properties.Schema(
                                properties.Schema.LIST,
                                _('API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_NAME: properties.Schema(
                                            properties.Schema.STRING,
                                            _('API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_NAME.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_CRUD: properties.Schema(
                                            properties.Schema.STRING,
                                            _('API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_CRUD.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                    }
                                )
                            ),
                        }
                    )
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
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
        DOMAIN: properties.Schema(
            properties.Schema.STRING,
            _('DOMAIN.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_SYSTEM_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_SYSTEM_CONFIG.'),
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
        API_ACCESS_LIST_ENTRIES: attributes.Schema(
            _('API_ACCESS_LIST_ENTRIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
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
        DOMAIN: attributes.Schema(
            _('DOMAIN.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
        GLOBAL_SYSTEM_CONFIG: attributes.Schema(
            _('GLOBAL_SYSTEM_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.DOMAIN) and self.properties.get(self.DOMAIN) != 'config-root':
            try:
                parent_obj = self.vnc_lib().domain_read(fq_name_str=self.properties.get(self.DOMAIN))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().domain_read(id=str(uuid.UUID(self.properties.get(self.DOMAIN))))
            except:
                parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT) and self.properties.get(self.PROJECT) != 'config-root':
            try:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(self.properties.get(self.PROJECT))))
            except:
                parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) != 'config-root':
            try:
                parent_obj = self.vnc_lib().global_system_config_read(fq_name_str=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_system_config_read(id=str(uuid.UUID(self.properties.get(self.GLOBAL_SYSTEM_CONFIG))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) != 'config-root':
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.ApiAccessList(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.API_ACCESS_LIST_ENTRIES) is not None:
            obj_1 = vnc_api.RbacRuleEntriesType()
            if self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE) is not None:
                for index_1 in range(len(self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE))):
                    obj_2 = vnc_api.RbacRuleType()
                    if self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_OBJECT) is not None:
                        obj_2.set_rule_object(self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_OBJECT))
                    if self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_FIELD) is not None:
                        obj_2.set_rule_field(self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_FIELD))
                    if self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS) is not None:
                        for index_2 in range(len(self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS))):
                            obj_3 = vnc_api.RbacPermType()
                            if self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_NAME) is not None:
                                obj_3.set_role_name(self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_NAME))
                            if self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_CRUD) is not None:
                                obj_3.set_role_crud(self.properties.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_CRUD))
                            obj_2.add_rule_perms(obj_3)
                    obj_1.add_rbac_rule(obj_2)
            obj_0.set_api_access_list_entries(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
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
            obj_uuid = super(ContrailApiAccessList, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().api_access_list_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.API_ACCESS_LIST_ENTRIES) is not None:
            obj_1 = vnc_api.RbacRuleEntriesType()
            if prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE) is not None:
                for index_1 in range(len(prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE))):
                    obj_2 = vnc_api.RbacRuleType()
                    if prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_OBJECT) is not None:
                        obj_2.set_rule_object(prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_OBJECT))
                    if prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_FIELD) is not None:
                        obj_2.set_rule_field(prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_FIELD))
                    if prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS) is not None:
                        for index_2 in range(len(prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS))):
                            obj_3 = vnc_api.RbacPermType()
                            if prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_NAME) is not None:
                                obj_3.set_role_name(prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_NAME))
                            if prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_CRUD) is not None:
                                obj_3.set_role_crud(prop_diff.get(self.API_ACCESS_LIST_ENTRIES, {}).get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE, {})[index_1].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS, {})[index_2].get(self.API_ACCESS_LIST_ENTRIES_RBAC_RULE_RULE_PERMS_ROLE_CRUD))
                            obj_2.add_rule_perms(obj_3)
                    obj_1.add_rbac_rule(obj_2)
            obj_0.set_api_access_list_entries(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
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
            self.vnc_lib().api_access_list_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().api_access_list_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('api_access_list %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().api_access_list_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::ApiAccessList': ContrailApiAccessList,
    }
