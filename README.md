# Recipe Recommendation

A recipe recommender with a desktop PyQt interface (`main.py`) and a browser interface (`streamlit_app.py`). The browser app reads the existing recipe collection in `recipes.py`.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Free deployment

The browser app can be hosted for free on [Streamlit Community Cloud](https://share.streamlit.io/):

1. Push this repository to GitHub.
2. Sign in to Streamlit Community Cloud with GitHub and choose **Create app**.
3. Select this repository, the `main` branch, and `streamlit_app.py` as the app file.
4. Choose **Deploy**. Community Cloud will install `requirements.txt` and provide a public `*.streamlit.app` link.

The original PyQt desktop app remains available through `main.py`; Streamlit hosts the browser version.
