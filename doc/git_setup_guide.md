# Complete Beginner's Guide: Setting Up Git & GitHub

This guide assumes you've never used version control before. It covers **installing Git, configuring your identity, setting up authentication, and making your first commit**.

---

## Step 1: Install Git

🔹 **Windows**: Install [Git for Windows](https://git-scm.com/downloads) and select **“Use Git from the command line”** during setup.  
🔹 **Mac**: Run in Terminal:  
```bash
xcode-select --install
```
🔹 **Linux**: Install via package manager (e.g., Ubuntu/Debian: `sudo apt install git`)  

To check installation, run:  
```bash
git --version
```

---

## Step 2: Configure Git (One-Time Setup)

After installing Git, **set up your identity** (this is required for commits).  
Replace `"Your Name"` and `"your-email@example.com"` with your details:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

To check your setup:  
```bash
git config --list
```

🔹 **Why do this?** This ensures that every commit you make is linked to you.

---

## Step 3: Create a GitHub Account

1. **Go to [GitHub.com](https://github.com/) and sign up**.  
2. **Verify your email** and set up **2-factor authentication (optional but recommended)**.  

---

## Step 4: Create a Repository on GitHub

1. Go to [GitHub New Repo](https://github.com/new).  
2. **Enter a repository name** (e.g., `my-first-repo`).  
3. Choose **Public or Private**.  
4. **Check "Add a README"** (this makes it easier to get started).  
5. Click **Create Repository**.  

---

## Step 5: Clone the Repository to Your Computer

1. Copy the **HTTPS URL** of your repository (GitHub provides this).  
2. Open a terminal (or Git Bash on Windows) and run:

   ```bash
   git clone https://github.com/YOUR-USERNAME/my-first-repo.git
   cd my-first-repo
   ```

---

## Step 6: Set Up Authentication (Simplest Method)

GitHub requires authentication when pushing changes. The easiest way is:

### **Option A: Use GitHub CLI (Recommended)**

1. Install [GitHub CLI](https://cli.github.com/).  
2. Run:
   ```bash
   gh auth login
   ```
   - Select **GitHub.com**  
   - Choose **HTTPS**  
   - Authenticate via browser  
   
✅ **After this, pushing commits won’t ask for your password!**

### **Option B: Use a Personal Access Token (If Not Using `gh`)**

1. Go to **GitHub → Settings → Developer Settings → Personal Access Tokens**  
2. Click **Generate New Token (Classic)**  
3. Select **repo** permissions  
4. Copy the token and use it instead of a password when prompted  

---

## Step 7: Make Your First Change

1. Create a new file:
   ```bash
   echo "Hello, GitHub!" > hello.txt
   ```
2. Add it to Git:
   ```bash
   git add hello.txt
   ```
3. Commit the change:
   ```bash
   git commit -m "Added hello.txt"
   ```
4. Push it to GitHub:
   ```bash
   git push origin main
   ```

---

## Done! 🎉

✅ **Git is configured**  
✅ **GitHub account is set up**  
✅ **First commit pushed**  

This method is **clean, simple, and avoids SSH confusion**. 🚀
