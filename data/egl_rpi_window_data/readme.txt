monitor was 1080p@60Hz

vanilla, digital2/analog2 is from normal raspbian, rate@30Hz, gpio before flip
rt, digital2_rt/analog2_rt is from raspbian with rt kernel, rate@30Hz, gpio before flip
wait_delay, digital_wait/analog_wait is from raspbian with rt kernel, rate@30Hz, with WaitClient, GPIO output *after* flip
wait_delay60, digital_wait_60/analog_wait_60 is from raspbian with rt kernel, kivy rate unlimited (bound by monitor fps), with WaitClient, GPIO output *after* flip



