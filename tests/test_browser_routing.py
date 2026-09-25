#!/usr/bin/env python3
from __future__ import annotations

import unittest
from unittest.mock import patch

import ringer


class BrowserRoutingTests(unittest.TestCase):
    @patch.object(ringer.subprocess, "Popen")
    def test_named_macos_browser_opens_without_focus_steal(self, popen: object) -> None:
        with patch.object(ringer.sys, "platform", "darwin"):
            ringer.open_in_browser("http://127.0.0.1:8700", "Vivaldi")

        popen.assert_called_once_with(
            ["open", "-g", "-a", "Vivaldi", "http://127.0.0.1:8700"],
            stdout=ringer.subprocess.DEVNULL,
            stderr=ringer.subprocess.DEVNULL,
        )

    @patch.object(ringer.webbrowser, "open")
    def test_non_macos_keeps_webbrowser_fallback(self, browser_open: object) -> None:
        with patch.object(ringer.sys, "platform", "linux"):
            ringer.open_in_browser("http://127.0.0.1:8700", "Vivaldi")

        browser_open.assert_called_once_with("http://127.0.0.1:8700")


if __name__ == "__main__":
    unittest.main()
