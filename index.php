<?
ini_set('error_reporting', E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
?>
<html>

<head>
  <meta charset="UTF-8">
  <title>Temperature</title>
  <link rel="stylesheet" href="css/style.css">
  <script src="js/jquery3.3.1.min.js"></script>
  <script src="js/check.js"></script>
  <script type="text/javascript">
  	temp();
  	var timr = setTimeout(function tim() {
  	temp();
  	timr = setTimeout(tim, 5000);
	}, 5000);
  </script>
</head>

<body>
  <div style="display: inline-block; background-color: red;" id="t1">Temp 1:NaN</div><br>
  <div style="display: inline-block; background-color: blue;" id="t2">Temp 2:NaN</div>
</body>

</html>
