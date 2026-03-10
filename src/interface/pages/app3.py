import os
import re

import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

name: str = "Transcrição YouTube"
order: int = 3
requires_auth: bool = True


def _extract_video_id(url: str) -> str | None:
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11})",
        r"(?:youtu\.be\/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def download_captions(url: str, languages: list[str]) -> tuple[str, str]:
    video_id = _extract_video_id(url)
    if not video_id:
        raise ValueError("URL inválida. Não foi possível extrair o ID do vídeo.")

    ytt = YouTubeTranscriptApi()
    transcript_list = ytt.list(video_id)

    try:
        transcript = transcript_list.find_transcript(languages)
    except NoTranscriptFound:
        transcript = transcript_list.find_generated_transcript(languages)

    title = f"Video {video_id}"
    entries = transcript.fetch()
    captions = " ".join(entry.text for entry in entries)
    return title, captions


def transcription_to_markdown(title: str, captions: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Variável de ambiente OPENAI_API_KEY não definida.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente que organiza transcrições de vídeos em Markdown. "
                    "Organize o texto em seções com títulos, parágrafos e listas quando adequado. "
                    "Corrija erros de transcrição automática e melhore a legibilidade."
                ),
            },
            {
                "role": "user",
                "content": f"Título do vídeo: {title}\n\nTranscrição:\n{captions}",
            },
        ],
    )

    return response.choices[0].message.content or ""


def render() -> None:
    st.markdown("<h1>Transcrição YouTube</h1>", unsafe_allow_html=True)

    url = st.text_input(
        "URL do vídeo", placeholder="https://www.youtube.com/watch?v=..."
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        run = st.button("Transcrever", use_container_width=True)
    with col2:
        clear = st.button("Limpar", use_container_width=True)

    if clear:
        st.session_state.pop("yt_transcript_result", None)
        st.rerun()

    if run:
        if not url:
            st.warning("Informe a URL do vídeo.")
        else:
            with st.spinner("Baixando e processando transcrição..."):
                try:
                    title, captions = download_captions(
                        url, languages=["pt", "pt-BR", "en"]
                    )
                    markdown = transcription_to_markdown(title, captions)
                    st.session_state["yt_transcript_result"] = markdown
                except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable) as e:
                    st.error(f"Transcrição não disponível: {e}")
                except ValueError as e:
                    st.error(str(e))
                except Exception as e:
                    st.error(f"Erro inesperado: {e}")

    result = st.session_state.get("yt_transcript_result")

    if result:
        st.code(result, language=None)
    else:
        st.text_area(
            "Resultado",
            value="",
            height=400,
            disabled=True,
            placeholder="A transcrição aparecerá aqui...",
        )
