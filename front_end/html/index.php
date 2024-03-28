<?php
/**
 * Sample PHP file with DB transactions
 *
 * @author Vanessa Richie Alia-Trapero <vrat.engr@gmail.com>
 * @implementedby Yoniliman Galvis Aguirre Alias maZinger <yoniliman.gales@uao.edu.co>
 */

echo "<pre>IA TASKFORCE!\n";
echo "<pre>WEBSCRAPPING APPLICATION\n";
echo "<pre>1\n";

$host       = "127.0.0.1:9004"; // service name of the database container
$user       = "webusr"; // MARIADB_USER
$password   = "webusr"; // MARIADB_PASSWORD
$db         = "wsdb"; // MARIADB_DATABASE
$table      = "user_name"; // table name from our data.sql dump
$g_link = false;
    
function GetMyConnection()
{
    global $g_link;
    if( $g_link )
        return $g_link;
    $g_link = mysql_connect( $host, $user, $password) or die('Could not connect to server. ' . $host);
    mysql_select_db($db, $g_link) or die('Could not select database.' . $db);
    return $g_link;
}

function CleanUpDB()
{
    global $g_link;
    if( $g_link != false )
        mysql_close($g_link);
    $g_link = false;
}



/*$conn       = new mysqli($host, $user, $password, $db);

if ($conn->connect_error) {
    die ("Database connection error: " . $conn->connect_error);
} else {
    */
    // $result = $conn->query("INSERT INTO $table (note) VALUES ('random note - " . rand() . "')");
    $result = mysql_query("SELECT * FROM $table", GetMyConnection() );
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