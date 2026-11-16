# Gonzalo Loayza — portfolio

Jekyll portfolio connecting applied experience, case studies and public code.

- [Live site](https://gonza055.github.io/)
- [Applied case studies](https://gonza055.github.io/projects/)
- [Public code guide](https://gonza055.github.io/code/)

## Structure

`index.md` is the landing page; `projects.md` indexes the case studies. `_pages/` holds experience, code and resume pages. `assets/css/` contains the existing visual systems. `_data/navigation.yml` defines navigation.

## Build

Use Ruby 3.1 and Bundler, matching the existing GitHub Actions workflow:

```sh
bundle install
python -m pip install pillow reportlab
python scripts/generate_social_previews.py
python scripts/generate_resume_pdf.py
bundle exec jekyll build
```

The main-branch workflow builds and publishes to `gh-pages`. The resume PDF is generated from `scripts/generate_resume_pdf.py`; update that source alongside `_pages/resume.md` to keep both versions consistent.

## Content rules

Use expected graduation until the degree is conferred. Distinguish internship contributions, team prototypes and independent learning projects. Keep employer code and underlying operational datasets out of this repository. Case-study metrics describe the specific documented dataset or workflow; they are not general performance guarantees.
