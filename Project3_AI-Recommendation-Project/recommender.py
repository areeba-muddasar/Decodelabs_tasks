"""
Project 3: AI Recommendation Logic - CLI Version
Tech Stack Recommender
DecodeLabs | Batch 2026
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


CSV_FILE = 'raw_skills.csv'
MIN_SKILLS = 3
DEFAULT_TOP_N = 3


def load_data(filepath=CSV_FILE):
    if not os.path.exists(filepath):
        print(f"❌ Error: {filepath} not found!")
        return None
    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} job roles from {filepath}")
    return df


def build_model(df):
    vectorizer = TfidfVectorizer()
    job_vectors = vectorizer.fit_transform(df['skills'])
    print(f"✅ TF-IDF model built (vocabulary size: {len(vectorizer.get_feature_names_out())})")
    return vectorizer, job_vectors


def get_recommendations(user_skills, vectorizer, job_vectors, df, top_n=DEFAULT_TOP_N):
    user_vector = vectorizer.transform([' '.join(user_skills)])
    scores = cosine_similarity(user_vector, job_vectors).flatten()
    df_result = df.copy()
    df_result['similarity_score'] = scores
    df_sorted = df_result.sort_values(by='similarity_score', ascending=False)
    return df_sorted.head(top_n)


def display_results(recommendations):
    print("\n" + "=" * 65)
    print("🎯 TOP RECOMMENDED CAREER PATHS")
    print("=" * 65)
    for rank, (idx, row) in enumerate(recommendations.iterrows(), 1):
        match_pct = row['similarity_score'] * 100
        bar_length = int(match_pct / 2)
        bar = '█' * bar_length + '░' * (50 - bar_length)
        print(f"\n{rank}. {row['job_role']}")
        print(f"   [{bar}] {match_pct:.2f}%")
        print(f"   Required Skills: {row['skills']}")
        print(f"   {'─' * 60}")


def main():
    print("=" * 65)
    print("🎯 TECH STACK RECOMMENDER - CLI")
    print("   Powered by DecodeLabs | Project 3")
    print("=" * 65)
    
    df = load_data()
    if df is None:
        return
    
    vectorizer, job_vectors = build_model(df)
    
    print("\n📝 Enter your skills (minimum 3, comma separated)")
    print("   Example: Python, Cloud, Automation")
    user_input = input("\n> ")
    
    user_skills = [s.strip().lower() for s in user_input.split(',') if s.strip()]
    
    if len(user_skills) < MIN_SKILLS:
        print(f"❌ Error: Please enter at least {MIN_SKILLS} skills!")
        return
    
    print(f"\n✅ Your skills: {user_skills}")
    
    recommendations = get_recommendations(user_skills, vectorizer, job_vectors, df)
    display_results(recommendations)
    
    print("\n" + "=" * 65)
    print("Thank you for using Tech Stack Recommender!")
    print("=" * 65)


if __name__ == "__main__":
    main()