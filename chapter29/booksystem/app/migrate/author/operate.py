all_author_sql = "SELECT id, username, email FROM author"
add_author_sql = "INSERT INTO author(username, email) value(%s, %s)"