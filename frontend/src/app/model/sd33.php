<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: PUT, GET, POST, DELETE");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
 $postdata = file_get_contents("php://input");

if(isset($postdata) && !empty($postdata))
{
      echo $postdata;
  }
 ?>