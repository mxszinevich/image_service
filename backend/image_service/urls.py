from config.routers import router
from .api.views import ImageDataView

router.register("images", ImageDataView, basename="images")

urlpatterns = router.urls
