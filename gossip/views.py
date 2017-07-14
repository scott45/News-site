from django.views.generic import ListView
from .models import Link


class LinkListView(ListView):
    model = Link
    paginate_by = 10

    def get_query_set(self):
        return Link.with_votes.all(self)
