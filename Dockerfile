FROM openjdk:8-bullseye
WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip install -r requirements.txt


CMD ["python3", "WorkoutPlan_1301190417.py"]