# How to Upload to GitHub

## 1. Create a New Repository

1. Go to [GitHub](https://github.com/new)
2. Sign in to your account
3. Click "New repository"
4. Give it a name (e.g., `Basketball_Analytics_Dashboard`)
5. Add a description (optional)
6. Choose "Public" or "Private"
7. Click "Create repository"

## 2. Upload via Git (Recommended)

```bash
# Navigate to your project folder
cd Basketball_Analytics_Dashboard

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit - Basketball Analytics Dashboard"

# Add remote repository (replace USERNAME and REPO_NAME)
git remote add origin https://github.com/USERNAME/REPO_NAME.git

# Push to GitHub (use 'main' or 'master' depending on your setup)
git branch -M main
git push -u origin main
```

## 3. Upload via Web (No Git Required)

1. Go to your new repository on GitHub
2. Click "Add file" → "Upload files"
3. Drag and drop files or click to select
4. Add a commit message
5. Click "Commit changes"

## 4. After Upload

Your project will be visible at:
```
https://github.com/USERNAME/REPO_NAME
```

You can now:
- Share the link with others
- Collaborate with team members
- Track changes with commits
- Use GitHub features (issues, discussions, etc.)
