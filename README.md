 generate_app -n scrat -p .
python3 generate_model.py -n archivetbl -t sql
python3 generate_handler.py -n archivetbl -t sql --rest
python3 generate_scaffold.py -n archivetbl -t bs4
python3 server.py

export PYTHONPATH=$PYTHONPATH:/workspace

python3 generate_migration.py -n "added a archivetable model"
python3 update_db.py -d up
python3 update_db.py -d down
Your next steps: 
--------------------------------------------------
  1. [Optional step: create a virtualenv in you app directory]
      virtualenv /workspace/scrat
  2. cd to you new apps directory: /workspace/scrat
     [optionally activate the virtualenv]
  3. pip3 install -r requirements.txt
  4. run: python3 server.py
  5. open your browser with http://localhost:8080

  sqlalchemy.url = postgresql://docker:docker@pgdb:5432/scrat