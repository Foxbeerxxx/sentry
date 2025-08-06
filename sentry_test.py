import sentry_sdk

sentry_sdk.init(
    dsn="https://57bcf494b3e17c6ca2d43da38a9ca2e1@o4509798640386048.ingest.de.sentry.io/4509798785220688",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

# Вот ошибка, которая создаст событие:
division_by_zero = 1 / 0
