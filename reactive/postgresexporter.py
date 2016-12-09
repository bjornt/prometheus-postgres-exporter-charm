from charms.reactive import (
    when,
)

@when('prometheus-client.available')
def prometheus_client(prometheus):
    prometheus.configure(port=9187)
