#
#
#
#
##### TEST MODULE
#
#
#
#

# winservice_test.py
from winservice import Service, instart
import subprocess
import os

class Test(Service):
    def start(self):
        path = os.getcwd() + "//Node.py"
        self.runflag=True
        subprocess.Popen(['python',path])
        while self.runflag:
            self.sleep(10)
            self.log("I'm alive ...")
    def stop(self):
        self.runflag=False
        self.log("I'm done")

instart(Test, 'aTestMe3', 'Python Service Test')
## end of http://code.activestate.com/recipes/551780/ }}}
