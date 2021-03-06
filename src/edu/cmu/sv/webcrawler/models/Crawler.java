package edu.cmu.sv.webcrawler.models;

import edu.cmu.sv.webcrawler.services.Get10K;
import edu.cmu.sv.webcrawler.services.GetRiskFactor;
import edu.cmu.sv.webcrawler.services.RequiredInfo;

import java.util.ArrayList;
import java.util.List;

public class Crawler {
	
	/**
	 * 
	 * @param symbol, 
	 * 				the CIK symbol for certian company
	 * @return 1 when Download10KbyCIK success, 
	 * 			-1 when Download10KbyCIK fail
	 */
	public int crawl(String symbol){
		//should try to call different crawling function here
		Get10K g = new Get10K();
		return g.Download10KbyCIK(symbol, false);
	}
	
	/**
	 * 
	 * @param symbol, 
	 * 				the CIK symbol for certian company
	 * @param docType,
	 * 				the documentType being crawled
	 * @return 1 when List returned by DownloadByCIKAndType return a list with size than zero,
	 * 			-1 when List returned by DownloadByCIKAndType return a list with size equal zero,
	 */
	public List<RequiredInfo> crawl(String symbol, String docType){
		GetRiskFactor g = new GetRiskFactor();
		List<RequiredInfo> results = new ArrayList<RequiredInfo>();
		System.out.printf("Request received\ndocType is %s\n",docType);
		if(docType.equals("all")) {
			RequiredInfo info = g.crawlAll2(symbol);
			results.add(info);
			return results;
		}
		
		return g.DownloadByCIKAndType(symbol, false, docType);

	}
}
