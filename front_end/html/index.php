<?php
/**
 * Sample PHP file with DB transactions
 *
 * @author Vanessa Richie Alia-Trapero <vrat.engr@gmail.com>
 * @implementedby Yoniliman Galvis Aguirre Alias maZinger <yoniliman.gales@uao.edu.co>
 */

echo "<pre>IA TASKFORCE!\n";
echo "<pre>WEBSCRAPPING APPLICATION\n";
echo "<pre> docker-mariadb \n";

$host       = "docker-mariadb"; // service name of the database container
$user       = "root"; // MARIADB_USER
$password   = "root"; // MARIADB_PASSWORD
$db         = "wsdb"; // MARIADB_DATABASE
$table      = "user_name"; // table name from our data.sql dump
$sql        = "SELECT * FROM $table";
$g_link = false;


function GetMyConnection()
{
    echo "global.\n";
    global $g_link;
    if( $g_link )
        return $g_link;
    echo "g_link.\n";
    $g_link = mysqli_connect( $GLOBALS['host'], $GLOBALS['user'], $GLOBALS['password']) or die('Could not connect to server. ' . $GLOBALS['host']);
    
    if( $g_link != false )
        echo "g_link 2 \n";

    mysqli_select_db($g_link, $GLOBALS['db']) or die('Could not select database.' . $GLOBALS['db']);
    echo "g_link 3 \n";

    return $g_link;
}

function CleanUpDB()
{
    global $g_link;
    if( $g_link != false )
        mysqli_close($g_link);
    $g_link = false;
}

/*
$mysqli = new mysqli($host, $user, $password, $db);
echo "1 /n";
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
echo "2 /n";
$result = mysqli_query($mysqli, $sql );
echo "3 /n";
while ($row = $result->fetch_assoc());
mysqli->close();
*/


/*$conn       = new mysqli($host, $user, $password, $db);

if ($conn->connect_error) {
    die ("Database connection error: " . $conn->connect_error);
} else {
*/
    // $result = $conn->query("INSERT INTO $table (note) VALUES ('random note - " . rand() . "')");
    
    echo "before result.\n";
    $result = mysqli_query(GetMyConnection(),$sql );
    echo "after result.\n";
    if ($result) {
        echo "Successfully connected to webscrapping database.\n";
        #$result = $conn->query("SELECT * FROM $table");
        $rows = $result->fetch_all(MYSQLI_ASSOC);
        foreach ($rows as $row) {
            echo "user # " . $row['user_id'] . ": " . $row['user_desc'] . ": " . $row['created_at'] . ": " . $row['last_edit_at'] . ": " . $row['last_edit_comment'] . "\n";
        }
    } else {
        die ("Database connection error occurred. :(");
    }

?>