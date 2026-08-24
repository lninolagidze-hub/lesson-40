import time

from django.db.models import F

from .models import Category


class CategoryAccessMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.perf_counter()

        
        category_id = request.resolver_match.kwargs.get(
            "category_id"
        ) if request.resolver_match else None

        if category_id:

            Category.objects.filter(
                id=category_id
            ).update(
                access_count=F("access_count") + 1
            )

    
        response = self.get_response(request)

        duration = time.perf_counter() - start_time

        response["X-Response-Time"] = (
            f"{duration:.4f} seconds"
        )

        return response
