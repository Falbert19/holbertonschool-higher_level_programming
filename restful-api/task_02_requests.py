#!/usr/bin/python3
"""
task_02_requests.py

This module interacts with the JSONPlaceholder
API using the requests library.
It provides two main functions:

1. fetch_and_print_posts():
   - Sends an HTTP GET request to the JSONPlaceholder posts endpoint.
   - Prints the status code of the response.
   - If the request is successful, parses the JSON
   response and prints the title of each post.

2. fetch_and_save_posts():
   - Sends an HTTP GET request to the JSONPlaceholder posts endpoint.
   - If the request is successful, parses the JSON
   response and structures the data into a list of dictionaries,
     each containing the post's id, title, and body.
   - Writes this data into a CSV file named 'posts.csv'
   using Python's csv module.

Usage:
    from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

    fetch_and_print_posts()
    fetch_and_save_posts()
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and
    prints the title of each post.

    This function:
    - Sends an HTTP GET request to the
    JSONPlaceholder posts endpoint.
    - Prints the status code of the HTTP response.
    - If the response status code is 200 (OK),
    it parses the JSON content and prints each post's title.

    Returns:
        None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        post = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and
    saves selected data to a CSV file.

    This function:
    - Sends an HTTP GET request to the
    JSONPlaceholder posts endpoint.
    - If the response status code is 200 (OK),
    it parses the JSON content.
    - Extracts a list of dictionaries
    containing 'id', 'title', and 'body' from each post.
    - Writes the extracted data to a CSV
    file named 'posts.csv' with columns 'id', 'title', and 'body'.

    Returns:
        None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json
        posts_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open(
            "posts.csv", mode="w", newline='', encoding="utf-8"
        ) as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_list)
