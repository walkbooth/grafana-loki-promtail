# Grafana - Loki - Promtail Proof of Concept

Easy-setup Grafana/Loki/Promtail log collection and visualization stack.

- Grafana: handles frontend interface, hosted on grafana:3000 by default
- Loki: persists and indexes application logs, hosted on loki:3100 by default
- Promtail: daemon that discovers and sends logs to Loki

I've created an example python script that runs on the host and writes logs to a file. That file is mounted into the promtail container via a volume so that Promtail can watch it and talk to Loki when new logs are flushed.

## Prerequisites

- Docker
- Docker Compose
- Python 3

## Getting Started

1. `docker-compose up -d`
2. Navigate to Grafana at http://localhost:3000
3. [Add Loki as a data source in Grafana](https://grafana.com/docs/loki/latest/getting-started/grafana/) (URL is http://loki:3100 since you're using docker-compose)
4. Start the "app": `python ./app.py` (it will start writing logs on the host machine, Ctrl + C to stop it)
5. Create some dashboards on Grafana!

## Helpful Resources

- [LogQL](https://grafana.com/docs/loki/latest/logql/): syntax for designing queries. Super flexible, and lots of ways to display query results in Grafana
- [Panel overview](https://grafana.com/docs/grafana/latest/panels/panels-overview/): describes how to create and manage panels in a dashboard
