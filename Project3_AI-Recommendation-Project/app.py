"""
============================================================
Project 3: AI Recommendation Logic
Tech Stack Recommender - Streamlit Web App
============================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import os


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Tech Stack Recommender",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD CUSTOM CSS FROM EXTERNAL FILE
# ============================================================
def load_css(filepath='assets/styles.css'):
    """Load custom CSS from external file"""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ CSS file not found: {filepath}")


load_css()


# ============================================================
# DATA LOADING
# ============================================================
@st.cache_data
def load_data(filepath='raw_skills.csv'):
    if not os.path.exists(filepath):
        st.error(f"❌ '{filepath}' not found!")
        st.stop()
    return pd.read_csv(filepath)


@st.cache_resource
def build_model(df):
    vectorizer = TfidfVectorizer()
    job_vectors = vectorizer.fit_transform(df['skills'])
    return vectorizer, job_vectors


# ============================================================
# HELPERS
# ============================================================
def recommend(user_skills, vectorizer, job_vectors, df, top_n=5):
    user_vector = vectorizer.transform([' '.join(user_skills)])
    scores = cosine_similarity(user_vector, job_vectors).flatten()
    result = df.copy()
    result['score'] = scores
    return result.sort_values('score', ascending=False).head(top_n)


def get_skill_gap(user_skills, job_skills):
    user_set = set(s.lower() for s in user_skills)
    job_set = set(job_skills.lower().split())
    return user_set & job_set, job_set - user_set, user_set - job_set


def get_badge(pct):
    if pct >= 50: return "🟢 Excellent", "badge-excellent"
    elif pct >= 30: return "🟡 Good", "badge-good"
    elif pct >= 15: return "🟠 Fair", "badge-fair"
    else: return "🔴 Low", "badge-low"


def render_skill_tags(skills_str):
    return ' '.join(f'<span class="skill-tag">{s}</span>' for s in skills_str.split())


# ============================================================
# MAIN APP
# ============================================================
def main():
    # ---------- HEADER ----------
    st.markdown('<h1 class="main-title">🎯 Tech Stack Recommender</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI-Powered Career Path Recommendation </p>', unsafe_allow_html=True)
    
    # ---------- LOAD ----------
    df = load_data()
    vectorizer, job_vectors = build_model(df)
    
    # ============================================================
    # SIDEBAR
    # ============================================================
    with st.sidebar:
        st.markdown("## ⚙️ Settings")
        st.markdown("---")
        st.markdown("### 📊 Dataset Info")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Jobs", len(df))
        with c2:
            st.metric("Skills", len(vectorizer.get_feature_names_out()))
        st.markdown("---")
        st.markdown("### 🎛️ Options")
        top_n = st.slider("Top N Recommendations", 1, 10, 5)
        show_chart = st.checkbox("Show Bar Chart", value=True)
        show_gap = st.checkbox("Show Skill Gap", value=True)
        st.markdown("---")
        st.caption("Built with ❤️ using Streamlit")
        st.caption("DecodeLabs | Batch 2026")
    
    # ============================================================
    # 6 TABS
    # ============================================================
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🎯 Recommendations",
        "📋 Job Directory",
        "🔍 Search & Filter",
        "📊 Analytics",
        "⚖️ Compare Jobs",
        "📊 Dataset Info"
    ])
    
    # ============================================================
    # TAB 1: RECOMMENDATIONS
    # ============================================================
    with tab1:
        st.markdown("### 📝 Enter Your Skills")
        st.caption("Type at least **3 skills** separated by commas.")
        
        st.markdown("**⚡ Quick Examples:**")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if st.button("🐍 Python Dev", use_container_width=True):
                st.session_state.skills_input = "Python, SQL, APIs"
        with c2:
            if st.button("☁️ Cloud Eng", use_container_width=True):
                st.session_state.skills_input = "AWS, Docker, Kubernetes"
        with c3:
            if st.button("🌐 Frontend", use_container_width=True):
                st.session_state.skills_input = "JavaScript, React, CSS"
        with c4:
            if st.button("🤖 AI/ML", use_container_width=True):
                st.session_state.skills_input = "Python, TensorFlow, Deep Learning"
        
        user_input = st.text_input(
            "Your skills:",
            value=st.session_state.get('skills_input', ''),
            placeholder="e.g., Python, Cloud, Automation",
            key="input_field"
        )
        
        if st.button("🚀 Get Recommendations", type="primary", use_container_width=True):
            if not user_input.strip():
                st.warning("⚠️ Please enter your skills!")
            else:
                skills = [s.strip().lower() for s in user_input.split(',') if s.strip()]
                if len(skills) < 3:
                    st.error(f"❌ Please enter at least 3 skills! You entered {len(skills)}.")
                else:
                    with st.spinner("🔄 Analyzing..."):
                        recs = recommend(skills, vectorizer, job_vectors, df, top_n)
                    
                    st.success(f"✅ Found {len(recs)} matches!")
                    st.markdown("---")
                    
                    for rank, (_, row) in enumerate(recs.iterrows(), 1):
                        pct = row['score'] * 100
                        badge_text, badge_class = get_badge(pct)
                        st.markdown(f"""
                        <div class="rec-card">
                            <h3>{rank}. {row['job_role']}
                                <span class="match-badge {badge_class}">{badge_text} {pct:.1f}%</span>
                            </h3>
                            <p><strong>Skills:</strong></p>
                            <p>{render_skill_tags(row['skills'])}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.progress(min(pct / 100, 1.0))
                    
                    if show_chart:
                        st.markdown("---")
                        st.markdown("### 📊 Match Comparison")
                        chart = recs[['job_role', 'score']].copy()
                        chart['pct'] = chart['score'] * 100
                        chart = chart.sort_values('pct')
                        fig = px.bar(
                            chart, x='pct', y='job_role', orientation='h',
                            color='pct', color_continuous_scale='Viridis', text='pct'
                        )
                        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
                        fig.update_layout(height=350, showlegend=False,
                            xaxis_title="Match %", yaxis_title="",
                            margin=dict(l=0, r=40, t=20, b=20))
                        st.plotly_chart(fig, use_container_width=True)
                    
                    if show_gap:
                        st.markdown("---")
                        st.markdown("### 📊 Skill Gap Analysis")
                        top_role = recs.iloc[0]
                        matched, missing, extra = get_skill_gap(skills, top_role['skills'])
                        c1, c2, c3 = st.columns(3)
                        with c1:
                            st.markdown("#### ✅ You Have")
                            for s in sorted(matched) or ["None"]:
                                st.markdown(f"- `{s}`")
                        with c2:
                            st.markdown("#### ❌ To Learn")
                            for s in sorted(missing)[:8] or ["None"]:
                                st.markdown(f"- `{s}`")
                        with c3:
                            st.markdown("#### ➕ Extra")
                            for s in sorted(extra) or ["None"]:
                                st.markdown(f"- `{s}`")
                    
                    st.markdown("---")
                    csv = recs.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Download Results (CSV)",
                        data=csv,
                        file_name=f"recommendations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime='text/csv',
                        use_container_width=True
                    )
    
    # ============================================================
    # TAB 2: JOB DIRECTORY
    # ============================================================
    with tab2:
        st.markdown("### 📋 Job Role Directory")
        st.caption(f"Browse all **{len(df)}** job roles")
        
        sort_by = st.radio("Sort by:", ["Name (A-Z)", "Name (Z-A)", "Skill Count"], horizontal=True)
        
        if sort_by == "Name (A-Z)":
            display_df = df.sort_values('job_role')
        elif sort_by == "Name (Z-A)":
            display_df = df.sort_values('job_role', ascending=False)
        else:
            display_df = df.copy()
            display_df['skill_count'] = display_df['skills'].str.split().str.len()
            display_df = display_df.sort_values('skill_count', ascending=False)
        
        st.markdown("---")
        
        for _, row in display_df.iterrows():
            with st.expander(f"💼 {row['job_role']}"):
                st.markdown(f"**Total Skills:** {len(row['skills'].split())}")
                st.markdown("**Required Skills:**")
                st.markdown(render_skill_tags(row['skills']), unsafe_allow_html=True)
    
    # ============================================================
    # TAB 3: SEARCH & FILTER
    # ============================================================
    with tab3:
        st.markdown("### 🔍 Search & Filter Jobs")
        
        search = st.text_input("🔍 Search by keyword:", placeholder="e.g., data, cloud, engineer")
        
        st.markdown("**Filter by Category:**")
        categories = {
            "All": [],
            "Data": ['data', 'analyst', 'scientist', 'bi', 'analytics'],
            "Web": ['frontend', 'backend', 'full stack', 'web'],
            "Cloud": ['cloud', 'devops', 'sre', 'site reliability'],
            "Security": ['security', 'penetration', 'soc'],
            "AI": ['ml', 'ai', 'machine learning', 'nlp', 'vision', 'generative', 'prompt'],
            "Mobile": ['mobile', 'ios', 'android'],
            "Game": ['game', 'ar', 'vr'],
        }
        selected_cat = st.selectbox("Category:", list(categories.keys()))
        
        filtered = df.copy()
        if search:
            filtered = filtered[filtered['job_role'].str.lower().str.contains(search.lower())]
        if selected_cat != "All":
            keywords = categories[selected_cat]
            mask = filtered['job_role'].str.lower().apply(
                lambda x: any(kw in x for kw in keywords)
            )
            filtered = filtered[mask]
        
        st.caption(f"Showing **{len(filtered)}** results")
        st.markdown("---")
        
        if filtered.empty:
            st.info("No jobs match your filters.")
        else:
            for _, row in filtered.iterrows():
                with st.expander(f"💼 {row['job_role']}"):
                    st.markdown(f"**Skills:**")
                    st.markdown(render_skill_tags(row['skills']), unsafe_allow_html=True)
    
    # ============================================================
    # TAB 4: ANALYTICS
    # ============================================================
    with tab4:
        st.markdown("### 📊 Dataset Analytics")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Total Jobs", len(df))
        with c2:
            st.metric("Unique Skills", len(vectorizer.get_feature_names_out()))
        with c3:
            avg = df['skills'].str.split().str.len().mean()
            st.metric("Avg Skills/Job", f"{avg:.1f}")
        with c4:
            total = df['skills'].str.split().str.len().sum()
            st.metric("Total Skill Entries", total)
        
        st.markdown("---")
        
        st.markdown("### 📈 Top 20 Most Common Skills")
        all_skills = ' '.join(df['skills']).lower().split()
        counts = pd.Series(all_skills).value_counts().head(20)
        fig1 = px.bar(
            x=counts.values, y=counts.index, orientation='h',
            color=counts.values, color_continuous_scale='Blues'
        )
        fig1.update_layout(height=500, showlegend=False,
            xaxis_title="Frequency", yaxis_title="",
            margin=dict(l=0, r=20, t=20, b=20))
        st.plotly_chart(fig1, use_container_width=True)
        
        st.markdown("### 📊 Skills Distribution per Job")
        df_chart = df.copy()
        df_chart['skill_count'] = df_chart['skills'].str.split().str.len()
        df_chart = df_chart.sort_values('skill_count', ascending=False).head(20)
        fig2 = px.bar(
            df_chart, x='job_role', y='skill_count',
            color='skill_count', color_continuous_scale='Purples'
        )
        fig2.update_layout(height=450, showlegend=False,
            xaxis_title="", yaxis_title="Number of Skills",
            xaxis_tickangle=-45)
        st.plotly_chart(fig2, use_container_width=True)
        
        st.markdown("### 🥧 Category Distribution")
        categories = {
            "Data": ['data', 'analyst', 'scientist', 'bi', 'analytics'],
            "Web": ['frontend', 'backend', 'full stack', 'web'],
            "Cloud": ['cloud', 'devops', 'sre', 'site reliability'],
            "Security": ['security', 'penetration', 'soc'],
            "AI": ['ml', 'ai', 'machine learning', 'nlp', 'vision', 'generative', 'prompt'],
            "Mobile": ['mobile', 'ios', 'android'],
            "Game": ['game', 'ar', 'vr'],
            "Other": []
        }
        cat_counts = {cat: 0 for cat in categories}
        for _, row in df.iterrows():
            role = row['job_role'].lower()
            matched = False
            for cat, kws in categories.items():
                if cat == "Other":
                    continue
                if any(kw in role for kw in kws):
                    cat_counts[cat] += 1
                    matched = True
                    break
            if not matched:
                cat_counts["Other"] += 1
        
        pie_df = pd.DataFrame({
            'Category': list(cat_counts.keys()),
            'Count': list(cat_counts.values())
        })
        pie_df = pie_df[pie_df['Count'] > 0]
        fig3 = px.pie(
            pie_df, values='Count', names='Category',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig3.update_layout(height=400)
        st.plotly_chart(fig3, use_container_width=True)
    
    # ============================================================
    # TAB 5: COMPARE JOBS
    # ============================================================
    with tab5:
        st.markdown("### ⚖️ Compare Two Job Roles")
        st.caption("Select two job roles to compare their required skills side-by-side.")
        
        col1, col2 = st.columns(2)
        with col1:
            job1 = st.selectbox("Job Role 1:", df['job_role'].tolist(), key="job1")
        with col2:
            job2 = st.selectbox("Job Role 2:", df['job_role'].tolist(), 
                                index=min(1, len(df)-1), key="job2")
        
        if job1 == job2:
            st.warning("⚠️ Please select two different job roles.")
        else:
            skills1 = set(df[df['job_role'] == job1].iloc[0]['skills'].lower().split())
            skills2 = set(df[df['job_role'] == job2].iloc[0]['skills'].lower().split())
            
            common = skills1 & skills2
            only1 = skills1 - skills2
            only2 = skills2 - skills1
            
            jv1 = vectorizer.transform([df[df['job_role'] == job1].iloc[0]['skills']])
            jv2 = vectorizer.transform([df[df['job_role'] == job2].iloc[0]['skills']])
            job_sim = cosine_similarity(jv1, jv2)[0][0] * 100
            
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Job Similarity", f"{job_sim:.1f}%")
            with c2:
                st.metric("Common Skills", len(common))
            with c3:
                st.metric("Total Unique Skills", len(skills1 | skills2))
            
            st.markdown("---")
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f'<div class="compare-card"><h3>💼 {job1}</h3>', unsafe_allow_html=True)
                st.markdown(f"**Total Skills:** {len(skills1)}")
                st.markdown("**All Skills:**")
                st.markdown(render_skill_tags(' '.join(sorted(skills1))), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with c2:
                st.markdown(f'<div class="compare-card"><h3>💼 {job2}</h3>', unsafe_allow_html=True)
                st.markdown(f"**Total Skills:** {len(skills2)}")
                st.markdown("**All Skills:**")
                st.markdown(render_skill_tags(' '.join(sorted(skills2))), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### 📋 Skill Breakdown")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f"#### 🤝 Common ({len(common)})")
                for s in sorted(common) or ["None"]:
                    st.markdown(f"- `{s}`")
            with c2:
                st.markdown(f"#### 1️⃣ Only in {job1} ({len(only1)})")
                for s in sorted(only1) or ["None"]:
                    st.markdown(f"- `{s}`")
            with c3:
                st.markdown(f"#### 2️⃣ Only in {job2} ({len(only2)})")
                for s in sorted(only2) or ["None"]:
                    st.markdown(f"- `{s}`")
    
    # ============================================================
    # TAB 6: DATASET INFO
    # ============================================================
    with tab6:
        st.markdown("### 📊 Full Dataset")
        st.dataframe(df, use_container_width=True, height=400)
        
        st.markdown("---")
        st.markdown("### 📥 Download Dataset")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Download raw_skills.csv",
            data=csv,
            file_name="raw_skills.csv",
            mime='text/csv',
            use_container_width=True
        )
        
        st.markdown("---")
        st.markdown("### ℹ️ About This Project")
        st.markdown("""
        **Project 3: AI Recommendation Logic**  
        **Domain:** Artificial Intelligence  
        **Batch:** 2026  
        
        This project uses **Content-Based Filtering** with:
        - **TF-IDF** (Term Frequency - Inverse Document Frequency) for feature extraction
        - **Cosine Similarity** for measuring alignment between user profile and job roles
        - **IPO Model** (Input → Process → Output)
        
        **Pipeline:**
        1. **Ingestion** — User enters 3+ skills
        2. **Scoring** — TF-IDF vectors + Cosine similarity
        3. **Sorting** — Results sorted descending
        4. **Filtering** — Top-N returned
        """)
    
    # ---------- FOOTER ----------
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")


if __name__ == "__main__":
    main()