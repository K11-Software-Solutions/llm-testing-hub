import time
import threading
import schedule
from agent import LLMEvalAgent
from utils import setup_logging

def scheduled_job():
    agent = LLMEvalAgent()
    agent.run_tests()

def run_scheduler(cron_expr=None):
    setup_logging()
    # For demo: run every day at midnight
    schedule.every().day.at("00:00").do(scheduled_job)
    print("Scheduler started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    run_scheduler()
