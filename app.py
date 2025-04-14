
import gradio as gr
from resume_optimizer import optimize_resume_section

def rewrite(section, tone, job_title):
    if not section.strip():
        return "!! Please enter a resume section."
    return optimize_resume_section(section, tone, job_title)

with gr.Blocks() as demo:
    gr.Markdown("# Resume Optimizer\nImprove your resume section using AI!")

    section_input = gr.Textbox(label=" Resume Section", lines=6, placeholder="Paste your current resume section here")
    tone_input = gr.Dropdown(choices=["professional", "confident", "concise", "friendly"], label=" Tone", value="professional")
    job_title_input = gr.Textbox(label=" Target Job Title (optional)", placeholder="e.g. Cloud Engineer")

    output = gr.Textbox(label=" Rewritten Resume Section", lines=6)

    btn = gr.Button(" Rewrite")

    btn.click(fn=rewrite, inputs=[section_input, tone_input, job_title_input], outputs=output)

# Launch in browser
if __name__ == "__main__":
    demo.launch()
