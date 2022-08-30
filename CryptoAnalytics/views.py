from .tasks import list_currencies

from .tasks import supper_sum
def form_valid(self, form):

    supper_sum.delay(5, 7)
    return super().form_valid(form)


# def form_valid(self, form):
#     list_currencies.delay(5, 7)
#     return super().form_valid(form)

    # ListCurrencies.objects.aget_or_create(currency=i)
    # return Response(data, status=status.HTTP_200_OK)