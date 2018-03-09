from Data_Extractor.Querry_Scrapper import Scrapper

if __name__ == '__main__':	
	query=str(input('Enter Query : '))
	s=Scrapper()
	s.scrape(query)
