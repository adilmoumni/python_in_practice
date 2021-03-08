from api.viewsets import IdeaBoxViewset
from rest_framework import routers
from employeeapi.viewsets import EmployeeViewset, CategoryViewset, IdeaboxViewset


router = routers.DefaultRouter()
router.register('category', CategoryViewset)
router.register('employee', EmployeeViewset)
router.register('ideabox', IdeaBoxViewset)
router.register('ideaboxEm', IdeaboxViewset)
