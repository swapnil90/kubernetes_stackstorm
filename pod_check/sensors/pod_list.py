from kubernetes import client, config
from st2reactor.sensor.base import PollingSensor


class KubernetesPodSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=None):
        super(KubernetesPodSensor, self).__init__(sensor_service=sensor_service,
                                                     config=config,
                                                     poll_interval=poll_interval)
        self._trigger_ref = 'pod_check.event1'
        self._logger = self._sensor_service.get_logger(__name__)
        self._last_replication_count = 0

    def setup(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()
        pass

    def poll(self):
        trigger = self._trigger_ref
        pod_list = self.v1.list_pod_for_all_namespaces(watch=False,pretty='true',label_selector='app = nginx')
        pod_list=pod_list.to_dict()
        replication_count = len(pod_list['items'])
        last_replication_count = int(self._get_last_count())
        self._logger.info("last replication cound is %s and current replication count is %s" %(last_replication_count, replication_count))
        if (replication_count > 5) and (last_replication_count != replication_count):
            payload = {'replication_count': replication_count}
            self._set_last_count(replication_count)
            self._sensor_service.dispatch(trigger=trigger, payload=payload)

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def _get_last_count(self):
        if hasattr(self._sensor_service, 'get_value'):
            try:
                self._last_replication_count = self._sensor_service.get_value(name='last_count')
            except:
                pass
        return self._last_replication_count

    def _set_last_count(self, last_count):
        self._last_replication_count = last_count

        if hasattr(self._sensor_service, 'set_value'):
            self._sensor_service.set_value(name='last_count', value=last_count)

