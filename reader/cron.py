from django_cron import cronScheduler, Job
import logging

logger = logging.getlogger(__name__)

class CheckNews(Job):
	run_every = 120

	def job(self):
		logger.log('piu')

cronScheduler.register(CheckNews)