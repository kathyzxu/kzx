def create_index_page(html_files, output_file):
    # Basic HTML structure for the index page
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index of HTML Files</title>
    </head>
    <body>
        <h1>Index of HTML Files</h1>
        <ul>
    """
    
    # Adding links to each HTML file
    for file in html_files:
        html_content += f'            <li><a href="{file}">{file}</a></li>\n'
    
    # Closing HTML tags
    html_content += """
        </ul>
    </body>
    </html>
    """
    
    # Write the content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Example usage
files_with_text = [
    ('may24.html', 'May'),
    ('june24.html', 'June'),
    ('july24.html', 'July')
]
output_file = 'menu.html'
create_index_page(files_with_text, output_file)