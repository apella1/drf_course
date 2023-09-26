"""Permission mixins"""
from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin:
    """Base class to be inherited
    by classes accepting permission_classes member
    """

    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
