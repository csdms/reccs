# Changelog

All notable changes to this project are documented here.

## [v0.4] — 2028-06-04

### Added
- Community health files: credits and support documents
- Links to standard CSDMS contributing and code of conduct documents
- GitHub Actions workflows for notebook checking and linting
- Nox sessions for checking and linting notebooks
- Pre-commit hooks configuration

### Fixed
- Notebook formatting: imports (isort), style (black), line endings
- Skip test cells that intentionally demonstrate errors

---

## [v0.3] — 2025-05-29

RECCS 2025: Python Programming in the Geosciences

### Changed
- Replace `environment.yaml` with pip `requirements.txt`
- Point nbgitpuller link to explore Hub
- Update current year references
- Modernize code: replace `%`-formatted prints with f-strings, remove unused `print` calls
- Rework library analogy; use f-string in one expression

---

## [v0.2] — 2023-06-06

RECCS 2023: Python Programming in the Geosciences

### Added
- Answers to exercises
- ipykernel dependency for JupyterHub use

### Changed
- Renumber notebooks
- Update text and links
- Save all notebooks in unrun state

### Removed
- Old notebook tutorial

### Fixed
- Post-class content fixes
- Update to `scipy.io.netcdf_file` (deprecated `scipy.io.netcdf` namespace)
- Add link to CSDMS Ivy course material; add list of additional topics

---

## [v0.1] — 2021-06-02

RECCS 2021: Python Programming in the Geosciences — initial release.

### Added
- Morning session: Python fundamentals, libraries, and a data example notebook
- Afternoon session: additional Python fundamentals and reanalysis data example
- NEON sonic anemometer data for examples
- Conda environment file
- Agenda, resources, acknowledgments, and overview
- Notebook tutorial and nbgitpuller launch link
- NSF and NEON data acknowledgments
- License covering instructional material
- Function docstring formatting
