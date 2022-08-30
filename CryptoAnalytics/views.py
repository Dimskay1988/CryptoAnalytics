from .tasks import supper_sum


def form_valid(self, form):
    supper_sum.delay(5, 7)
    return super().form_valid(form)
