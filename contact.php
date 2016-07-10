<html><body>
<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);
// database connectivity
$servername = "ec2-54-169-165-242.ap-southeast-1.compute.amazonaws.com";
$username = "root";
$password = "cfg";
$db="mysql";

// Create connection
$conn =mysqli_connect($servername, $username, $password,$db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
else
{
    //echo "Connected successfully";

}
$result=mysqli_query($conn,"select lastname,firstname,contact_no from investor");
//echo $result;
//$count = $result->num_rows;
//echo $count;
if ($result->num_rows> 0) {
	//echo "bye";
	 echo "<table><tr><th>Investor Name  </th><th> Last name  </th><th> Contact details  </th></tr>";
        // echo "sasa";
    while($row = $result->fetch_assoc()) {
         
         echo "<tr><td>".$row["lastname"]."</td><td>".$row["firstname"]."</td><td>".$row["contact_no"]."</td></tr>";
    
    }
    echo "</table>";
} else {
    echo "0 results";
}



//if (!$query) {
    //echo "Could not successfully run query ($sql) from DB: " . mysql_error();
  //  exit;
//}
?>
    
</body>
</html>
