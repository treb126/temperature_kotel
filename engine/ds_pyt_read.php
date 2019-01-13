<?php
	ini_set('error_reporting', E_ALL);
	ini_set('display_errors', 1);
	ini_set('display_startup_errors', 1);
	$t1 = shell_exec('sudo python ../pyt/t1.py');
	$t2 = shell_exec('sudo python ../pyt/t2.py');
	$now = shell_exec('sudo python ../pyt/now.py');
	echo $now.'/'.$t1.'/'.$t2;

?>