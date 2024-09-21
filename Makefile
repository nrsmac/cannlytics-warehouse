download-data:
	poetry run python scripts/download_data.py
load-data: 
	poetry run python scripts/load_data.py
transform-data:
	cd src/transformations && poetry run dbt run 
docs:
	cd src/transformations && poetry run dbt docs generate && poetry run dbt docs serve 
export-materialized-views:
	poetry run python scripts/export_materialized_views.py
generate-frontend-requirements:
	poetry run python scripts/extract_dependencies.py frontend > src/frontend/requirements.txt
build-frontend-docker: transform-data
	docker build -t canalyte-frontend .  --network=host
run-dev:
	poetry run streamlit run src/frontend/app.py
run-frontend-docker: build-frontend-docker
	docker run -p 8501:8501 -it canalyte-frontend 

