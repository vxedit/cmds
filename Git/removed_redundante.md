---

## **Basic Git Commands redundancies removed. **

### **Initialize and Add Files**
- Initialize a repository:
  ```bash
  git init
  ```
- Add files to the staging area:
  ```bash
  git add .
  ```
- Commit changes:
  ```bash
  git commit -m "Your commit message"
    ```

### **Remove Files or Cache**
- Remove cached files:
  ```bash
  git rm --cached -r '/_pycache_'
  git rm --cached -r .env
  ```

---

## **Connecting to a Remote Repository**

### **Add or Update Remote**
- Add remote:
  ```bash
  git remote add origin <remote-url>
  ```
- Verify remote:
  ```bash
  git remote -v
  ```
- Update remote URL:
  ```bash
  git remote set-url origin <new-url>
  ```
- Remove remote:
  ```bash
  git remote remove origin
  ```

### **Push to Remote**
- Push branch to remote and set upstream:
  ```bash
  git push -u origin <branch-name>
  ```
- Force push (if necessary):
  ```bash
  git push origin <branch-name> --force
  ```

---

## **Branch Management**

### **Create, Rename, and Switch Branches**
- Create and switch to a new branch:
  ```bash
  git checkout -b <branch-name>
  ```
- Rename the current branch:
  ```bash
  git branch -m <new-branch-name>
  ```
- Switch to an existing branch:
  ```bash
  git checkout <branch-name>
  ```

### **Set Upstream**
- Set upstream branch:
  ```bash
  git push --set-upstream origin <branch-name>
  ```

### **Delete Branch**
- Delete a branch remotely:
  ```bash
  git push origin --delete <branch-name>
  ```

---

## **Pull, Merge, and Rebase**

### **Pull Changes**
- Pull changes from a remote branch:
  ```bash
  git pull origin <branch-name>
  ```
- Pull with unrelated histories:
  ```bash
  git pull origin <branch-name> --allow-unrelated-histories
  ```

### **Merge**
- Merge another branch into the current branch:
  ```bash
  git merge <branch-name>
  ```

### **Rebase**
- Pull and rebase local changes on top of remote:
  ```bash
  git pull --rebase
  ```
- Continue rebase after resolving conflicts:
  ```bash
  git rebase --continue
  ```

---

## **Undoing Changes**

### **Reset**
- for recent HEAD positions
  ```bash
  git reflog
  ```
- move head
  ```bash
  git reset --hard 710070d
  ```
- Soft reset (keep changes staged):
  ```bash
  git reset --soft HEAD~1
  ```
- Hard reset (discard all changes):
  ```bash
  git reset --hard HEAD~1
  ```

### **Revert**
- Create a new commit to undo changes:
  ```bash
  git revert HEAD
  ```

---

## **Tagging and Releases**

### **Create and Push Tags**
- Create a tag:
  ```bash
  git tag -a v1.0.0 -m "Release version 1.0.0"
  ```
- Push tag to remote:
  ```bash
  git push origin v1.0.0
  ```

### **Prepare for Release**
- Commit and tag for a release:
  ```bash
  git add .
  git commit -m "Prepare release v1.0.0"
  git tag -a v1.0.0 -m "Release version 1.0.0"
  git push origin master
  git push origin v1.0.0
  ```

---

## **SSH Setup**

### **Generate and Add SSH Key**
- Generate an SSH key:
  ```bash
  ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
  ```
- Display the public key:
  ```bash
  cat ~/.ssh/id_rsa.pub
  ```
- Add the public key to GitHub/GitLab.

### **Test SSH Connection**
```bash
ssh -T git@github.com
```

---

## **User Configuration**

### **View or Set User Information**
- View current configuration:
  ```bash
  git config --list
  ```
- Set global user details:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your-email@example.com"
  ```
- Set local user details:
  ```bash
  git config --local user.name "Your Name"
  git config --local user.email "your-email@example.com"
  ```

---

## **Conflict Resolution**

### **Handling Conflicts During Rebase**
- After pulling with `--rebase`, resolve conflicts and continue:
  ```bash
  git rebase --continue
  ```

### **Handling Merge Conflicts**
- Manually resolve conflicts in files.
- Stage the resolved files:
  ```bash
  git add <file-name>
  ```
- Complete the merge:
  ```bash
  git merge --continue
  ```

---

## **Divergent Branch Workflow**

### **Rebase**
- Rebase local commits on top of remote:
  ```bash
  git pull --rebase
  ```

### **Merge**
- Pull and merge with no rebase:
  ```bash
  git pull --no-rebase origin master
  ```

---
