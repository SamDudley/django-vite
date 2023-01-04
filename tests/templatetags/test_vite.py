import pytest

import django_vite.templatetags.vite as vite
from django_vite.templatetags.vite import vite_css, vite_dev_client, vite_js


@pytest.mark.parametrize(
    ["is_dev", "filename", "html"],
    [
        (True, "main.css", ""),
        (False, "main.css", '<link rel="stylesheet" href="assets/main.83069a53.css">'),
    ],
)
def test_vite_css(monkeypatch, is_dev: bool, filename: str, html: str):
    monkeypatch.setattr(vite, "VITE_DEV", is_dev)
    assert vite_css(filename) == html


@pytest.mark.parametrize(
    ["is_dev", "html"],
    [
        (
            True,
            '<script type="module" src="http://localhost:5173/@vite/client"></script>',
        ),
        (False, ""),
    ],
)
def test_vite_dev_client(monkeypatch, is_dev: bool, html: str):
    monkeypatch.setattr(vite, "VITE_DEV", is_dev)
    assert vite_dev_client() == html


@pytest.mark.parametrize(
    ["is_dev", "filename", "html"],
    [
        (
            True,
            "main.js",
            '<script type="module" src="http://localhost:5173/main.js"></script>',
        ),
        (
            False,
            "foo/bar.js",
            '<script type="module" src="assets/foo.869aea0d.js"></script>',
        ),
    ],
)
def test_vite_js(monkeypatch, is_dev: bool, filename: str, html: str):
    monkeypatch.setattr(vite, "VITE_DEV", is_dev)
    assert vite_js(filename) == html
