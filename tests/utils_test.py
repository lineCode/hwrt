#!/usr/bin/env python

import nose
# mine
import hwrt.utils as utils


# Tests
def execution_test():
    utils.get_project_root()
    utils.get_latest_model(".", "model")
    utils.get_latest_working_model(".")
    utils.get_latest_successful_run(".")
    nose.tools.assert_equal(utils.get_readable_time(123), "123ms")
    nose.tools.assert_equal(utils.get_readable_time(1000*30),
                            "30s 0ms")
    nose.tools.assert_equal(utils.get_readable_time(1000*60),
                            "1 minutes 0s 0ms")
    nose.tools.assert_equal(utils.get_readable_time(1000*60*60),
                            "1h, 0 minutes 0s 0ms")
    nose.tools.assert_equal(utils.get_readable_time(2*1000*60*60),
                            "2h, 0 minutes 0s 0ms")
    nose.tools.assert_equal(utils.get_readable_time(25*1000*60*60+3),
                            "25h, 0 minutes 0s 3ms")