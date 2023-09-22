"""Default permissions"""
from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    """_summary_

    Args:
        permissions (_type_): _description_
    """

    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            # for the permission -> view_(model_name)
            # app_name.verb_product_name
            if user.has_perm("products.view_product"):
                return True
            if user.has_perm("products.change_product"):
                return True
            if user.has_perm("products.add_product"):
                return True
            if user.has_perm("products.delete_product"):
                return True
            return False
        return False
