# -*- coding: utf-8 -*-
from jobspy import scrape_jobs
import pandas as pd

def fetch_jobs(keyword, location="Turkey"):
    """
    Fetches active job listings from LinkedIn and Indeed using python-jobspy.
    Prioritizes LinkedIn and retrieves up to 100 results without time restrictions.
    """
    print(f"\n--- Scraping job listings for '{keyword}' in {location} ---")
    
    try:
        # Scrape jobs from multiple platforms
        jobs = scrape_jobs(
            site_name=["linkedin", "indeed"], 
            search_term=keyword,
            location=location,
            results_wanted=100,      
            country_indeed='turkey'
        )
        
        job_list = []
        
        # Guard clause for empty results
        if jobs is None or jobs.empty:
            print("No jobs were found during the scraping process.")
            return []

        # Process and clean the dataframe rows
        for index, row in jobs.iterrows():
            title = str(row.get('title', 'N/A'))
            company = str(row.get('company', 'N/A'))
            description = str(row.get('description', ''))
            job_url = str(row.get('job_url', ''))

            job_list.append({
                "title": title,
                "company": company,
                "desc": f"{title} {description}", # Concatenate title and desc for engine analysis
                "link": job_url
            })
            
        return job_list

    except Exception as e:
        print(f"Error during job scraping: {e}")
        return []