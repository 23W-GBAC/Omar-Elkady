import datetime

# Define the directory where you want to save your blog posts
blog_directory = ''

# Generate the current date in the format YYYY-MM-DD
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Create a filename with the current date and a default title
file_name = 'README.md'

# Define the front matter template
front_matter = """---
layout: post
title: "New Blog Post"
date: {current_date}
categories: update
---

Your content goes here.
"""

# Replace the placeholder with the current date in the front matter
front_matter = front_matter.format(current_date=current_date)

# Combine the directory and filename to create the full path
full_path = f"{blog_directory}/{file_name}"

# Write the front matter to a new file
with open(full_path, 'w') as file:
    file.write(front_matter)

print(f"New blog post template created at: {full_path}")
