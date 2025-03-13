## Outcome of Pregnancy Project

### Step-1: Create a Modular Code Structure

1. Create virtual environment:
    - "conda create -p venv -python==3.10 -y"
    - "conda activate venv/"

2. Create "src" folder followed by creating "__init__.py" file

3. Create a github repository and add ".gitignore" file (python)

4. Create "requirements.txt" file

5. Create a "README.md" file

6. Create "setup.py" file

7. Update git repository:
    - To sync README file from local to github "git add README.md"    
    - To check the which files are getting added "git status"
    - To commit the files "git commit -m "Initial commit"
    - To push the files to github "git push -u origin main"
    - To pull the files from github "git pull origin main"
    - To sync all files from local to github "git add ."

8. Under "src" folder create following files:
    - "__inti__.py"
    - exception.py
    - logger.py
    - util.py

9. Inside src create components folder with following files:
    - "__init__.py"
    - data_ingestion.py
    - data_transformation.py
    - data_visualization.py
    - model_trainer.py
    - model_evaluation.py
    - model_deployment.py

10. Inside src create pipeline folder with following files:
    - "__init__.py"
    - predict_pipeline.py
    - train_pipeline.py


