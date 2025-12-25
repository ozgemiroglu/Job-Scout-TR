import os
import pandas as pd
from src import engine, provider

def run_job_scout():
    """Main execution function for the Job-Scout-TR application."""
    print("\n--- Job Scout AI: Starting Analysis ---")
    
    # 1. Load user configuration from me.txt
    config_path = "me.txt"
    if not os.path.exists(config_path):
        print(f"Error: Configuration file '{config_path}' not found.")
        return

    config = {}
    with open(config_path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, value = line.split(":", 1)
                config[key.strip()] = value.strip()

    # Dynamic Parameters
    search_keyword = config.get("ARANAN POZİSYON", "").strip()
    target_city = config.get("ŞEHİR", "Turkey").strip()
    user_profile = config.get("DENEYİM VE ÖZET", "").strip()

    # Validation
    if not search_keyword:
        print("Error: 'ARANAN POZİSYON' must be specified in me.txt.")
        return

    print(f"Target Role: {search_keyword}")
    print(f"Location: {target_city}")

    # 2. Fetch Jobs
    job_results = provider.fetch_jobs(search_keyword, target_city)

    if not job_results:
        print(f"No active jobs found for '{search_keyword}'.")
        return

    # 3. Scoring and Ranking
    print(f"Analyzing {len(job_results)} job descriptions against user profile...")
    scored_data = []
    
    for job in job_results:
        # Semantic similarity calculation
        match_score = engine.get_similarity(user_profile, job['desc'])
        scored_data.append({
            "Match Score (%)": round(match_score * 100, 2),
            "Position": job['title'],
            "Company": job['company'],
            "Job URL": job['link']
        })

    # Rank results by score in descending order
    df = pd.DataFrame(scored_data).sort_values(by="Match Score (%)", ascending=False)
    
    # 4. Export to Excel
    safe_filename = search_keyword.replace(' ', '_')
    output_filename = f"Analysis_Report_{safe_filename}.xlsx"
    df.to_excel(output_filename, index=False)
    
    print("\nAnalysis Complete!")
    print(f"Report saved to: {output_filename}")
    print("-" * 50)
    # Display top 5 matches in terminal
    print(df.head(5)[["Match Score (%)", "Position", "Company"]].to_string(index=False))

if __name__ == "__main__":
    run_job_scout()