@echo off

python -m pip install pipreqs
pipreqs .
docker build -t pythonconcept .
docker run -d pythonconcept
