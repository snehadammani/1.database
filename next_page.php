<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Select Entity</title>
</head>
<body>
    <h1>Select Entity:</h1>
    <form action="next_page.php" method="post">
        <label>Select an entity:</label>
        <select name="entity">
            <option value="Supplier">Supplier</option>
            <option value="Vegetable">Vegetable</option>
            <!-- Add options for other entities as needed -->
        </select>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
