import gradio as gr
# from AiInfused1 import summariser_langchain
from summariser_langchain import summarize


# ============================================================
# CSS
# ============================================================

css = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

:root {
    --bg: #f6f8fc;
    --card: #ffffff;
    --text: #172033;
    --muted: #687386;
    --border: #e5e9f2;
    --primary: #4f46e5;
    --primary-hover: #4338ca;
    --primary-light: #eef2ff;
}

body {
    background: #f6f8fc !important;
    font-family: "DM Sans", sans-serif !important;
    color: var(--text);
}

.gradio-container {
    max-width: 1180px !important;
    margin: auto !important;
    padding: 10px 12px 8px 12px !important;
}


/* ============================================================
   HEADER
   ============================================================ */

.hero {
    text-align: center;
    padding: 8px 10px 10px;
}

.hero-badge {
    display: inline-block;

    padding: 7px 7px;

    background: #eef2ff;
    color: #4f46e5;

    border: 1px solid #dfe3ff;
    border-radius: 999px;

    font-size: 6px;
    font-weight: 700;
}

.hero h1 {
    margin: 0 0 0px;

    font-family: "Plus Jakarta Sans", sans-serif !important;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -1.3px;

    color: #172033;
}

.hero h1 span {
    color: #4f46e5;
}

.hero p {
    margin: 0 auto;

    color: #687386;
    font-size: 12px;
    line-height: 1.5;
}


/* ============================================================
   TWO COLUMN LAYOUT
   ============================================================ */

.dashboard {
    display: flex !important;
    gap: 20px !important;
    align-items: stretch !important;
}

.left-panel,
.right-panel {
    background: #ffffff !important;

    border: 1px solid #e5e9f2 !important;
    border-radius: 20px !important;

    padding: 26px !important;

    box-shadow:
        0 8px 30px rgba(23, 32, 51, 0.06) !important;

    min-height: 570px !important;
}


/* Left side */

.left-panel {
    flex: 0 0 42% !important;
}


/* Right side */

.right-panel {
    flex: 1 !important;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: #172033;

    font-family: "Plus Jakarta Sans", sans-serif !important;

    font-size: 16px;
    font-weight: 700;

    margin-bottom: 7px;
}

.section-description {
    color: #7a8495;

    font-size: 13px;
    line-height: 1.5;

    margin-bottom: 16px;
}


/* ============================================================
   URL INPUT
   ============================================================ */

.url-input input {
    height: 52px !important;

    background: #fafbfe !important;

    color: #172033 !important;

    border: 1px solid #dfe4ed !important;
    border-radius: 12px !important;

    font-family: "DM Sans", sans-serif !important;
    font-size: 14px !important;
}

.url-input input::placeholder {
    color: #a0a8b6 !important;
}

.url-input input:focus {
    border-color: #818cf8 !important;

    box-shadow:
        0 0 0 3px rgba(79, 70, 229, 0.10) !important;
}


/* ============================================================
   PERSONALITY
   ============================================================ */

.personality-title {
    margin-top: 16px;
}

.personality-radio {
    border: none !important;
    background: transparent !important;
}

.personality-radio label {
    background: #fafbfe !important;

    border: 1px solid #e3e7ef !important;
    border-radius: 11px !important;

    color: #394458 !important;

    padding: 11px 13px !important;
    margin-bottom: 7px !important;

    font-size: 13px !important;
    font-weight: 600 !important;

    transition: all 0.18s ease !important;
}

.personality-radio label:hover {
    background: #f5f6ff !important;
    border-color: #a5b4fc !important;
}

.personality-radio label.selected {
    background: #eef2ff !important;
    border-color: #6366f1 !important;
    color: #4338ca !important;
}


/* ============================================================
   BUTTON
   ============================================================ */

#summarize-btn {
    width: 100% !important;

    height: 52px !important;

    margin-top: 20px !important;

    border: none !important;
    border-radius: 12px !important;

    background: #4f46e5 !important;

    color: white !important;

    font-family: "DM Sans", sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;

    box-shadow:
        0 5px 15px rgba(79, 70, 229, 0.20) !important;

    transition: all 0.2s ease !important;
}

#summarize-btn:hover {
    background: #4338ca !important;

    transform: translateY(-1px);

    box-shadow:
        0 8px 20px rgba(79, 70, 229, 0.25) !important;
}


/* ============================================================
   SUMMARY PANEL
   ============================================================ */

.summary-header {
    display: flex;

    align-items: center;
    justify-content: space-between;

    margin-bottom: 14px;
}

