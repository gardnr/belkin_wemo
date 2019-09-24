from ouimeaux.environment import Environment

from gardnr import drivers, logger


class Wemo(drivers.Power):

    def setup(self):
        env = Environment()
        self.switch = env.get_switch(self.device_name)

    def on(self):
        logger.info('turning on {}'.format(self.device_name))
        self.switch.on()

    def off(self):
        logger.info('turning off {}'.format(self.device_name))
        self.switch.off()
