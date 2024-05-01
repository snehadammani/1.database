<?php
// MySQL database connection details
$servername = "127.0.0.1";
$username = "root";
$password = "Sneha$29";
$dbname = "vegetable_vendor_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process form data based on entity
$entity = $_POST['entity'];
if ($entity === 'Supplier') {
    $name = $_POST['name'];
    $phone = $_POST['phone'];
    // Insert data into Supplier table
    $sql = "INSERT INTO Supplier (supplier_name, supplier_phone) VALUES ('$name', '$phone')";
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} elseif ($entity === 'Vegetable') {
    $name = $_POST['name'];
    $category = $_POST['category'];
    // Insert data into Vegetable table
    $sql = "INSERT INTO Vegetable (vegetable_name, category_id) VALUES ('$name', '$category')";
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
// Add conditions for other entities

$conn->close();
?>
