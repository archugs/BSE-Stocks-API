
class BSEStockQuotes(object):

	def __init__(self, companies):
		self.companies = companies
		self.stockQuotes = {}
		self.get_stock_quotes()

	def get_stock_quotes(self):
		raise NotImplementedError("Subclasses are responsible for creating this method")