.summary-title {
    color: #172033;

    font-family: "Plus Jakarta Sans", sans-serif !important;

    font-size: 16px;
    font-weight: 700;
}

.summary-badge {
    padding: 5px 10px;

    background: #ecfdf5;

    color: #047857;

    border-radius: 999px;

    font-size: 11px;
    font-weight: 700;
}


/* Result window */

.output-box {
    height: 480px !important;

    overflow-y: auto !important;

    background: #fafbfe !important;

    border: 1px solid #e3e7ef !important;
    border-radius: 14px !important;

    padding: 20px !important;

    color: #293449 !important;

    font-size: 14px !important;
    line-height: 1.75 !important;
}


/* Markdown */

.output-box h1,
.output-box h2,
.output-box h3 {
    color: #172033 !important;

    font-family: "Plus Jakarta Sans", sans-serif !important;
}

.output-box strong {
    color: #3730a3 !important;
}

.output-box li {
    margin-bottom: 7px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;

    color: #98a1b1;

    font-size: 11px;

    padding: 18px 0 5px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 800px) {

    .gradio-container {
        padding: 20px 14px !important;
    }

    .hero h1 {
        font-size: 31px;
    }

    .dashboard {
        flex-direction: column !important;
    }

    .left-panel,
    .right-panel {
        min-height: auto !important;
    }

    .left-panel {
        flex: 1 !important;
    }

    .output-box {
        height: 400px !important;
    }
}
"""


# ============================================================
# PERSONALITIES
# ============================================================

personalities = [
    "✨ Executive",
    "⚡ Quick & Simple",
    "🧠 Detailed",
    "🎯 Key Takeaways",
    "😎 Casual",
]


# ============================================================
# FUNCTION
# ============================================================

def summarize_with_personality(url, personality):

    # Current summarize() accepts URL only.
    # Later you can change this to:
    #
    # return summarize(url, personality)

    return summarize(url)


# ============================================================
# UI
# ============================================================

with gr.Blocks(
    title="AI Website Summarizer",
    theme=gr.themes.Base(
        font=["DM Sans", "sans-serif"],
        font_mono=["monospace"],
        primary_hue="indigo",
        neutral_hue="slate",
    ),
    css=css
) as demo:

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    gr.HTML("""
    <div class="hero">

        <h1>
            Turn websites into
            <span>clear insights.</span>
        </h1>

        <p>
            Paste a URL, choose your personality, and get an instant AI summary.
        </p>

    </div>
    """)


    # --------------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------------

    with gr.Row(elem_classes="dashboard"):

        # ====================================================
        # LEFT PANEL
        # ====================================================

        with gr.Column(elem_classes="left-panel"):

            gr.HTML("""
            <div class="section-title">
                🌐 Website
            </div>

            <div class="section-description">
                Enter the URL of the website you want to summarize.
            </div>
            """)

            url_input = gr.Textbox(
                placeholder="https://example.com",
                show_label=False,
                elem_classes="url-input"
            )


            gr.HTML("""
            <div class="section-title personality-title">
                🎭 Personality Picks
            </div>

            <div class="section-description">
                Choose how your summary should sound.
            </div>
            """)

            personality = gr.Radio(
                choices=personalities,
                value="✨ Executive",
                show_label=False,
                elem_classes="personality-radio"
            )


            summarize_btn = gr.Button(
                "✨  Summarize Website",
                elem_id="summarize-btn"
            )


        # ====================================================
        # RIGHT PANEL
        # ====================================================

        with gr.Column(elem_classes="right-panel"):

            gr.HTML("""
            <div class="summary-header">

                <div class="summary-title">
                    📄 AI Summary
                </div>

                <div class="summary-badge">
                    READY
                </div>

            </div>
            """)

            output = gr.Markdown(
                value="""
### Your summary will appear here

Enter a website URL on the left and click **Summarize Website**.

Your result will stay in this window, so there's no need to scroll down.
""",
                elem_classes="output-box"
            )


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    gr.HTML("""
            
    <div class="footer-badge">
        ✦ AI-POWERED WEBSITE INTELLIGENCE
    </div>
            
    <div class="footer">
        Simple · Clear · Intelligent
    </div>
    """)


    # --------------------------------------------------------
    # EVENT
    # --------------------------------------------------------

    summarize_btn.click(
        fn=summarize_with_personality,
        inputs=[url_input, personality],
        outputs=output
    )


demo.launch(share=True)
