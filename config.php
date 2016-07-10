<?php
   define('DB_SERVER', 'ec2-54-169-165-242.ap-southeast-1.compute.amazonaws.com');
   define('DB_USERNAME', 'root');
   define('DB_PASSWORD', 'cfg');
   define('DB_DATABASE', 'mysql');
   $db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
?>
