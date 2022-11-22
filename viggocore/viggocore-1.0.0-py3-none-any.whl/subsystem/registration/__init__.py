from viggocore.common import subsystem
from viggocore.subsystem.registration import controller, router

subsystem = subsystem.Subsystem(
    individual_name='register',
    collection_name='register',
    controller=controller.Controller,
    router=router.Router)
