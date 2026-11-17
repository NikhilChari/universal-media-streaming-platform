"""
Tests for Media Scanner and File Detection.
"""

import os
from backend.scanner import determine_media_type, extract_title_from_filename, scan_media_directory

def test_media_type_detection():
    assert determine_media_type(".mp3") == "audio"
    assert determine_media_type(".wav") == "audio"
    assert determine_media_type(".flac") == "audio"
    assert determine_media_type(".mp4") == "video"
    assert determine_media_type(".mkv") == "video"
    assert determine_media_type(".webm") == "video"
    assert determine_media_type(".txt") is None
    assert determine_media_type(".pdf") is None

def test_title_extraction():
    assert extract_title_from_filename("avengers_endgame.mp4") == "Avengers Endgame"
    assert extract_title_from_filename("pink_floyd_time.mp3") == "Pink Floyd Time"

def test_directory_scanning(setup_test_db):
    sample_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sample_media")
    result = scan_media_directory(sample_dir, db_path=setup_test_db)
    assert result["status"] == "completed"
    assert result["files_found"] >= 4
