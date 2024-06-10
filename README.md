## Flask Application Design for a Recent Newspaper Articles Website

**HTML Files:**

- **index.html:** This is the homepage of the website. It should contain a list of the most recent newspaper articles and links to each article's individual page.
- **article.html:** This file will display the full content of a single newspaper article. It should include the article's title, author, date published, and body text.

**Routes:**

- **@app.route('/')**: This route will handle the request for the homepage. It should query the database for the most recent newspaper articles and pass them to the `index.html` template.
- **@app.route('/article/<int:article_id>')**: This route will handle the request for an individual newspaper article. It should query the database for the article with the specified ID and pass it to the `article.html` template.
- **@app.route('/search')**: This route will handle the search functionality of the website. It should allow users to search for articles based on keywords and return a list of matching articles.