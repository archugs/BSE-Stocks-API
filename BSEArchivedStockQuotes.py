from BSEStockQuotes import BSEStockQuotes
from CompanyArchivedQuotes import CompanyArchivedQuotes

class BSEArchivedStockQuotes(BSEStockQuotes):

	def get_stock_quotes(self):
		for company in self.companies:
			self.stockQuotes[company] = CompanyArchivedQuotes(company)

	def print_output(self, delimiter='\t'):
		CompanyArchivedQuotes.print_headers(delimiter)
		for company in self.companies:
			self.stockQuotes[company].print_info(delimiter)


#Testing
#lstCodes = ["500180", "500209"]
#st = BSEArchivedStockQuotes(lstCodes)
#print st.stockQuotes["500180"].day_high[5]
#for code in lstCompanyCodes:
#	print st.stockQuotes[code].companyname
#	print st.stockQuotes[code].date[3]
#	print st.stockQuotes[code].total_turnover[3]
#st.print_output()
