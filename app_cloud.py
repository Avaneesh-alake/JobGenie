import gradio as gr
from resume_optimizer import optimize_resume_section
from job_description_analyzer_cloud import extract_skills_from_jd_keywords, compare_resume_with_jd
from voice_interview_cloud import transcribe_audio_file, analyze_speech_feedback
import os

def rewrite(section, tone, job_title):
    if not section.strip():
        return "⚠️ Please enter a resume section."
    return optimize_resume_section(section, tone, job_title)

def analyze(jd, resume):
    skills = extract_skills_from_jd_keywords(jd)   # only KeyBERT
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
                label="Resume Section",
                lines=6,
                placeholder="Paste your current resume section here"
            )

        with gr.Row():
            tone_input = gr.Dropdown(
                choices=["professional", "confident", "concise", "friendly"],
                label="Tone",
                value="professional"
            )
            job_title_input = gr.Textbox(
                label="Target Job Title (optional)",
                placeholder="e.g. Cloud Engineer"
            )

        with gr.Row():
            btn = gr.Button("Rewrite Section")

        output = gr.Textbox(label="Rewritten Resume Section", lines=6)

        btn.click(fn=rewrite, inputs=[section_input, tone_input, job_title_input], outputs=output)

    with gr.Tab("📝 Job Description Analyzer"):
        gr.Markdown("### Extract skills from a job description using two methods:\n- 🧠 Existing keyword extractor\n- 🤖 Your fine-tuned AI model")
        with gr.Row():
            with gr.Column():
                jd_input = gr.Textbox(
                    label="Job Description",
                    lines=6,
                    placeholder="Paste job description here"
                )
            with gr.Column():
                resume_input = gr.Textbox(
                    label="Your Resume Text",
                    lines=6,
                    placeholder="Paste your resume section here"
                )

        analyze_button = gr.Button("Analyze Job Fit")

        with gr.Row():
            keyword_skills_output = gr.Textbox(label="Skills from Keyword Extractor")
            finetuned_skills_output = gr.Textbox(label="Skills from Fine-Tuned Model")
        with gr.Row():
            score_output = gr.Textbox(label="Job Fit Score (%)")
        def analyze(jd, resume):
            from job_description_analyzer import (
                extract_skills_from_jd_keywords,
                extract_skills_from_jd_finetuned,
                compare_resume_with_jd
            )
            keywords = extract_skills_from_jd_keywords(jd)
            finetuned = extract_skills_from_jd_finetuned(jd)
            score = compare_resume_with_jd(resume, jd)
            return ", ".join(keywords), ", ".join(finetuned), f"{score} %"
        analyze_button.click(
            fn=analyze,
            inputs=[jd_input, resume_input],
            outputs=[keyword_skills_output, finetuned_skills_output, score_output]
        )


    with gr.Tab("🎤 Voice Interview Assistant"):
        gr.Markdown("### Practice mock interviews using your voice")

        with gr.Row():
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Record Your Answer")
            transcribe_button = gr.Button("📝 Transcribe and Analyze")

        with gr.Row():
            transcript_output = gr.Textbox(label="🗒️ Transcribed Answer", lines=6)
            feedback_output = gr.Textbox(label="💬 AI Feedback", lines=4)

        def process_audio_and_feedback(audio_path):
            transcript = transcribe_audio_file(audio_path)
            feedback = analyze_speech_feedback(transcript)
            return transcript, feedback

        transcribe_button.click(
            fn=process_audio_and_feedback,
            inputs=[audio_input],
            outputs=[transcript_output, feedback_output]
        )



# Launch in browser
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)