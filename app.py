import gradio as gr
from resume_optimizer import optimize_resume_section
from job_description_analyzer import extract_skills_from_jd, compare_resume_with_jd

def rewrite(section, tone, job_title):
    if not section.strip():
        return "⚠️ Please enter a resume section."
    return optimize_resume_section(section, tone, job_title)

def analyze(jd, resume):
    skills = extract_skills_from_jd(jd)
    score = compare_resume_with_jd(resume, jd)
    return ", ".join(skills), f"{score} %"

with gr.Blocks(title="JobGenie: AI-Powered Career Assistant") as demo:
    gr.Markdown("""
    # 💼 JobGenie
    _An AI-powered assistant to rewrite your resume, analyze job descriptions, and boost your job applications._
    """)

    with gr.Tab("✍️ Resume Optimizer"):
        gr.Markdown("### Enhance your resume section with AI")

        with gr.Row():
            section_input = gr.Textbox(
                label="📄 Resume Section",
                lines=6,
                placeholder="Paste your current resume section here"
            )

        with gr.Row():
            tone_input = gr.Dropdown(
                choices=["professional", "confident", "concise", "friendly"],
                label="🎯 Tone",
                value="professional"
            )
            job_title_input = gr.Textbox(
                label="💼 Target Job Title (optional)",
                placeholder="e.g. Cloud Engineer"
            )

        with gr.Row():
            btn = gr.Button("🚀 Rewrite Section")

        output = gr.Textbox(label="✨ Rewritten Resume Section", lines=6)

        btn.click(fn=rewrite, inputs=[section_input, tone_input, job_title_input], outputs=output)

    with gr.Tab("📊 Job Description Analyzer"):
        gr.Markdown("### Extract skills from a job description and calculate your job fit score")

        with gr.Row():
            with gr.Column():
                jd_input = gr.Textbox(
                    label="📝 Job Description",
                    lines=6,
                    placeholder="Paste job description here"
                )
            with gr.Column():
                resume_input = gr.Textbox(
                    label="📋 Your Resume Text",
                    lines=6,
                    placeholder="Paste your resume section here"
                )

        analyze_button = gr.Button("🔍 Analyze Job Fit")

        with gr.Row():
            skills_output = gr.Textbox(label="🔑 Extracted Skills from JD")
            score_output = gr.Textbox(label="💯 Job Fit Score (%)")

        analyze_button.click(
            fn=analyze,
            inputs=[jd_input, resume_input],
            outputs=[skills_output, score_output]
        )

# Launch in browser
if __name__ == "__main__":
    demo.launch()
