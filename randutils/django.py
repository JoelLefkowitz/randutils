from .exceptions import NoObjectsError
from .generate import randint


def get_random_instance(model):
    count = model.objects.count()

    if count == 0:
        raise NoObjectsError(model)

    return model.objects.all()[randint(count)]


def get_random_instances(model):
    pks = model.objects.values_list("pk", flat=True)

    for i in range(pks.count()):
        yield model.objects.get(pk=pks[randint(pks.count())])
