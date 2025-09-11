# Personal Financial Tracker

 #### Video Demo: <URL HERE>

# Description

As I brainstormed, I knew I could easily get carried away and try to add every possible feature. In order to avoid getting stuck, I decided to start with the MVP (Minimum Viable Product) - the smallest version of the app that still works. I also made a list of ideas for future phases, but kept them separate from what I needed for the first version. I could focus on finishing something instead of trying to be perfect.

# Approach

Here’s the approach I followed:

1. Requirements Gathering

I wrote down everything I wanted the tracker to do. Those were the core features for the MVP:

- Be able to enter income transactions.
- Enter expense transactions.
- Categorize the transaction
- Send those transactions to Notion so they appear in my financial dashboard.

Future ideas I am planning to work on when I start studying for the Azure certificaiton AI-102 is adding natural-processing language, chatbot, Plaid API, and a Flask component.

2. Breaking It Down Into Components

Then I broke the project into smaller, manageable pieces. It was much easier to stay motivated and avoid feeling overwhelmed when I tackled smaller chunks of work. There were three main components:

- Main Function - This is the start of the program. This is where the app asks the user if they want to log income or expenses, then directs them to the right section.
- Class Budget Categories - Stores my income and expense categories. This ensures consistency-rather than manually typing a category name (and risking typos), I can select from predefined ones.
- Transactions Class - Handles adding transactions. This class processes any amount, assigns a category, and prepares it for Notion.
-  Notion Class - Here's where things got tough. The Notion API isn't too complicated, but I had to figure out how to structure the requests so that the data lands where I want it in my dashboard. I watched YouTube tutorials, read the official Notion API documentation, and even searched Stack Overflow and Reddit for examples from other developers. It helped me understand the little details that weren't obvious from the documentation.
- Created My Own CS50.ai - I really found the CS50.ai useful.  Therefore, I created my own ChatGPT version of it.  I created an agent where I specified to never give me the code but to help me with troubleshooting efforts so it could help me figure out what was wrong with my code.

With this step-by-step approach, I was able to complete my financial tracker's first version, by planning the MVP, breaking it down into smaller components, and learning from multiple resources. Although it's not perfect yet, it's functional, and I now have a solid foundation to build on.
