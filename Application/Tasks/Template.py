from ..Handler import User as UserHandler, Bookkeeping as BillHandler
from ..Application import scheduler


@scheduler.task('cron', id='monthly-1', day='1', month="*")
def insert_balance():
    with scheduler.app.app_context():
        # TODO your task here
